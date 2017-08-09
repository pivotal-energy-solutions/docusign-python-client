# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LoginAccount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account_id=None, account_id_guid=None, base_url=None, email=None, is_default=None, login_account_settings=None, login_user_settings=None, name=None, site_description=None, user_id=None, user_name=None):
        """
        LoginAccount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account_id': 'str',
            'account_id_guid': 'str',
            'base_url': 'str',
            'email': 'str',
            'is_default': 'str',
            'login_account_settings': 'list[NameValue]',
            'login_user_settings': 'list[NameValue]',
            'name': 'str',
            'site_description': 'str',
            'user_id': 'str',
            'user_name': 'str'
        }

        self.attribute_map = {
            'account_id': 'accountId',
            'account_id_guid': 'accountIdGuid',
            'base_url': 'baseUrl',
            'email': 'email',
            'is_default': 'isDefault',
            'login_account_settings': 'loginAccountSettings',
            'login_user_settings': 'loginUserSettings',
            'name': 'name',
            'site_description': 'siteDescription',
            'user_id': 'userId',
            'user_name': 'userName'
        }

        self._account_id = account_id
        self._account_id_guid = account_id_guid
        self._base_url = base_url
        self._email = email
        self._is_default = is_default
        self._login_account_settings = login_account_settings
        self._login_user_settings = login_user_settings
        self._name = name
        self._site_description = site_description
        self._user_id = user_id
        self._user_name = user_name

    @property
    def account_id(self):
        """
        Gets the account_id of this LoginAccount.
        The account ID associated with the envelope.

        :return: The account_id of this LoginAccount.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this LoginAccount.
        The account ID associated with the envelope.

        :param account_id: The account_id of this LoginAccount.
        :type: str
        """

        self._account_id = account_id

    @property
    def account_id_guid(self):
        """
        Gets the account_id_guid of this LoginAccount.
        The GUID associated with the account ID.

        :return: The account_id_guid of this LoginAccount.
        :rtype: str
        """
        return self._account_id_guid

    @account_id_guid.setter
    def account_id_guid(self, account_id_guid):
        """
        Sets the account_id_guid of this LoginAccount.
        The GUID associated with the account ID.

        :param account_id_guid: The account_id_guid of this LoginAccount.
        :type: str
        """

        self._account_id_guid = account_id_guid

    @property
    def base_url(self):
        """
        Gets the base_url of this LoginAccount.
        The URL that should be used for successive calls to this account. It includes the protocal (https), the DocuSign server where the account is located, and the account number. Use this Url to make API calls against this account. Many of the API calls provide Uri's that are relative to this baseUrl.

        :return: The base_url of this LoginAccount.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """
        Sets the base_url of this LoginAccount.
        The URL that should be used for successive calls to this account. It includes the protocal (https), the DocuSign server where the account is located, and the account number. Use this Url to make API calls against this account. Many of the API calls provide Uri's that are relative to this baseUrl.

        :param base_url: The base_url of this LoginAccount.
        :type: str
        """

        self._base_url = base_url

    @property
    def email(self):
        """
        Gets the email of this LoginAccount.
        The email address for the user.

        :return: The email of this LoginAccount.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this LoginAccount.
        The email address for the user.

        :param email: The email of this LoginAccount.
        :type: str
        """

        self._email = email

    @property
    def is_default(self):
        """
        Gets the is_default of this LoginAccount.
        This value is true if this is the default account for the user, otherwise false is returned.

        :return: The is_default of this LoginAccount.
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this LoginAccount.
        This value is true if this is the default account for the user, otherwise false is returned.

        :param is_default: The is_default of this LoginAccount.
        :type: str
        """

        self._is_default = is_default

    @property
    def login_account_settings(self):
        """
        Gets the login_account_settings of this LoginAccount.
        A list of settings on the acccount that indicate what features are available.

        :return: The login_account_settings of this LoginAccount.
        :rtype: list[NameValue]
        """
        return self._login_account_settings

    @login_account_settings.setter
    def login_account_settings(self, login_account_settings):
        """
        Sets the login_account_settings of this LoginAccount.
        A list of settings on the acccount that indicate what features are available.

        :param login_account_settings: The login_account_settings of this LoginAccount.
        :type: list[NameValue]
        """

        self._login_account_settings = login_account_settings

    @property
    def login_user_settings(self):
        """
        Gets the login_user_settings of this LoginAccount.
        A list of user-level settings that indicate what user-specific features are available.

        :return: The login_user_settings of this LoginAccount.
        :rtype: list[NameValue]
        """
        return self._login_user_settings

    @login_user_settings.setter
    def login_user_settings(self, login_user_settings):
        """
        Sets the login_user_settings of this LoginAccount.
        A list of user-level settings that indicate what user-specific features are available.

        :param login_user_settings: The login_user_settings of this LoginAccount.
        :type: list[NameValue]
        """

        self._login_user_settings = login_user_settings

    @property
    def name(self):
        """
        Gets the name of this LoginAccount.
        The name associated with the account.

        :return: The name of this LoginAccount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LoginAccount.
        The name associated with the account.

        :param name: The name of this LoginAccount.
        :type: str
        """

        self._name = name

    @property
    def site_description(self):
        """
        Gets the site_description of this LoginAccount.
        An optional descirption of the site that hosts the account.

        :return: The site_description of this LoginAccount.
        :rtype: str
        """
        return self._site_description

    @site_description.setter
    def site_description(self, site_description):
        """
        Sets the site_description of this LoginAccount.
        An optional descirption of the site that hosts the account.

        :param site_description: The site_description of this LoginAccount.
        :type: str
        """

        self._site_description = site_description

    @property
    def user_id(self):
        """
        Gets the user_id of this LoginAccount.
        

        :return: The user_id of this LoginAccount.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this LoginAccount.
        

        :param user_id: The user_id of this LoginAccount.
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """
        Gets the user_name of this LoginAccount.
        The name of this user as defined by the account.

        :return: The user_name of this LoginAccount.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this LoginAccount.
        The name of this user as defined by the account.

        :param user_name: The user_name of this LoginAccount.
        :type: str
        """

        self._user_name = user_name

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