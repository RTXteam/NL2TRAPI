# NL2TRAPI
A prototype investigation of converting natural language questions to the TRAPI format

## First draft plan

1. Named Entity Recognition (what is a concept and what representes a concrete bioentity)
    1. Sundar: what are the concepts and what are concrete bioentities
    2. Amy: What are the curies for these
2. Chunyu & David: Named entity linking
    1. stuff like https://ieeexplore.ieee.org/document/6823700
    2. https://medium.com/analytics-vidhya/entity-linking-a-primary-nlp-task-for-information-extraction-22f9d4b90aa8


## Environment Installation
Please install the necessary packages via [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) following the commands below:

```bash
# Clone the repo
git clone https://github.com/RTXteam/NL2TRAPI.git
cd NL2TRAPI

# Create a conda environment for YACHT
conda env create -f env/llm_ner.yaml
conda activate llm_ner
```

## Download Nodesynonymizer
Please download the node synonymizer database from the `arax-databases.rtx.ai` and put it under the `./NodeSynonymizer` folder. Pleae note that this needs you to have permission to access this server.

## Download ScispaCy training data
Please download the `en_core_sci_lg` model from [here](https://allenai.github.io/scispacy/). In short, this can be accomplished with
```bash
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.3/en_core_sci_lg-0.5.3.tar.gz
```

## Run a draft NER class for biomedical concepts
```python
# Import libraries
import json
from srcs import TRAPI_NER

## initalize trapi ner class
trapi_ner = TRAPI_NER(synonymizer_dir = './NodeSynonymizer', synonymizer_dbname = 'node_synonymizer_v1.1_KG2.8.0.1.sqlite', linker_name = ['umls', 'mesh'])


## Use Examples
sentence = "type 2 diabetes"
sentence = "Diabetes Mellitus, Type 2"
sentence = "type 1 diabetes"
sentence = 'diabetes'
sentence = "ibuprofen"
sentence = "Influenza"
sentence = "Swine influenza"
sentence = "Achromobacter"
sentence = 'what gene is assocaited with AK-Taine?'
sentence = 'SDFxddf'
sentence = 'Puerperal fever'
sentence = 'Periodontitis'
sentence = 'hemophilia B'
sentence = 'Christmas Disease'
sentence = 'Filgrastim (USP/INN)'


## run ner class
res = trapi_ner.get_kg2_match(sentence, remove_mark = True)
json_string = json.dumps(res, indent=4)
print(json_string)


``` 
