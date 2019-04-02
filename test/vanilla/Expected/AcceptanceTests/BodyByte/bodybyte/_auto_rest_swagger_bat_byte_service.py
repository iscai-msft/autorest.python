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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AutoRestSwaggerBATByteServiceConfiguration
from .operations import ByteOperations
from . import models


class AutoRestSwaggerBATByteService(SDKClient):
    """Test Infrastructure for AutoRest Swagger BAT

    :ivar config: Configuration for client.
    :vartype config: AutoRestSwaggerBATByteServiceConfiguration

    :ivar byte: Byte operations
    :vartype byte: bodybyte.operations.ByteOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None, config=None, pipeline=None):

        self.config = config or AutoRestSwaggerBATByteServiceConfiguration(base_url)
        super(AutoRestSwaggerBATByteService, self).__init__(None, self.config, pipeline=pipeline)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.byte = ByteOperations(
            self._client, self.config, self._serialize, self._deserialize)