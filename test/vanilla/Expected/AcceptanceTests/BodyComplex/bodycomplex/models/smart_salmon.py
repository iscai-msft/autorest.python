# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .salmon import Salmon


class SmartSalmon(Salmon):
    """SmartSalmon.

    All required parameters must be populated in order to send to Azure.

    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param location:
    :type location: str
    :param iswild:
    :type iswild: bool
    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param college_degree:
    :type college_degree: str
    """

    _validation = {
        'length': {'required': True},
        'fishtype': {'required': True},
    }

    _attribute_map = {
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
        'fishtype': {'key': 'fishtype', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'iswild': {'key': 'iswild', 'type': 'bool'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'college_degree': {'key': 'college_degree', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SmartSalmon, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.college_degree = kwargs.get('college_degree', None)
        self.fishtype = 'smart_salmon'
