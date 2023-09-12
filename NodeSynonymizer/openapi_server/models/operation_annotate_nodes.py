# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.operation_annotate_nodes_parameters import OperationAnnotateNodesParameters
from openapi_server import util

from openapi_server.models.operation_annotate_nodes_parameters import OperationAnnotateNodesParameters  # noqa: E501

class OperationAnnotateNodes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, parameters=None):  # noqa: E501
        """OperationAnnotateNodes - a model defined in OpenAPI

        :param id: The id of this OperationAnnotateNodes.  # noqa: E501
        :type id: str
        :param parameters: The parameters of this OperationAnnotateNodes.  # noqa: E501
        :type parameters: OperationAnnotateNodesParameters
        """
        self.openapi_types = {
            'id': str,
            'parameters': OperationAnnotateNodesParameters
        }

        self.attribute_map = {
            'id': 'id',
            'parameters': 'parameters'
        }

        self._id = id
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'OperationAnnotateNodes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OperationAnnotateNodes of this OperationAnnotateNodes.  # noqa: E501
        :rtype: OperationAnnotateNodes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this OperationAnnotateNodes.


        :return: The id of this OperationAnnotateNodes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OperationAnnotateNodes.


        :param id: The id of this OperationAnnotateNodes.
        :type id: str
        """
        allowed_values = ["annotate_nodes"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def parameters(self):
        """Gets the parameters of this OperationAnnotateNodes.


        :return: The parameters of this OperationAnnotateNodes.
        :rtype: OperationAnnotateNodesParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this OperationAnnotateNodes.


        :param parameters: The parameters of this OperationAnnotateNodes.
        :type parameters: OperationAnnotateNodesParameters
        """

        self._parameters = parameters
