# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core import AsyncPipelineClient
from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._utils.serialization import Deserializer, Serializer
from ...operations._operation_group_one_operations import (
    build_test_operation_group_paging_request,
    build_test_two_request,
)
from .._configuration import MultiapiServiceClientConfiguration

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class OperationGroupOneOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.multiapi.sample.v3.aio.MultiapiServiceClient`'s
        :attr:`operation_group_one` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: MultiapiServiceClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def test_operation_group_paging(self, **kwargs: Any) -> AsyncIterable["_models.ModelThree"]:
        """Returns ModelThree with optionalProperty 'paged'.

        :return: An iterator like instance of either ModelThree or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.multiapi.sample.v3.models.ModelThree]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.PagingResult] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_test_operation_group_paging_request(
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PagingResult", pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @overload
    async def test_two(
        self,
        parameter_one: Optional[_models.ModelThree] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ModelThree:
        """TestTwo should be in OperationGroupOneOperations. Takes in ModelThree and ouputs ModelThree.

        :param parameter_one: A ModelThree parameter. Default value is None.
        :type parameter_one: ~azure.multiapi.sample.v3.models.ModelThree
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ModelThree or the result of cls(response)
        :rtype: ~azure.multiapi.sample.v3.models.ModelThree
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def test_two(
        self, parameter_one: Optional[IO[bytes]] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ModelThree:
        """TestTwo should be in OperationGroupOneOperations. Takes in ModelThree and ouputs ModelThree.

        :param parameter_one: A ModelThree parameter. Default value is None.
        :type parameter_one: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ModelThree or the result of cls(response)
        :rtype: ~azure.multiapi.sample.v3.models.ModelThree
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def test_two(
        self, parameter_one: Optional[Union[_models.ModelThree, IO[bytes]]] = None, **kwargs: Any
    ) -> _models.ModelThree:
        """TestTwo should be in OperationGroupOneOperations. Takes in ModelThree and ouputs ModelThree.

        :param parameter_one: A ModelThree parameter. Is either a ModelThree type or a IO[bytes] type.
         Default value is None.
        :type parameter_one: ~azure.multiapi.sample.v3.models.ModelThree or IO[bytes]
        :return: ModelThree or the result of cls(response)
        :rtype: ~azure.multiapi.sample.v3.models.ModelThree
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "3.0.0"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ModelThree] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameter_one, (IOBase, bytes)):
            _content = parameter_one
        else:
            if parameter_one is not None:
                _json = self._serialize.body(parameter_one, "ModelThree")
            else:
                _json = None

        _request = build_test_two_request(
            api_version=api_version,
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
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ModelThree", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
