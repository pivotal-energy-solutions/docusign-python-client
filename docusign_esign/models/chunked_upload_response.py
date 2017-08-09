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


class ChunkedUploadResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, checksum=None, chunked_upload_id=None, chunked_upload_parts=None, chunked_upload_uri=None, committed=None, expiration_date_time=None, max_chunked_upload_parts=None, max_total_size=None, total_size=None):
        """
        ChunkedUploadResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'checksum': 'str',
            'chunked_upload_id': 'str',
            'chunked_upload_parts': 'list[ChunkedUploadPart]',
            'chunked_upload_uri': 'str',
            'committed': 'str',
            'expiration_date_time': 'str',
            'max_chunked_upload_parts': 'str',
            'max_total_size': 'str',
            'total_size': 'str'
        }

        self.attribute_map = {
            'checksum': 'checksum',
            'chunked_upload_id': 'chunkedUploadId',
            'chunked_upload_parts': 'chunkedUploadParts',
            'chunked_upload_uri': 'chunkedUploadUri',
            'committed': 'committed',
            'expiration_date_time': 'expirationDateTime',
            'max_chunked_upload_parts': 'maxChunkedUploadParts',
            'max_total_size': 'maxTotalSize',
            'total_size': 'totalSize'
        }

        self._checksum = checksum
        self._chunked_upload_id = chunked_upload_id
        self._chunked_upload_parts = chunked_upload_parts
        self._chunked_upload_uri = chunked_upload_uri
        self._committed = committed
        self._expiration_date_time = expiration_date_time
        self._max_chunked_upload_parts = max_chunked_upload_parts
        self._max_total_size = max_total_size
        self._total_size = total_size

    @property
    def checksum(self):
        """
        Gets the checksum of this ChunkedUploadResponse.
        

        :return: The checksum of this ChunkedUploadResponse.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """
        Sets the checksum of this ChunkedUploadResponse.
        

        :param checksum: The checksum of this ChunkedUploadResponse.
        :type: str
        """

        self._checksum = checksum

    @property
    def chunked_upload_id(self):
        """
        Gets the chunked_upload_id of this ChunkedUploadResponse.
        

        :return: The chunked_upload_id of this ChunkedUploadResponse.
        :rtype: str
        """
        return self._chunked_upload_id

    @chunked_upload_id.setter
    def chunked_upload_id(self, chunked_upload_id):
        """
        Sets the chunked_upload_id of this ChunkedUploadResponse.
        

        :param chunked_upload_id: The chunked_upload_id of this ChunkedUploadResponse.
        :type: str
        """

        self._chunked_upload_id = chunked_upload_id

    @property
    def chunked_upload_parts(self):
        """
        Gets the chunked_upload_parts of this ChunkedUploadResponse.
        

        :return: The chunked_upload_parts of this ChunkedUploadResponse.
        :rtype: list[ChunkedUploadPart]
        """
        return self._chunked_upload_parts

    @chunked_upload_parts.setter
    def chunked_upload_parts(self, chunked_upload_parts):
        """
        Sets the chunked_upload_parts of this ChunkedUploadResponse.
        

        :param chunked_upload_parts: The chunked_upload_parts of this ChunkedUploadResponse.
        :type: list[ChunkedUploadPart]
        """

        self._chunked_upload_parts = chunked_upload_parts

    @property
    def chunked_upload_uri(self):
        """
        Gets the chunked_upload_uri of this ChunkedUploadResponse.
        

        :return: The chunked_upload_uri of this ChunkedUploadResponse.
        :rtype: str
        """
        return self._chunked_upload_uri

    @chunked_upload_uri.setter
    def chunked_upload_uri(self, chunked_upload_uri):
        """
        Sets the chunked_upload_uri of this ChunkedUploadResponse.
        

        :param chunked_upload_uri: The chunked_upload_uri of this ChunkedUploadResponse.
        :type: str
        """

        self._chunked_upload_uri = chunked_upload_uri

    @property
    def committed(self):
        """
        Gets the committed of this ChunkedUploadResponse.
        

        :return: The committed of this ChunkedUploadResponse.
        :rtype: str
        """
        return self._committed

    @committed.setter
    def committed(self, committed):
        """
        Sets the committed of this ChunkedUploadResponse.
        

        :param committed: The committed of this ChunkedUploadResponse.
        :type: str
        """

        self._committed = committed

    @property
    def expiration_date_time(self):
        """
        Gets the expiration_date_time of this ChunkedUploadResponse.
        

        :return: The expiration_date_time of this ChunkedUploadResponse.
        :rtype: str
        """
        return self._expiration_date_time

    @expiration_date_time.setter
    def expiration_date_time(self, expiration_date_time):
        """
        Sets the expiration_date_time of this ChunkedUploadResponse.
        

        :param expiration_date_time: The expiration_date_time of this ChunkedUploadResponse.
        :type: str
        """

        self._expiration_date_time = expiration_date_time

    @property
    def max_chunked_upload_parts(self):
        """
        Gets the max_chunked_upload_parts of this ChunkedUploadResponse.
        

        :return: The max_chunked_upload_parts of this ChunkedUploadResponse.
        :rtype: str
        """
        return self._max_chunked_upload_parts

    @max_chunked_upload_parts.setter
    def max_chunked_upload_parts(self, max_chunked_upload_parts):
        """
        Sets the max_chunked_upload_parts of this ChunkedUploadResponse.
        

        :param max_chunked_upload_parts: The max_chunked_upload_parts of this ChunkedUploadResponse.
        :type: str
        """

        self._max_chunked_upload_parts = max_chunked_upload_parts

    @property
    def max_total_size(self):
        """
        Gets the max_total_size of this ChunkedUploadResponse.
        

        :return: The max_total_size of this ChunkedUploadResponse.
        :rtype: str
        """
        return self._max_total_size

    @max_total_size.setter
    def max_total_size(self, max_total_size):
        """
        Sets the max_total_size of this ChunkedUploadResponse.
        

        :param max_total_size: The max_total_size of this ChunkedUploadResponse.
        :type: str
        """

        self._max_total_size = max_total_size

    @property
    def total_size(self):
        """
        Gets the total_size of this ChunkedUploadResponse.
        

        :return: The total_size of this ChunkedUploadResponse.
        :rtype: str
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """
        Sets the total_size of this ChunkedUploadResponse.
        

        :param total_size: The total_size of this ChunkedUploadResponse.
        :type: str
        """

        self._total_size = total_size

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