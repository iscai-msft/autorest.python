# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_post_required_request(
    path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    custom_header = kwargs.pop('custom_header', None)  # type: Optional[str]
    query = kwargs.pop('query', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/parameterGrouping/postRequired/{path}")
    path_format_arguments = {
        "path": _SERIALIZER.url("path", path, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if query is not None:
        _query_parameters['query'] = _SERIALIZER.query("query", query, 'int')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if custom_header is not None:
        _header_parameters['customHeader'] = _SERIALIZER.header("custom_header", custom_header, 'str')
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_post_optional_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    custom_header = kwargs.pop('custom_header', None)  # type: Optional[str]
    query = kwargs.pop('query', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/parameterGrouping/postOptional")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if query is not None:
        _query_parameters['query'] = _SERIALIZER.query("query", query, 'int')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if custom_header is not None:
        _header_parameters['customHeader'] = _SERIALIZER.header("custom_header", custom_header, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_post_reserved_words_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    from_parameter = kwargs.pop('from_parameter', None)  # type: Optional[str]
    accept_parameter = kwargs.pop('accept_parameter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/parameterGrouping/postReservedWords")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if from_parameter is not None:
        _query_parameters['from'] = _SERIALIZER.query("from_parameter", from_parameter, 'str')
    if accept_parameter is not None:
        _query_parameters['accept'] = _SERIALIZER.query("accept_parameter", accept_parameter, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_post_multi_param_groups_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    header_one = kwargs.pop('header_one', None)  # type: Optional[str]
    query_one = kwargs.pop('query_one', 30)  # type: Optional[int]
    header_two = kwargs.pop('header_two', None)  # type: Optional[str]
    query_two = kwargs.pop('query_two', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/parameterGrouping/postMultipleParameterGroups")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if query_one is not None:
        _query_parameters['query-one'] = _SERIALIZER.query("query_one", query_one, 'int')
    if query_two is not None:
        _query_parameters['query-two'] = _SERIALIZER.query("query_two", query_two, 'int')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if header_one is not None:
        _header_parameters['header-one'] = _SERIALIZER.header("header_one", header_one, 'str')
    if header_two is not None:
        _header_parameters['header-two'] = _SERIALIZER.header("header_two", header_two, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_post_shared_parameter_group_object_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    header_one = kwargs.pop('header_one', None)  # type: Optional[str]
    query_one = kwargs.pop('query_one', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/parameterGrouping/sharedParameterGroupObject")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if query_one is not None:
        _query_parameters['query-one'] = _SERIALIZER.query("query_one", query_one, 'int')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if header_one is not None:
        _header_parameters['header-one'] = _SERIALIZER.header("header_one", header_one, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class ParameterGroupingOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azureparametergrouping.AutoRestParameterGroupingTestService`'s
        :attr:`parameter_grouping` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def post_required(  # pylint: disable=inconsistent-return-statements
        self,
        parameter_grouping_post_required_parameters,  # type: _models.ParameterGroupingPostRequiredParameters
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Post a bunch of required parameters grouped.

        :param parameter_grouping_post_required_parameters: Parameter group.
        :type parameter_grouping_post_required_parameters:
         ~azureparametergrouping.models.ParameterGroupingPostRequiredParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _custom_header = None
        _query = None
        _path = None
        _body = None
        if parameter_grouping_post_required_parameters is not None:
            _custom_header = parameter_grouping_post_required_parameters.custom_header
            _query = parameter_grouping_post_required_parameters.query
            _path = parameter_grouping_post_required_parameters.path
            _body = parameter_grouping_post_required_parameters.body
        _json = self._serialize.body(_body, "int")

        request = build_post_required_request(
            path=_path,
            content_type=content_type,
            json=_json,
            custom_header=_custom_header,
            query=_query,
            template_url=self.post_required.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_required.metadata = {"url": "/parameterGrouping/postRequired/{path}"}  # type: ignore

    @distributed_trace
    def post_optional(  # pylint: disable=inconsistent-return-statements
        self,
        parameter_grouping_post_optional_parameters=None,  # type: Optional[_models.ParameterGroupingPostOptionalParameters]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Post a bunch of optional parameters grouped.

        :param parameter_grouping_post_optional_parameters: Parameter group. Default value is None.
        :type parameter_grouping_post_optional_parameters:
         ~azureparametergrouping.models.ParameterGroupingPostOptionalParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _custom_header = None
        _query = None
        if parameter_grouping_post_optional_parameters is not None:
            _custom_header = parameter_grouping_post_optional_parameters.custom_header
            _query = parameter_grouping_post_optional_parameters.query

        request = build_post_optional_request(
            custom_header=_custom_header,
            query=_query,
            template_url=self.post_optional.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_optional.metadata = {"url": "/parameterGrouping/postOptional"}  # type: ignore

    @distributed_trace
    def post_reserved_words(  # pylint: disable=inconsistent-return-statements
        self,
        parameter_grouping_post_reserved_words_parameters=None,  # type: Optional[_models.ParameterGroupingPostReservedWordsParameters]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Post a grouped parameters with reserved words.

        :param parameter_grouping_post_reserved_words_parameters: Parameter group. Default value is
         None.
        :type parameter_grouping_post_reserved_words_parameters:
         ~azureparametergrouping.models.ParameterGroupingPostReservedWordsParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _from_parameter = None
        _accept_parameter = None
        if parameter_grouping_post_reserved_words_parameters is not None:
            _from_parameter = parameter_grouping_post_reserved_words_parameters.from_property
            _accept_parameter = parameter_grouping_post_reserved_words_parameters.accept

        request = build_post_reserved_words_request(
            from_parameter=_from_parameter,
            accept_parameter=_accept_parameter,
            template_url=self.post_reserved_words.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_reserved_words.metadata = {"url": "/parameterGrouping/postReservedWords"}  # type: ignore

    @distributed_trace
    def post_multi_param_groups(  # pylint: disable=inconsistent-return-statements
        self,
        first_parameter_group=None,  # type: Optional[_models.FirstParameterGroup]
        parameter_grouping_post_multi_param_groups_second_param_group=None,  # type: Optional[_models.ParameterGroupingPostMultiParamGroupsSecondParamGroup]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Post parameters from multiple different parameter groups.

        :param first_parameter_group: Parameter group. Default value is None.
        :type first_parameter_group: ~azureparametergrouping.models.FirstParameterGroup
        :param parameter_grouping_post_multi_param_groups_second_param_group: Parameter group. Default
         value is None.
        :type parameter_grouping_post_multi_param_groups_second_param_group:
         ~azureparametergrouping.models.ParameterGroupingPostMultiParamGroupsSecondParamGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _header_one = None
        _query_one = None
        _header_two = None
        _query_two = None
        if first_parameter_group is not None:
            _header_one = first_parameter_group.header_one
            _query_one = first_parameter_group.query_one
        if parameter_grouping_post_multi_param_groups_second_param_group is not None:
            _header_two = parameter_grouping_post_multi_param_groups_second_param_group.header_two
            _query_two = parameter_grouping_post_multi_param_groups_second_param_group.query_two

        request = build_post_multi_param_groups_request(
            header_one=_header_one,
            query_one=_query_one,
            header_two=_header_two,
            query_two=_query_two,
            template_url=self.post_multi_param_groups.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_multi_param_groups.metadata = {"url": "/parameterGrouping/postMultipleParameterGroups"}  # type: ignore

    @distributed_trace
    def post_shared_parameter_group_object(  # pylint: disable=inconsistent-return-statements
        self,
        first_parameter_group=None,  # type: Optional[_models.FirstParameterGroup]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Post parameters with a shared parameter group object.

        :param first_parameter_group: Parameter group. Default value is None.
        :type first_parameter_group: ~azureparametergrouping.models.FirstParameterGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _header_one = None
        _query_one = None
        if first_parameter_group is not None:
            _header_one = first_parameter_group.header_one
            _query_one = first_parameter_group.query_one

        request = build_post_shared_parameter_group_object_request(
            header_one=_header_one,
            query_one=_query_one,
            template_url=self.post_shared_parameter_group_object.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_shared_parameter_group_object.metadata = {"url": "/parameterGrouping/sharedParameterGroupObject"}  # type: ignore
