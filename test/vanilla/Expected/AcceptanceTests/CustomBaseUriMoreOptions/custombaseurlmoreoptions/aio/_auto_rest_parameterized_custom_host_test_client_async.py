# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AutoRestParameterizedCustomHostTestClientConfiguration
from .operations_async import PathsOperations
from .. import models


class AutoRestParameterizedCustomHostTestClient(object):
    """Test Infrastructure for AutoRest


    :ivar paths: PathsOperations operations
    :vartype paths: custombaseurlmoreoptions.aio.operations_async.PathsOperations
    :param subscription_id: The subscription id with value 'test12'.
    :type subscription_id: str
    :param dns_suffix: A string value that is used as a global part of the parameterized host. Default value 'host'.
    :type dns_suffix: str
    """

    def __init__(self, subscription_id, dns_suffix, **kwargs):

        base_url = '{vault}{secret}{dnsSuffix}'
        self._config = AutoRestParameterizedCustomHostTestClientConfiguration(subscription_id, dns_suffix, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self):
        await self._client.close()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
