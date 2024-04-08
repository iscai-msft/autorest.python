# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._polymorphicrecursive_operations import build_get_valid_request, build_put_valid_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PolymorphicrecursiveOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodycomplex.aio.AutoRestComplexTestService`'s
        :attr:`polymorphicrecursive` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_valid(self, **kwargs: Any) -> _models.Fish:
        """Get complex types that are polymorphic and have recursive references.

        :return: Fish or the result of cls(response)
        :rtype: ~bodycomplex.models.Fish
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Fish] = kwargs.pop("cls", None)

        _request = build_get_valid_request(
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Fish", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: _models.Fish, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic and have recursive references.

        :param complex_body: Please put a salmon that looks like this:
         {
             "fishtype": "salmon",
             "species": "king",
             "length": 1,
             "age": 1,
             "location": "alaska",
             "iswild": true,
             "siblings": [
                 {
                     "fishtype": "shark",
                     "species": "predator",
                     "length": 20,
                     "age": 6,
                     "siblings": [
                         {
                             "fishtype": "salmon",
                             "species": "coho",
                             "length": 2,
                             "age": 2,
                             "location": "atlantic",
                             "iswild": true,
                             "siblings": [
                                 {
                                     "fishtype": "shark",
                                     "species": "predator",
                                     "length": 20,
                                     "age": 6
                                 },
                                 {
                                     "fishtype": "sawshark",
                                     "species": "dangerous",
                                     "length": 10,
                                     "age": 105
                                 }
                             ]
                         },
                         {
                             "fishtype": "sawshark",
                             "species": "dangerous",
                             "length": 10,
                             "age": 105
                         }
                     ]
                 },
                 {
                     "fishtype": "sawshark",
                     "species": "dangerous",
                     "length": 10,
                     "age": 105
                 }
             ]
         }. Required.
        :type complex_body: ~bodycomplex.models.Fish
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic and have recursive references.

        :param complex_body: Please put a salmon that looks like this:
         {
             "fishtype": "salmon",
             "species": "king",
             "length": 1,
             "age": 1,
             "location": "alaska",
             "iswild": true,
             "siblings": [
                 {
                     "fishtype": "shark",
                     "species": "predator",
                     "length": 20,
                     "age": 6,
                     "siblings": [
                         {
                             "fishtype": "salmon",
                             "species": "coho",
                             "length": 2,
                             "age": 2,
                             "location": "atlantic",
                             "iswild": true,
                             "siblings": [
                                 {
                                     "fishtype": "shark",
                                     "species": "predator",
                                     "length": 20,
                                     "age": 6
                                 },
                                 {
                                     "fishtype": "sawshark",
                                     "species": "dangerous",
                                     "length": 10,
                                     "age": 105
                                 }
                             ]
                         },
                         {
                             "fishtype": "sawshark",
                             "species": "dangerous",
                             "length": 10,
                             "age": 105
                         }
                     ]
                 },
                 {
                     "fishtype": "sawshark",
                     "species": "dangerous",
                     "length": 10,
                     "age": 105
                 }
             ]
         }. Required.
        :type complex_body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: Union[_models.Fish, IO[bytes]], **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic and have recursive references.

        :param complex_body: Please put a salmon that looks like this:
         {
             "fishtype": "salmon",
             "species": "king",
             "length": 1,
             "age": 1,
             "location": "alaska",
             "iswild": true,
             "siblings": [
                 {
                     "fishtype": "shark",
                     "species": "predator",
                     "length": 20,
                     "age": 6,
                     "siblings": [
                         {
                             "fishtype": "salmon",
                             "species": "coho",
                             "length": 2,
                             "age": 2,
                             "location": "atlantic",
                             "iswild": true,
                             "siblings": [
                                 {
                                     "fishtype": "shark",
                                     "species": "predator",
                                     "length": 20,
                                     "age": 6
                                 },
                                 {
                                     "fishtype": "sawshark",
                                     "species": "dangerous",
                                     "length": 10,
                                     "age": 105
                                 }
                             ]
                         },
                         {
                             "fishtype": "sawshark",
                             "species": "dangerous",
                             "length": 10,
                             "age": 105
                         }
                     ]
                 },
                 {
                     "fishtype": "sawshark",
                     "species": "dangerous",
                     "length": 10,
                     "age": 105
                 }
             ]
         }. Is either a Fish type or a IO[bytes] type. Required.
        :type complex_body: ~bodycomplex.models.Fish or IO[bytes]
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(complex_body, (IOBase, bytes)):
            _content = complex_body
        else:
            _json = self._serialize.body(complex_body, "Fish")

        _request = build_put_valid_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
