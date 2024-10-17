# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.22.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class UserBadgeOption(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'badge_slugs': 'list[str]'
    }

    attribute_map = {
        'badge_slugs': 'badge_slugs'
    }

    def __init__(self, badge_slugs=None, _configuration=None):  # noqa: E501
        """UserBadgeOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._badge_slugs = None
        self.discriminator = None

        if badge_slugs is not None:
            self.badge_slugs = badge_slugs

    @property
    def badge_slugs(self):
        """Gets the badge_slugs of this UserBadgeOption.  # noqa: E501


        :return: The badge_slugs of this UserBadgeOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._badge_slugs

    @badge_slugs.setter
    def badge_slugs(self, badge_slugs):
        """Sets the badge_slugs of this UserBadgeOption.


        :param badge_slugs: The badge_slugs of this UserBadgeOption.  # noqa: E501
        :type: list[str]
        """

        self._badge_slugs = badge_slugs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(UserBadgeOption, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserBadgeOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserBadgeOption):
            return True

        return self.to_dict() != other.to_dict()
