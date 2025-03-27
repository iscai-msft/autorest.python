# coding=utf-8
import sys
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer
from .._validation import api_version_validation
from .._vendor import ResiliencyServiceDrivenClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_resiliency_service_driven_add_operation_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    # Construct URL
    _url = "/add-operation"

    return HttpRequest(method="DELETE", url=_url, **kwargs)


def build_resiliency_service_driven_from_none_request(  # pylint: disable=name-too-long
    *, new_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/add-optional-param/from-none"

    # Construct parameters
    if new_parameter is not None:
        _params["new-parameter"] = _SERIALIZER.query("new_parameter", new_parameter, "str")

    return HttpRequest(method="HEAD", url=_url, params=_params, **kwargs)


def build_resiliency_service_driven_from_one_required_request(  # pylint: disable=name-too-long
    *, parameter: str, new_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/add-optional-param/from-one-required"

    # Construct parameters
    _params["parameter"] = _SERIALIZER.query("parameter", parameter, "str")
    if new_parameter is not None:
        _params["new-parameter"] = _SERIALIZER.query("new_parameter", new_parameter, "str")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_resiliency_service_driven_from_one_optional_request(  # pylint: disable=name-too-long
    *, parameter: Optional[str] = None, new_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/add-optional-param/from-one-optional"

    # Construct parameters
    if parameter is not None:
        _params["parameter"] = _SERIALIZER.query("parameter", parameter, "str")
    if new_parameter is not None:
        _params["new-parameter"] = _SERIALIZER.query("new_parameter", new_parameter, "str")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


class ResiliencyServiceDrivenClientOperationsMixin(  # pylint: disable=name-too-long
    ResiliencyServiceDrivenClientMixinABC
):

    @distributed_trace
    @api_version_validation(
        method_added_on="v2",
    )
    def add_operation(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Added operation.

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

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_resiliency_service_driven_add_operation_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "serviceDeploymentVersion": self._serialize.url(
                "self._config.service_deployment_version",
                self._config.service_deployment_version,
                "str",
                skip_quote=True,
            ),
            "apiVersion": self._serialize.url(
                "self._config.api_version", self._config.api_version, "str", skip_quote=True
            ),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    @api_version_validation(
        params_added_on={"v2": ["new_parameter"]},
    )
    def from_none(self, *, new_parameter: Optional[str] = None, **kwargs: Any) -> bool:
        """Test that grew up from accepting no parameters to an optional input parameter.

        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
        :return: bool
        :rtype: bool
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

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_resiliency_service_driven_from_none_request(
            new_parameter=new_parameter,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "serviceDeploymentVersion": self._serialize.url(
                "self._config.service_deployment_version",
                self._config.service_deployment_version,
                "str",
                skip_quote=True,
            ),
            "apiVersion": self._serialize.url(
                "self._config.api_version", self._config.api_version, "str", skip_quote=True
            ),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
        return 200 <= response.status_code <= 299

    @distributed_trace
    @api_version_validation(
        params_added_on={"v2": ["new_parameter"]},
    )
    def from_one_required(  # pylint: disable=inconsistent-return-statements
        self, *, parameter: str, new_parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Operation that grew up from accepting one required parameter to accepting a required parameter
        and an optional parameter.

        :keyword parameter: I am a required parameter. Required.
        :paramtype parameter: str
        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
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

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_resiliency_service_driven_from_one_required_request(
            parameter=parameter,
            new_parameter=new_parameter,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "serviceDeploymentVersion": self._serialize.url(
                "self._config.service_deployment_version",
                self._config.service_deployment_version,
                "str",
                skip_quote=True,
            ),
            "apiVersion": self._serialize.url(
                "self._config.api_version", self._config.api_version, "str", skip_quote=True
            ),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    @api_version_validation(
        params_added_on={"v2": ["new_parameter"]},
    )
    def from_one_optional(  # pylint: disable=inconsistent-return-statements
        self, *, parameter: Optional[str] = None, new_parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Tests that we can grow up an operation from accepting one optional parameter to accepting two
        optional parameters.

        :keyword parameter: I am an optional parameter. Default value is None.
        :paramtype parameter: str
        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
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

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_resiliency_service_driven_from_one_optional_request(
            parameter=parameter,
            new_parameter=new_parameter,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "serviceDeploymentVersion": self._serialize.url(
                "self._config.service_deployment_version",
                self._config.service_deployment_version,
                "str",
                skip_quote=True,
            ),
            "apiVersion": self._serialize.url(
                "self._config.api_version", self._config.api_version, "str", skip_quote=True
            ),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
