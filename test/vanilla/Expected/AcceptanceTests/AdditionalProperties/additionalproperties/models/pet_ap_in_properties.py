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

from msrest.serialization import Model


class PetAPInProperties(Model):
    """PetAPInProperties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required.
    :type id: int
    :param name:
    :type name: str
    :ivar status:
    :vartype status: bool
    :param additional_properties:
    :type additional_properties: dict[str, float]
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
        'additional_properties': {'key': 'additionalProperties', 'type': '{float}'},
    }

    def __init__(self, **kwargs):
        super(PetAPInProperties, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.status = None
        self.additional_properties = kwargs.get('additional_properties', None)
