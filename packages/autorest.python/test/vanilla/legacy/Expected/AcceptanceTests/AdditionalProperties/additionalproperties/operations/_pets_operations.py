# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core import PipelineClient
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

from .. import models as _models
from .._configuration import AdditionalPropertiesClientConfiguration
from .._utils.serialization import Deserializer, Serializer

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_create_ap_true_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/true")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_create_cat_ap_true_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/true-subclass")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_create_ap_object_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/type/object")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_create_ap_string_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/type/string")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_create_ap_in_properties_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/in/properties")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_create_ap_in_properties_with_ap_string_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/in/properties/with/additionalProperties/string")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


class PetsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~additionalproperties.AdditionalPropertiesClient`'s
        :attr:`pets` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: AdditionalPropertiesClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def create_ap_true(
        self, create_parameters: _models.PetAPTrue, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPTrue:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPTrue
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_ap_true(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPTrue:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_ap_true(
        self, create_parameters: Union[_models.PetAPTrue, IO[bytes]], **kwargs: Any
    ) -> _models.PetAPTrue:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a PetAPTrue type or a IO[bytes] type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPTrue or IO[bytes]
        :return: PetAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
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
        cls: ClsType[_models.PetAPTrue] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPTrue")

        _request = build_create_ap_true_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPTrue", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_cat_ap_true(
        self, create_parameters: _models.CatAPTrue, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CatAPTrue:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.CatAPTrue
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CatAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_cat_ap_true(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CatAPTrue:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CatAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_cat_ap_true(
        self, create_parameters: Union[_models.CatAPTrue, IO[bytes]], **kwargs: Any
    ) -> _models.CatAPTrue:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Is either a CatAPTrue type or a IO[bytes] type. Required.
        :type create_parameters: ~additionalproperties.models.CatAPTrue or IO[bytes]
        :return: CatAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
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
        cls: ClsType[_models.CatAPTrue] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "CatAPTrue")

        _request = build_create_cat_ap_true_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("CatAPTrue", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_ap_object(
        self, create_parameters: _models.PetAPObject, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPObject:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPObject
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPObject or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_ap_object(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPObject:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPObject or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_ap_object(
        self, create_parameters: Union[_models.PetAPObject, IO[bytes]], **kwargs: Any
    ) -> _models.PetAPObject:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a PetAPObject type or a IO[bytes] type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPObject or IO[bytes]
        :return: PetAPObject or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
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
        cls: ClsType[_models.PetAPObject] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPObject")

        _request = build_create_ap_object_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPObject", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_ap_string(
        self, create_parameters: _models.PetAPString, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPString
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_ap_string(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_ap_string(
        self, create_parameters: Union[_models.PetAPString, IO[bytes]], **kwargs: Any
    ) -> _models.PetAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a PetAPString type or a IO[bytes] type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPString or IO[bytes]
        :return: PetAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
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
        cls: ClsType[_models.PetAPString] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPString")

        _request = build_create_ap_string_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPString", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_ap_in_properties(
        self, create_parameters: _models.PetAPInProperties, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPInProperties:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPInProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPInProperties or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_ap_in_properties(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPInProperties:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPInProperties or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_ap_in_properties(
        self, create_parameters: Union[_models.PetAPInProperties, IO[bytes]], **kwargs: Any
    ) -> _models.PetAPInProperties:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a PetAPInProperties type or a IO[bytes] type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPInProperties or IO[bytes]
        :return: PetAPInProperties or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
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
        cls: ClsType[_models.PetAPInProperties] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPInProperties")

        _request = build_create_ap_in_properties_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPInProperties", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_ap_in_properties_with_ap_string(
        self,
        create_parameters: _models.PetAPInPropertiesWithAPString,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PetAPInPropertiesWithAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPInPropertiesWithAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_ap_in_properties_with_ap_string(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPInPropertiesWithAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPInPropertiesWithAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_ap_in_properties_with_ap_string(
        self, create_parameters: Union[_models.PetAPInPropertiesWithAPString, IO[bytes]], **kwargs: Any
    ) -> _models.PetAPInPropertiesWithAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a PetAPInPropertiesWithAPString type or a IO[bytes] type.
         Required.
        :type create_parameters: ~additionalproperties.models.PetAPInPropertiesWithAPString or
         IO[bytes]
        :return: PetAPInPropertiesWithAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
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
        cls: ClsType[_models.PetAPInPropertiesWithAPString] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPInPropertiesWithAPString")

        _request = build_create_ap_in_properties_with_ap_string_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPInPropertiesWithAPString", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
