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


class AccountPasswordMinimumPasswordAgeDays(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, maximum_age=None, minimum_age=None):
        """
        AccountPasswordMinimumPasswordAgeDays - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'maximum_age': 'str',
            'minimum_age': 'str'
        }

        self.attribute_map = {
            'maximum_age': 'maximumAge',
            'minimum_age': 'minimumAge'
        }

        self._maximum_age = maximum_age
        self._minimum_age = minimum_age

    @property
    def maximum_age(self):
        """
        Gets the maximum_age of this AccountPasswordMinimumPasswordAgeDays.
        

        :return: The maximum_age of this AccountPasswordMinimumPasswordAgeDays.
        :rtype: str
        """
        return self._maximum_age

    @maximum_age.setter
    def maximum_age(self, maximum_age):
        """
        Sets the maximum_age of this AccountPasswordMinimumPasswordAgeDays.
        

        :param maximum_age: The maximum_age of this AccountPasswordMinimumPasswordAgeDays.
        :type: str
        """

        self._maximum_age = maximum_age

    @property
    def minimum_age(self):
        """
        Gets the minimum_age of this AccountPasswordMinimumPasswordAgeDays.
        

        :return: The minimum_age of this AccountPasswordMinimumPasswordAgeDays.
        :rtype: str
        """
        return self._minimum_age

    @minimum_age.setter
    def minimum_age(self, minimum_age):
        """
        Sets the minimum_age of this AccountPasswordMinimumPasswordAgeDays.
        

        :param minimum_age: The minimum_age of this AccountPasswordMinimumPasswordAgeDays.
        :type: str
        """

        self._minimum_age = minimum_age

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
