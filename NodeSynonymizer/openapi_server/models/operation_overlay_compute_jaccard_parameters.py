# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class OperationOverlayComputeJaccardParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, end_node_keys=None, intermediate_node_key=None, virtual_relation_label=None):  # noqa: E501
        """OperationOverlayComputeJaccardParameters - a model defined in OpenAPI

        :param end_node_keys: The end_node_keys of this OperationOverlayComputeJaccardParameters.  # noqa: E501
        :type end_node_keys: List[str]
        :param intermediate_node_key: The intermediate_node_key of this OperationOverlayComputeJaccardParameters.  # noqa: E501
        :type intermediate_node_key: str
        :param virtual_relation_label: The virtual_relation_label of this OperationOverlayComputeJaccardParameters.  # noqa: E501
        :type virtual_relation_label: str
        """
        self.openapi_types = {
            'end_node_keys': List[str],
            'intermediate_node_key': str,
            'virtual_relation_label': str
        }

        self.attribute_map = {
            'end_node_keys': 'end_node_keys',
            'intermediate_node_key': 'intermediate_node_key',
            'virtual_relation_label': 'virtual_relation_label'
        }

        self._end_node_keys = end_node_keys
        self._intermediate_node_key = intermediate_node_key
        self._virtual_relation_label = virtual_relation_label

    @classmethod
    def from_dict(cls, dikt) -> 'OperationOverlayComputeJaccardParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OperationOverlayComputeJaccard_parameters of this OperationOverlayComputeJaccardParameters.  # noqa: E501
        :rtype: OperationOverlayComputeJaccardParameters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def end_node_keys(self):
        """Gets the end_node_keys of this OperationOverlayComputeJaccardParameters.

        A list of qnode keys specifying the ending nodes.  # noqa: E501

        :return: The end_node_keys of this OperationOverlayComputeJaccardParameters.
        :rtype: List[str]
        """
        return self._end_node_keys

    @end_node_keys.setter
    def end_node_keys(self, end_node_keys):
        """Sets the end_node_keys of this OperationOverlayComputeJaccardParameters.

        A list of qnode keys specifying the ending nodes.  # noqa: E501

        :param end_node_keys: The end_node_keys of this OperationOverlayComputeJaccardParameters.
        :type end_node_keys: List[str]
        """
        if end_node_keys is None:
            raise ValueError("Invalid value for `end_node_keys`, must not be `None`")  # noqa: E501

        self._end_node_keys = end_node_keys

    @property
    def intermediate_node_key(self):
        """Gets the intermediate_node_key of this OperationOverlayComputeJaccardParameters.

        A qnode key specifying the intermediate node.  # noqa: E501

        :return: The intermediate_node_key of this OperationOverlayComputeJaccardParameters.
        :rtype: str
        """
        return self._intermediate_node_key

    @intermediate_node_key.setter
    def intermediate_node_key(self, intermediate_node_key):
        """Sets the intermediate_node_key of this OperationOverlayComputeJaccardParameters.

        A qnode key specifying the intermediate node.  # noqa: E501

        :param intermediate_node_key: The intermediate_node_key of this OperationOverlayComputeJaccardParameters.
        :type intermediate_node_key: str
        """
        if intermediate_node_key is None:
            raise ValueError("Invalid value for `intermediate_node_key`, must not be `None`")  # noqa: E501

        self._intermediate_node_key = intermediate_node_key

    @property
    def virtual_relation_label(self):
        """Gets the virtual_relation_label of this OperationOverlayComputeJaccardParameters.

        The key of the query graph edge that corresponds to the knowledge graph edges that were added by this operation.  # noqa: E501

        :return: The virtual_relation_label of this OperationOverlayComputeJaccardParameters.
        :rtype: str
        """
        return self._virtual_relation_label

    @virtual_relation_label.setter
    def virtual_relation_label(self, virtual_relation_label):
        """Sets the virtual_relation_label of this OperationOverlayComputeJaccardParameters.

        The key of the query graph edge that corresponds to the knowledge graph edges that were added by this operation.  # noqa: E501

        :param virtual_relation_label: The virtual_relation_label of this OperationOverlayComputeJaccardParameters.
        :type virtual_relation_label: str
        """
        if virtual_relation_label is None:
            raise ValueError("Invalid value for `virtual_relation_label`, must not be `None`")  # noqa: E501

        self._virtual_relation_label = virtual_relation_label
