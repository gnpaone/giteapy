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


class NodeInfo(object):
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
        'metadata': 'object',
        'open_registrations': 'bool',
        'protocols': 'list[str]',
        'services': 'NodeInfoServices',
        'software': 'NodeInfoSoftware',
        'usage': 'NodeInfoUsage',
        'version': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'open_registrations': 'openRegistrations',
        'protocols': 'protocols',
        'services': 'services',
        'software': 'software',
        'usage': 'usage',
        'version': 'version'
    }

    def __init__(self, metadata=None, open_registrations=None, protocols=None, services=None, software=None, usage=None, version=None, _configuration=None):  # noqa: E501
        """NodeInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._metadata = None
        self._open_registrations = None
        self._protocols = None
        self._services = None
        self._software = None
        self._usage = None
        self._version = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if open_registrations is not None:
            self.open_registrations = open_registrations
        if protocols is not None:
            self.protocols = protocols
        if services is not None:
            self.services = services
        if software is not None:
            self.software = software
        if usage is not None:
            self.usage = usage
        if version is not None:
            self.version = version

    @property
    def metadata(self):
        """Gets the metadata of this NodeInfo.  # noqa: E501


        :return: The metadata of this NodeInfo.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NodeInfo.


        :param metadata: The metadata of this NodeInfo.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def open_registrations(self):
        """Gets the open_registrations of this NodeInfo.  # noqa: E501


        :return: The open_registrations of this NodeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._open_registrations

    @open_registrations.setter
    def open_registrations(self, open_registrations):
        """Sets the open_registrations of this NodeInfo.


        :param open_registrations: The open_registrations of this NodeInfo.  # noqa: E501
        :type: bool
        """

        self._open_registrations = open_registrations

    @property
    def protocols(self):
        """Gets the protocols of this NodeInfo.  # noqa: E501


        :return: The protocols of this NodeInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this NodeInfo.


        :param protocols: The protocols of this NodeInfo.  # noqa: E501
        :type: list[str]
        """

        self._protocols = protocols

    @property
    def services(self):
        """Gets the services of this NodeInfo.  # noqa: E501


        :return: The services of this NodeInfo.  # noqa: E501
        :rtype: NodeInfoServices
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this NodeInfo.


        :param services: The services of this NodeInfo.  # noqa: E501
        :type: NodeInfoServices
        """

        self._services = services

    @property
    def software(self):
        """Gets the software of this NodeInfo.  # noqa: E501


        :return: The software of this NodeInfo.  # noqa: E501
        :rtype: NodeInfoSoftware
        """
        return self._software

    @software.setter
    def software(self, software):
        """Sets the software of this NodeInfo.


        :param software: The software of this NodeInfo.  # noqa: E501
        :type: NodeInfoSoftware
        """

        self._software = software

    @property
    def usage(self):
        """Gets the usage of this NodeInfo.  # noqa: E501


        :return: The usage of this NodeInfo.  # noqa: E501
        :rtype: NodeInfoUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this NodeInfo.


        :param usage: The usage of this NodeInfo.  # noqa: E501
        :type: NodeInfoUsage
        """

        self._usage = usage

    @property
    def version(self):
        """Gets the version of this NodeInfo.  # noqa: E501


        :return: The version of this NodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NodeInfo.


        :param version: The version of this NodeInfo.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(NodeInfo, dict):
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
        if not isinstance(other, NodeInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeInfo):
            return True

        return self.to_dict() != other.to_dict()
