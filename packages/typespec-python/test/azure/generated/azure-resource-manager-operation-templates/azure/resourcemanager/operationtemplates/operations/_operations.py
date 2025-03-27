# pylint: disable=line-too-long,useless-suppression,too-many-lines
# coding=utf-8
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Iterable, Iterator, List, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core import PipelineClient
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
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from .._configuration import OperationTemplatesClientConfiguration
from .._model_base import SdkJSONEncoder, _deserialize, _failsafe_deserialize
from .._serialization import Deserializer, Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_operations_list_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/providers/Azure.ResourceManager.OperationTemplates/operations"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_check_name_availability_check_global_request(  # pylint: disable=name-too-long
    subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/subscriptions/{subscriptionId}/providers/Azure.ResourceManager.OperationTemplates/checkNameAvailability"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_check_name_availability_check_local_request(  # pylint: disable=name-too-long
    location: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/subscriptions/{subscriptionId}/providers/Azure.ResourceManager.OperationTemplates/locations/{location}/checkNameAvailability"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "location": _SERIALIZER.url("location", location, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_lro_create_or_replace_request(
    resource_group_name: str, order_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Azure.ResourceManager.OperationTemplates/orders/{orderName}"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "orderName": _SERIALIZER.url("order_name", order_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_lro_export_request(
    resource_group_name: str, order_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Azure.ResourceManager.OperationTemplates/orders/{orderName}/export"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "orderName": _SERIALIZER.url("order_name", order_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_lro_delete_request(
    resource_group_name: str, order_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Azure.ResourceManager.OperationTemplates/orders/{orderName}"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "orderName": _SERIALIZER.url("order_name", order_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


class Operations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.resourcemanager.operationtemplates.OperationTemplatesClient`'s
        :attr:`operations` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: OperationTemplatesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(self, **kwargs: Any) -> Iterable["_models.Operation"]:
        """List the operations for the provider.

        :return: An iterator like instance of Operation
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.resourcemanager.operationtemplates.models.Operation]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.Operation]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_operations_list_request(
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.Operation], deserialized.get("value", []))
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = _failsafe_deserialize(_models.ErrorResponse, response.json())
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)


class CheckNameAvailabilityOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.resourcemanager.operationtemplates.OperationTemplatesClient`'s
        :attr:`check_name_availability` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: OperationTemplatesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def check_global(
        self, body: _models.CheckNameAvailabilityRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CheckNameAvailabilityResponse:
        """Implements global CheckNameAvailability operations.

        :param body: The CheckAvailability request. Required.
        :type body: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CheckNameAvailabilityResponse. The CheckNameAvailabilityResponse is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def check_global(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CheckNameAvailabilityResponse:
        """Implements global CheckNameAvailability operations.

        :param body: The CheckAvailability request. Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CheckNameAvailabilityResponse. The CheckNameAvailabilityResponse is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def check_global(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CheckNameAvailabilityResponse:
        """Implements global CheckNameAvailability operations.

        :param body: The CheckAvailability request. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CheckNameAvailabilityResponse. The CheckNameAvailabilityResponse is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def check_global(
        self, body: Union[_models.CheckNameAvailabilityRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.CheckNameAvailabilityResponse:
        """Implements global CheckNameAvailability operations.

        :param body: The CheckAvailability request. Is one of the following types:
         CheckNameAvailabilityRequest, JSON, IO[bytes] Required.
        :type body: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityRequest or
         JSON or IO[bytes]
        :return: CheckNameAvailabilityResponse. The CheckNameAvailabilityResponse is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityResponse
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
        cls: ClsType[_models.CheckNameAvailabilityResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_check_name_availability_check_global_request(
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.CheckNameAvailabilityResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def check_local(
        self,
        location: str,
        body: _models.CheckNameAvailabilityRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckNameAvailabilityResponse:
        """Implements local CheckNameAvailability operations.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param body: The CheckAvailability request. Required.
        :type body: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CheckNameAvailabilityResponse. The CheckNameAvailabilityResponse is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def check_local(
        self, location: str, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CheckNameAvailabilityResponse:
        """Implements local CheckNameAvailability operations.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param body: The CheckAvailability request. Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CheckNameAvailabilityResponse. The CheckNameAvailabilityResponse is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def check_local(
        self, location: str, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CheckNameAvailabilityResponse:
        """Implements local CheckNameAvailability operations.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param body: The CheckAvailability request. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CheckNameAvailabilityResponse. The CheckNameAvailabilityResponse is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def check_local(
        self, location: str, body: Union[_models.CheckNameAvailabilityRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.CheckNameAvailabilityResponse:
        """Implements local CheckNameAvailability operations.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param body: The CheckAvailability request. Is one of the following types:
         CheckNameAvailabilityRequest, JSON, IO[bytes] Required.
        :type body: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityRequest or
         JSON or IO[bytes]
        :return: CheckNameAvailabilityResponse. The CheckNameAvailabilityResponse is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityResponse
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
        cls: ClsType[_models.CheckNameAvailabilityResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_check_name_availability_check_local_request(
            location=location,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.CheckNameAvailabilityResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class LroOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.resourcemanager.operationtemplates.OperationTemplatesClient`'s
        :attr:`lro` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: OperationTemplatesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def _create_or_replace_initial(
        self, resource_group_name: str, order_name: str, resource: Union[_models.Order, JSON, IO[bytes]], **kwargs: Any
    ) -> Iterator[bytes]:
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
        cls: ClsType[Iterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_lro_create_or_replace_request(
            resource_group_name=resource_group_name,
            order_name=order_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            try:
                response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 201:
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    def begin_create_or_replace(
        self,
        resource_group_name: str,
        order_name: str,
        resource: _models.Order,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.Order]:
        """Create a Order.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param order_name: The name of the Order. Required.
        :type order_name: str
        :param resource: Resource create parameters. Required.
        :type resource: ~azure.resourcemanager.operationtemplates.models.Order
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Order. The Order is compatible with
         MutableMapping
        :rtype: ~azure.core.polling.LROPoller[~azure.resourcemanager.operationtemplates.models.Order]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_create_or_replace(
        self,
        resource_group_name: str,
        order_name: str,
        resource: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.Order]:
        """Create a Order.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param order_name: The name of the Order. Required.
        :type order_name: str
        :param resource: Resource create parameters. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Order. The Order is compatible with
         MutableMapping
        :rtype: ~azure.core.polling.LROPoller[~azure.resourcemanager.operationtemplates.models.Order]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_create_or_replace(
        self,
        resource_group_name: str,
        order_name: str,
        resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.Order]:
        """Create a Order.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param order_name: The name of the Order. Required.
        :type order_name: str
        :param resource: Resource create parameters. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Order. The Order is compatible with
         MutableMapping
        :rtype: ~azure.core.polling.LROPoller[~azure.resourcemanager.operationtemplates.models.Order]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def begin_create_or_replace(
        self, resource_group_name: str, order_name: str, resource: Union[_models.Order, JSON, IO[bytes]], **kwargs: Any
    ) -> LROPoller[_models.Order]:
        """Create a Order.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param order_name: The name of the Order. Required.
        :type order_name: str
        :param resource: Resource create parameters. Is one of the following types: Order, JSON,
         IO[bytes] Required.
        :type resource: ~azure.resourcemanager.operationtemplates.models.Order or JSON or IO[bytes]
        :return: An instance of LROPoller that returns Order. The Order is compatible with
         MutableMapping
        :rtype: ~azure.core.polling.LROPoller[~azure.resourcemanager.operationtemplates.models.Order]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Order] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._create_or_replace_initial(
                resource_group_name=resource_group_name,
                order_name=order_name,
                resource=resource,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = _deserialize(_models.Order, response.json())
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, ARMPolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[_models.Order].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[_models.Order](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    def _export_initial(
        self,
        resource_group_name: str,
        order_name: str,
        body: Union[_models.ExportRequest, JSON, IO[bytes]],
        **kwargs: Any
    ) -> Iterator[bytes]:
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
        cls: ClsType[Iterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_lro_export_request(
            resource_group_name=resource_group_name,
            order_name=order_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            try:
                response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    def begin_export(
        self,
        resource_group_name: str,
        order_name: str,
        body: _models.ExportRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[None]:
        """A long-running resource action.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param order_name: The name of the Order. Required.
        :type order_name: str
        :param body: The content of the action request. Required.
        :type body: ~azure.resourcemanager.operationtemplates.models.ExportRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_export(
        self,
        resource_group_name: str,
        order_name: str,
        body: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[None]:
        """A long-running resource action.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param order_name: The name of the Order. Required.
        :type order_name: str
        :param body: The content of the action request. Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_export(
        self,
        resource_group_name: str,
        order_name: str,
        body: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[None]:
        """A long-running resource action.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param order_name: The name of the Order. Required.
        :type order_name: str
        :param body: The content of the action request. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def begin_export(
        self,
        resource_group_name: str,
        order_name: str,
        body: Union[_models.ExportRequest, JSON, IO[bytes]],
        **kwargs: Any
    ) -> LROPoller[None]:
        """A long-running resource action.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param order_name: The name of the Order. Required.
        :type order_name: str
        :param body: The content of the action request. Is one of the following types: ExportRequest,
         JSON, IO[bytes] Required.
        :type body: ~azure.resourcemanager.operationtemplates.models.ExportRequest or JSON or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._export_initial(
                resource_group_name=resource_group_name,
                order_name=order_name,
                body=body,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, ARMPolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    def _delete_initial(self, resource_group_name: str, order_name: str, **kwargs: Any) -> Iterator[bytes]:
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Iterator[bytes]] = kwargs.pop("cls", None)

        _request = build_lro_delete_request(
            resource_group_name=resource_group_name,
            order_name=order_name,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            try:
                response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def begin_delete(self, resource_group_name: str, order_name: str, **kwargs: Any) -> LROPoller[None]:
        """Delete a Order.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param order_name: The name of the Order. Required.
        :type order_name: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._delete_initial(
                resource_group_name=resource_group_name,
                order_name=order_name,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, ARMPolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore
