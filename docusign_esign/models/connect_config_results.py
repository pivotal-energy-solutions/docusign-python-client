# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConnectConfigResults(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, configurations=None, total_records=None):
        """
        ConnectConfigResults - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'configurations': 'list[ConnectCustomConfiguration]',
            'total_records': 'str'
        }

        self.attribute_map = {
            'configurations': 'configurations',
            'total_records': 'totalRecords'
        }

        self._configurations = configurations
        self._total_records = total_records

    @property
    def configurations(self):
        """
        Gets the configurations of this ConnectConfigResults.
        Reserved: TBD

        :return: The configurations of this ConnectConfigResults.
        :rtype: list[ConnectCustomConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this ConnectConfigResults.
        Reserved: TBD

        :param configurations: The configurations of this ConnectConfigResults.
        :type: list[ConnectCustomConfiguration]
        """

        self._configurations = configurations

    @property
    def total_records(self):
        """
        Gets the total_records of this ConnectConfigResults.
        

        :return: The total_records of this ConnectConfigResults.
        :rtype: str
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """
        Sets the total_records of this ConnectConfigResults.
        

        :param total_records: The total_records of this ConnectConfigResults.
        :type: str
        """

        self._total_records = total_records

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
