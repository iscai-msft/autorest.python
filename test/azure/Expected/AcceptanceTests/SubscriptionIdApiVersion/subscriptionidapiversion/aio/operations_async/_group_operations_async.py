# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import uuid
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models


class GroupOperations:
    """GroupOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config
    @distributed_trace_async
    async def get_sample_resource_group(self, resource_group_name, cls=None, **kwargs):
        """Provides a resouce group with name 'testgroup101' and location 'West US'..

        FIXME: add operation.summary


        :param resource_group_name: Resource Group name 'testgroup101'.
        :type resource_group_name: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: SampleResourceGroup or the result of cls(response)
        :rtype: ~subscriptionidapiversion.models.SampleResourceGroup
        :raises: ~subscriptionidapiversion.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_sample_resource_group.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        kwargs.setdefault('request_id', str(uuid.uuid1()))


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        deserialized = self._deserialize('SampleResourceGroup', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_sample_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'}

