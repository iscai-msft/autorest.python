# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ..._operations._operations import (
    build_usage_input_and_output_request,
    build_usage_input_request,
    build_usage_output_request,
)
from .._vendor import UsageClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class UsageClientOperationsMixin(UsageClientMixinABC):

    @overload
    async def input(self, input: _models.InputRecord, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """input.

        :param input: Required.
        :type input: ~typetest.model.usage.models.InputRecord
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def input(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """input.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def input(self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> None:
        """input.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def input(self, input: Union[_models.InputRecord, JSON, IO[bytes]], **kwargs: Any) -> None:
        """input.

        :param input: Is one of the following types: InputRecord, JSON, IO[bytes] Required.
        :type input: ~typetest.model.usage.models.InputRecord or JSON or IO[bytes]
        :return: None
        :rtype: None
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
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_usage_input_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def output(self, **kwargs: Any) -> _models.OutputRecord:
        """output.

        :return: OutputRecord. The OutputRecord is compatible with MutableMapping
        :rtype: ~typetest.model.usage.models.OutputRecord
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.OutputRecord] = kwargs.pop("cls", None)

        _request = build_usage_output_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.OutputRecord, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def input_and_output(
        self, body: _models.InputOutputRecord, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.InputOutputRecord:
        """input_and_output.

        :param body: Required.
        :type body: ~typetest.model.usage.models.InputOutputRecord
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: InputOutputRecord. The InputOutputRecord is compatible with MutableMapping
        :rtype: ~typetest.model.usage.models.InputOutputRecord
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def input_and_output(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.InputOutputRecord:
        """input_and_output.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: InputOutputRecord. The InputOutputRecord is compatible with MutableMapping
        :rtype: ~typetest.model.usage.models.InputOutputRecord
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def input_and_output(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.InputOutputRecord:
        """input_and_output.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: InputOutputRecord. The InputOutputRecord is compatible with MutableMapping
        :rtype: ~typetest.model.usage.models.InputOutputRecord
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def input_and_output(
        self, body: Union[_models.InputOutputRecord, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.InputOutputRecord:
        """input_and_output.

        :param body: Is one of the following types: InputOutputRecord, JSON, IO[bytes] Required.
        :type body: ~typetest.model.usage.models.InputOutputRecord or JSON or IO[bytes]
        :return: InputOutputRecord. The InputOutputRecord is compatible with MutableMapping
        :rtype: ~typetest.model.usage.models.InputOutputRecord
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
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.InputOutputRecord] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_usage_input_and_output_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.InputOutputRecord, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
