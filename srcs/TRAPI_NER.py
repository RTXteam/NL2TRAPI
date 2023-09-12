## Import libraries
import os, sys
from .utils import get_logger
from typing import Union, List
import spacy
import scispacy
from scispacy.linking import EntityLinker
from scispacy.abbreviation import AbbreviationDetector
import json

class TRAPI_NER:
    
    def __init__(self, synonymizer_dir: str, synonymizer_dbname: str, 
                 spacy_model: str = 'en_core_sci_lg', 
                 linker_name: Union[str, List] = 'umls', 
                 threshold: float = 0.99, 
                 num_neighbors: int = 5):
        # Setup logger
        self.logger = get_logger()
        
        # Import Node Synonymizer
        sys.path.append(synonymizer_dir)
        from node_synonymizer import NodeSynonymizer
        self.synonymizer = NodeSynonymizer(synonymizer_dir, synonymizer_dbname)
        
        # Check if the input linker_name is valid
        if type(linker_name) not in [str, list]:
            raise ValueError("linker_name must be a string or list of strings")
        if type(linker_name) is str:
            linker_name = [linker_name]
        self.logger.info("Input linker_name: {}".format(linker_name))
        
        intersect_link_names = list(set([x.lower() for x in linker_name]).intersection(set(['umls', 'mesh'])))
        if len(intersect_link_names) == 0:
            raise ValueError("linker_name must be one of: umls, mesh or both of them")
        self.available_linker_names = intersect_link_names
        
        # Load spacy models
        for x in self.available_linker_names:
            self.logger.info("Setting up NER with linker: {}".format(x))
            model_name = f"nlp_{x}"
            setattr(self, model_name, spacy.load(spacy_model))
            nlp = getattr(self, model_name)
            nlp.add_pipe("abbreviation_detector")
            nlp.add_pipe("scispacy_linker", config={"resolve_abbreviations": True, "linker_name": x, "threshold": threshold, "k": num_neighbors})

    def _get_preferred_curies_info(self, query: Union[str, List]) -> dict:
        """
        Helper function to fetch information on preferred curies.
        
        Args:
        - query (list or str): List of curies or an entity to get information for.
        
        Returns:
        - dict: Information on preferred curies.
        """
        
        # query node synonymizer
        if isinstance(query, list):
            res = self.synonymizer.get_canonical_curies(query)
        else:
            res = self.synonymizer.get_canonical_curies(names=query)
        temp_dict = {}
        
        for curie, content in res.items():
            if content:
                preferred_curie = content['preferred_curie']
                preferred_info = {'preferred_name': content['preferred_name'],
                                'preferred_category': content['preferred_category'],
                                'matched_synonyms': temp_dict.get(preferred_curie, {}).get('matched_synonyms', []) + [curie]}
                temp_dict[preferred_curie] = preferred_info
        
        # Sort based on the number of matched synonyms
        return sorted(temp_dict.items(), key=lambda x: len(x[1]['matched_synonyms']), reverse=True)

    def get_kg2_match(self, sentence: str, remove_mark: bool = True):
        """
        Extract entities from a sentence and return the KG2 matched preferred curies
            
        Args:
        - sentence (str): The input sentence to extract entities from.
        - remove_mark (bool): Flag to decide whether to remove punctuation marks.
        
        Returns:
        - dict: Matched entities to their preferred curies.
        """
        # Validate the input sentence
        if not isinstance(sentence, str) or not sentence:
            return {}
        
        # Remove punctuation marks if needed
        if remove_mark:
            sentence = sentence.translate(str.maketrans("", "", ".,;:?!"))
        
        # Extract entities using available linkers
        self._detected_entities = {}
        for linker_name in self.available_linker_names:
            doc = getattr(self, f"nlp_{linker_name}")(sentence)
            for ent in doc.ents:
                self._detected_entities.setdefault(ent.text, set()).update([f"{linker_name.upper()}:{x[0]}" for x in ent._.kb_ents])
        
        # Obtain preferred curies for detected entities
        matched_dict = {}
        if len(self._detected_entities) > 0:
            for entity, curies in self._detected_entities.items():
                curie_to_info = self._get_preferred_curies_info(list(curies) if curies else entity)
                if curie_to_info:
                    matched_dict[entity] = curie_to_info
        else:
            curie_to_info = self._get_preferred_curies_info(sentence)
            if curie_to_info:
                matched_dict[sentence] = curie_to_info
                
        return matched_dict


    def check_equivalent(self, name: str, curie: str):
        """
        Check if the given name of UMLS/MESH curie is equivalent can match to its preferred curie.
        
        Args:
        - name (str): Name to be checked.
        - curie (str): UMLS/MESH curie.
        
        Returns:
        - bool: True if name matches the preferred curie, otherwise False.
        """
        # Check if the given curie is UMLS or MESH
        if not (type(curie) is str and (curie.startswith('UMLS:') or curie.startswith('MESH:')) and type(name) is str):
            return False
        
        # Get preferred curie of the given curie
        res = self.synonymizer.get_canonical_curies(curie)
        res = [content['preferred_curie'] for _, content in res.items() if content]
        if len(res) == 0:
            return False
        else:
            preferred_curie = res[0]

        # Check if the given name can match to the preferred curie
        res = self.get_kg2_match(name, use_synonymizer = False, remove_mark = True)
        if len(res) == 0:
            return False
        else:
            return preferred_curie in [res[key][0][0] for key in res]
