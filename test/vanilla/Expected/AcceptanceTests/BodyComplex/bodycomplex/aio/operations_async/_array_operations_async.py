# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models


class ArrayOperations:
    """ArrayOperations async operations.

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
    async def get_valid(self, cls=None, **kwargs):
        """Get complex types with array property.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: ArrayWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.ArrayWrapper
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        deserialized = self._deserialize('ArrayWrapper', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_valid.metadata = {'url': '/complex/array/valid'}

    @distributed_trace_async
    async def put_valid(self, array=None, cls=None, **kwargs):
        """Put complex types with array property.

        FIXME: add operation.summary


        :param array: 
        :type array: list[str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)
        complex_body = models.ArrayWrapper(array=array)

        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(complex_body, 'ArrayWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_valid.metadata = {'url': '/complex/array/valid'}

    @distributed_trace_async
    async def get_empty(self, cls=None, **kwargs):
        """Get complex types with array property which is empty.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: ArrayWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.ArrayWrapper
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_empty.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        deserialized = self._deserialize('ArrayWrapper', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_empty.metadata = {'url': '/complex/array/empty'}

    @distributed_trace_async
    async def put_empty(self, array=None, cls=None, **kwargs):
        """Put complex types with array property which is empty.

        FIXME: add operation.summary


        :param array: 
        :type array: list[str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)
        complex_body = models.ArrayWrapper(array=array)

        # Construct URL
        url = self.put_empty.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(complex_body, 'ArrayWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_empty.metadata = {'url': '/complex/array/empty'}

    @distributed_trace_async
    async def get_not_provided(self, cls=None, **kwargs):
        """Get complex types with array property while server doesn't provide a response payload.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: ArrayWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.ArrayWrapper
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_not_provided.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        deserialized = self._deserialize('ArrayWrapper', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_not_provided.metadata = {'url': '/complex/array/notprovided'}

