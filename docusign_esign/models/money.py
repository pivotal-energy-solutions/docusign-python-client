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


class Money(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, amount_in_base_unit=None, currency=None, display_amount=None):
        """
        Money - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'amount_in_base_unit': 'str',
            'currency': 'str',
            'display_amount': 'str'
        }

        self.attribute_map = {
            'amount_in_base_unit': 'amountInBaseUnit',
            'currency': 'currency',
            'display_amount': 'displayAmount'
        }

        self._amount_in_base_unit = amount_in_base_unit
        self._currency = currency
        self._display_amount = display_amount

    @property
    def amount_in_base_unit(self):
        """
        Gets the amount_in_base_unit of this Money.
        

        :return: The amount_in_base_unit of this Money.
        :rtype: str
        """
        return self._amount_in_base_unit

    @amount_in_base_unit.setter
    def amount_in_base_unit(self, amount_in_base_unit):
        """
        Sets the amount_in_base_unit of this Money.
        

        :param amount_in_base_unit: The amount_in_base_unit of this Money.
        :type: str
        """

        self._amount_in_base_unit = amount_in_base_unit

    @property
    def currency(self):
        """
        Gets the currency of this Money.
        

        :return: The currency of this Money.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Money.
        

        :param currency: The currency of this Money.
        :type: str
        """

        self._currency = currency

    @property
    def display_amount(self):
        """
        Gets the display_amount of this Money.
        

        :return: The display_amount of this Money.
        :rtype: str
        """
        return self._display_amount

    @display_amount.setter
    def display_amount(self, display_amount):
        """
        Sets the display_amount of this Money.
        

        :param display_amount: The display_amount of this Money.
        :type: str
        """

        self._display_amount = display_amount

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
