# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core import AsyncPipelineClient
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ..._serialization import Deserializer, Serializer
from ...operations._operations import (
    build_pets_create_ap_in_properties_request,
    build_pets_create_ap_in_properties_with_ap_string_request,
    build_pets_create_ap_object_request,
    build_pets_create_ap_string_request,
    build_pets_create_ap_true_request,
    build_pets_create_cat_ap_true_request,
)
from .._configuration import AdditionalPropertiesClientConfiguration

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~additionalpropertiesversiontolerant.aio.AdditionalPropertiesClient`'s
        :attr:`pets` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: AdditionalPropertiesClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_ap_true(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """

    @overload
    async def create_ap_true(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """

    @distributed_trace_async
    async def create_ap_true(self, create_parameters: Union[JSON, IO[bytes]], **kwargs: Any) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a JSON type or a IO[bytes] type. Required.
        :type create_parameters: JSON or IO[bytes]
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        _request = build_pets_create_ap_true_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore

    @overload
    async def create_cat_ap_true(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,
                    "friendly": bool,
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "friendly": bool,
                    "name": "str",
                    "status": bool
                }
        """

    @overload
    async def create_cat_ap_true(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "friendly": bool,
                    "name": "str",
                    "status": bool
                }
        """

    @distributed_trace_async
    async def create_cat_ap_true(self, create_parameters: Union[JSON, IO[bytes]], **kwargs: Any) -> JSON:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Is either a JSON type or a IO[bytes] type. Required.
        :type create_parameters: JSON or IO[bytes]
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,
                    "friendly": bool,
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "friendly": bool,
                    "name": "str",
                    "status": bool
                }
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        _request = build_pets_create_cat_ap_true_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore

    @overload
    async def create_ap_object(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """

    @overload
    async def create_ap_object(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """

    @distributed_trace_async
    async def create_ap_object(self, create_parameters: Union[JSON, IO[bytes]], **kwargs: Any) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a JSON type or a IO[bytes] type. Required.
        :type create_parameters: JSON or IO[bytes]
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        _request = build_pets_create_ap_object_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore

    @overload
    async def create_ap_string(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """

    @overload
    async def create_ap_string(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """

    @distributed_trace_async
    async def create_ap_string(self, create_parameters: Union[JSON, IO[bytes]], **kwargs: Any) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a JSON type or a IO[bytes] type. Required.
        :type create_parameters: JSON or IO[bytes]
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        _request = build_pets_create_ap_string_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore

    @overload
    async def create_ap_in_properties(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """

    @overload
    async def create_ap_in_properties(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """

    @distributed_trace_async
    async def create_ap_in_properties(self, create_parameters: Union[JSON, IO[bytes]], **kwargs: Any) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a JSON type or a IO[bytes] type. Required.
        :type create_parameters: JSON or IO[bytes]
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "id": 0,
                    "name": "str",
                    "status": bool
                }
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        _request = build_pets_create_ap_in_properties_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore

    @overload
    async def create_ap_in_properties_with_ap_string(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "@odata.location": "str",
                    "id": 0,
                    "additionalProperties": {
                        "str": 0.0
                    },
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "@odata.location": "str",
                    "id": 0,
                    "additionalProperties": {
                        "str": 0.0
                    },
                    "name": "str",
                    "status": bool
                }
        """

    @overload
    async def create_ap_in_properties_with_ap_string(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "@odata.location": "str",
                    "id": 0,
                    "additionalProperties": {
                        "str": 0.0
                    },
                    "name": "str",
                    "status": bool
                }
        """

    @distributed_trace_async
    async def create_ap_in_properties_with_ap_string(
        self, create_parameters: Union[JSON, IO[bytes]], **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a JSON type or a IO[bytes] type. Required.
        :type create_parameters: JSON or IO[bytes]
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "@odata.location": "str",
                    "id": 0,
                    "additionalProperties": {
                        "str": 0.0
                    },
                    "name": "str",
                    "status": bool
                }

                # response body for status code(s): 200
                response == {
                    "@odata.location": "str",
                    "id": 0,
                    "additionalProperties": {
                        "str": 0.0
                    },
                    "name": "str",
                    "status": bool
                }
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        _request = build_pets_create_ap_in_properties_with_ap_string_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore
