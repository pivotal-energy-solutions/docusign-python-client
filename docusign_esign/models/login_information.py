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


class LoginInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_password=None, login_accounts=None):
        """
        LoginInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_password': 'str',
            'login_accounts': 'list[LoginAccount]'
        }

        self.attribute_map = {
            'api_password': 'apiPassword',
            'login_accounts': 'loginAccounts'
        }

        self._api_password = api_password
        self._login_accounts = login_accounts

    @property
    def api_password(self):
        """
        Gets the api_password of this LoginInformation.
        Contains a token that can be used for authentication in API calls instead of using the user name and password. Only returned if the `api_password=true` query string is added to the URL.

        :return: The api_password of this LoginInformation.
        :rtype: str
        """
        return self._api_password

    @api_password.setter
    def api_password(self, api_password):
        """
        Sets the api_password of this LoginInformation.
        Contains a token that can be used for authentication in API calls instead of using the user name and password. Only returned if the `api_password=true` query string is added to the URL.

        :param api_password: The api_password of this LoginInformation.
        :type: str
        """

        self._api_password = api_password

    @property
    def login_accounts(self):
        """
        Gets the login_accounts of this LoginInformation.
        The list of accounts that authenticating user is a member of.

        :return: The login_accounts of this LoginInformation.
        :rtype: list[LoginAccount]
        """
        return self._login_accounts

    @login_accounts.setter
    def login_accounts(self, login_accounts):
        """
        Sets the login_accounts of this LoginInformation.
        The list of accounts that authenticating user is a member of.

        :param login_accounts: The login_accounts of this LoginInformation.
        :type: list[LoginAccount]
        """

        self._login_accounts = login_accounts

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
