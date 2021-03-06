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


class SenderEmailNotifications(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, changed_signer=None, comments_only_private_and_mention=None, comments_receive_all=None, delivery_failed=None, envelope_complete=None, offline_signing_failed=None, recipient_viewed=None, sender_envelope_declined=None, withdrawn_consent=None):
        """
        SenderEmailNotifications - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'changed_signer': 'str',
            'comments_only_private_and_mention': 'str',
            'comments_receive_all': 'str',
            'delivery_failed': 'str',
            'envelope_complete': 'str',
            'offline_signing_failed': 'str',
            'recipient_viewed': 'str',
            'sender_envelope_declined': 'str',
            'withdrawn_consent': 'str'
        }

        self.attribute_map = {
            'changed_signer': 'changedSigner',
            'comments_only_private_and_mention': 'commentsOnlyPrivateAndMention',
            'comments_receive_all': 'commentsReceiveAll',
            'delivery_failed': 'deliveryFailed',
            'envelope_complete': 'envelopeComplete',
            'offline_signing_failed': 'offlineSigningFailed',
            'recipient_viewed': 'recipientViewed',
            'sender_envelope_declined': 'senderEnvelopeDeclined',
            'withdrawn_consent': 'withdrawnConsent'
        }

        self._changed_signer = changed_signer
        self._comments_only_private_and_mention = comments_only_private_and_mention
        self._comments_receive_all = comments_receive_all
        self._delivery_failed = delivery_failed
        self._envelope_complete = envelope_complete
        self._offline_signing_failed = offline_signing_failed
        self._recipient_viewed = recipient_viewed
        self._sender_envelope_declined = sender_envelope_declined
        self._withdrawn_consent = withdrawn_consent

    @property
    def changed_signer(self):
        """
        Gets the changed_signer of this SenderEmailNotifications.
        When set to **true**, the sender receives notification if the signer changes.

        :return: The changed_signer of this SenderEmailNotifications.
        :rtype: str
        """
        return self._changed_signer

    @changed_signer.setter
    def changed_signer(self, changed_signer):
        """
        Sets the changed_signer of this SenderEmailNotifications.
        When set to **true**, the sender receives notification if the signer changes.

        :param changed_signer: The changed_signer of this SenderEmailNotifications.
        :type: str
        """

        self._changed_signer = changed_signer

    @property
    def comments_only_private_and_mention(self):
        """
        Gets the comments_only_private_and_mention of this SenderEmailNotifications.
        

        :return: The comments_only_private_and_mention of this SenderEmailNotifications.
        :rtype: str
        """
        return self._comments_only_private_and_mention

    @comments_only_private_and_mention.setter
    def comments_only_private_and_mention(self, comments_only_private_and_mention):
        """
        Sets the comments_only_private_and_mention of this SenderEmailNotifications.
        

        :param comments_only_private_and_mention: The comments_only_private_and_mention of this SenderEmailNotifications.
        :type: str
        """

        self._comments_only_private_and_mention = comments_only_private_and_mention

    @property
    def comments_receive_all(self):
        """
        Gets the comments_receive_all of this SenderEmailNotifications.
        

        :return: The comments_receive_all of this SenderEmailNotifications.
        :rtype: str
        """
        return self._comments_receive_all

    @comments_receive_all.setter
    def comments_receive_all(self, comments_receive_all):
        """
        Sets the comments_receive_all of this SenderEmailNotifications.
        

        :param comments_receive_all: The comments_receive_all of this SenderEmailNotifications.
        :type: str
        """

        self._comments_receive_all = comments_receive_all

    @property
    def delivery_failed(self):
        """
        Gets the delivery_failed of this SenderEmailNotifications.
        When set to **true**, the sender receives notification if the delivery of the envelope fails.

        :return: The delivery_failed of this SenderEmailNotifications.
        :rtype: str
        """
        return self._delivery_failed

    @delivery_failed.setter
    def delivery_failed(self, delivery_failed):
        """
        Sets the delivery_failed of this SenderEmailNotifications.
        When set to **true**, the sender receives notification if the delivery of the envelope fails.

        :param delivery_failed: The delivery_failed of this SenderEmailNotifications.
        :type: str
        """

        self._delivery_failed = delivery_failed

    @property
    def envelope_complete(self):
        """
        Gets the envelope_complete of this SenderEmailNotifications.
        When set to **true**, the user receives notification that the envelope has been completed.

        :return: The envelope_complete of this SenderEmailNotifications.
        :rtype: str
        """
        return self._envelope_complete

    @envelope_complete.setter
    def envelope_complete(self, envelope_complete):
        """
        Sets the envelope_complete of this SenderEmailNotifications.
        When set to **true**, the user receives notification that the envelope has been completed.

        :param envelope_complete: The envelope_complete of this SenderEmailNotifications.
        :type: str
        """

        self._envelope_complete = envelope_complete

    @property
    def offline_signing_failed(self):
        """
        Gets the offline_signing_failed of this SenderEmailNotifications.
        When set to **true**, the user receives notification if the offline signing failed.

        :return: The offline_signing_failed of this SenderEmailNotifications.
        :rtype: str
        """
        return self._offline_signing_failed

    @offline_signing_failed.setter
    def offline_signing_failed(self, offline_signing_failed):
        """
        Sets the offline_signing_failed of this SenderEmailNotifications.
        When set to **true**, the user receives notification if the offline signing failed.

        :param offline_signing_failed: The offline_signing_failed of this SenderEmailNotifications.
        :type: str
        """

        self._offline_signing_failed = offline_signing_failed

    @property
    def recipient_viewed(self):
        """
        Gets the recipient_viewed of this SenderEmailNotifications.
        When set to **true**, the sender receives notification that the recipient viewed the enveloper.

        :return: The recipient_viewed of this SenderEmailNotifications.
        :rtype: str
        """
        return self._recipient_viewed

    @recipient_viewed.setter
    def recipient_viewed(self, recipient_viewed):
        """
        Sets the recipient_viewed of this SenderEmailNotifications.
        When set to **true**, the sender receives notification that the recipient viewed the enveloper.

        :param recipient_viewed: The recipient_viewed of this SenderEmailNotifications.
        :type: str
        """

        self._recipient_viewed = recipient_viewed

    @property
    def sender_envelope_declined(self):
        """
        Gets the sender_envelope_declined of this SenderEmailNotifications.
        

        :return: The sender_envelope_declined of this SenderEmailNotifications.
        :rtype: str
        """
        return self._sender_envelope_declined

    @sender_envelope_declined.setter
    def sender_envelope_declined(self, sender_envelope_declined):
        """
        Sets the sender_envelope_declined of this SenderEmailNotifications.
        

        :param sender_envelope_declined: The sender_envelope_declined of this SenderEmailNotifications.
        :type: str
        """

        self._sender_envelope_declined = sender_envelope_declined

    @property
    def withdrawn_consent(self):
        """
        Gets the withdrawn_consent of this SenderEmailNotifications.
        When set to **true**, the user receives notification if consent is withdrawn.

        :return: The withdrawn_consent of this SenderEmailNotifications.
        :rtype: str
        """
        return self._withdrawn_consent

    @withdrawn_consent.setter
    def withdrawn_consent(self, withdrawn_consent):
        """
        Sets the withdrawn_consent of this SenderEmailNotifications.
        When set to **true**, the user receives notification if consent is withdrawn.

        :param withdrawn_consent: The withdrawn_consent of this SenderEmailNotifications.
        :type: str
        """

        self._withdrawn_consent = withdrawn_consent

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
