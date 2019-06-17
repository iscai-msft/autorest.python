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

from azure.core.exceptions import map_error

from ... import models


class FormdataOperations:
    """FormdataOperations async operations.

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

    async def upload_file(self, file_content, file_name, *, cls=None, **kwargs):
        """Upload file.

        :param file_content: File to upload.
        :type file_content: Generator
        :param file_name: File name to upload. Name has to be spelled exactly
         as written here.
        :type file_name: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: object or the result of cls(response)
        :rtype: Generator
        :raises: :class:`ErrorException<bodyformdata.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.upload_file.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'multipart/form-data'

        # Construct form data
        form_data_content = {
            'fileContent': file_content,
            'fileName': file_name,
        }

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, form_content=form_data_content)
        pipeline_response = await self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            await response.load_body()
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    upload_file.metadata = {'url': '/formdata/stream/uploadfile'}

    async def upload_file_via_body(self, file_content, *, cls=None, **kwargs):
        """Upload file.

        :param file_content: File to upload.
        :type file_content: Generator
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: object or the result of cls(response)
        :rtype: Generator
        :raises: :class:`ErrorException<bodyformdata.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.upload_file_via_body.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/octet-stream'

        # Construct body

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, stream_content=file_content)
        pipeline_response = await self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            await response.load_body()
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    upload_file_via_body.metadata = {'url': '/formdata/stream/uploadfile'}
