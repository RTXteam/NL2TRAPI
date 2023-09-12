# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.operation_filter_results_top_n_parameters import OperationFilterResultsTopNParameters
from openapi_server import util

from openapi_server.models.operation_filter_results_top_n_parameters import OperationFilterResultsTopNParameters  # noqa: E501

class OperationFilterResultsTopN(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, parameters=None):  # noqa: E501
        """OperationFilterResultsTopN - a model defined in OpenAPI

        :param id: The id of this OperationFilterResultsTopN.  # noqa: E501
        :type id: str
        :param parameters: The parameters of this OperationFilterResultsTopN.  # noqa: E501
        :type parameters: OperationFilterResultsTopNParameters
        """
        self.openapi_types = {
            'id': str,
            'parameters': OperationFilterResultsTopNParameters
        }

        self.attribute_map = {
            'id': 'id',
            'parameters': 'parameters'
        }

        self._id = id
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'OperationFilterResultsTopN':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OperationFilterResultsTopN of this OperationFilterResultsTopN.  # noqa: E501
        :rtype: OperationFilterResultsTopN
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this OperationFilterResultsTopN.


        :return: The id of this OperationFilterResultsTopN.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OperationFilterResultsTopN.


        :param id: The id of this OperationFilterResultsTopN.
        :type id: str
        """
        allowed_values = ["filter_results_top_n"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def parameters(self):
        """Gets the parameters of this OperationFilterResultsTopN.


        :return: The parameters of this OperationFilterResultsTopN.
        :rtype: OperationFilterResultsTopNParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this OperationFilterResultsTopN.


        :param parameters: The parameters of this OperationFilterResultsTopN.
        :type parameters: OperationFilterResultsTopNParameters
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters
