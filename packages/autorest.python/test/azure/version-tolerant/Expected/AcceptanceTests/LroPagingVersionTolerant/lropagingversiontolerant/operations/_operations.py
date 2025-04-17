# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from io import IOBase
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
from azure.core.polling.base_polling import LROBasePolling
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._configuration import LroPagingClientConfiguration
from .._utils.serialization import Deserializer, Serializer

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_question_answering_projects_get_qnas_request(  # pylint: disable=name-too-long
    project_name: str,
    *,
    source: Optional[str] = None,
    top: Optional[int] = None,
    skip: Optional[int] = None,
    maxpagesize: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/query-knowledgebases/projects/{projectName}/qnas"
    path_format_arguments = {
        "projectName": _SERIALIZER.url("project_name", project_name, "str", max_length=100),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if source is not None:
        _params["source"] = _SERIALIZER.query("source", source, "str")
    if top is not None:
        _params["top"] = _SERIALIZER.query("top", top, "int")
    if skip is not None:
        _params["skip"] = _SERIALIZER.query("skip", skip, "int")
    if maxpagesize is not None:
        _params["maxpagesize"] = _SERIALIZER.query("maxpagesize", maxpagesize, "int")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_question_answering_projects_update_qnas_request(  # pylint: disable=name-too-long
    project_name: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/query-knowledgebases/projects/{projectName}/qnas"
    path_format_arguments = {
        "projectName": _SERIALIZER.url("project_name", project_name, "str", max_length=100),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


class QuestionAnsweringProjectsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~lropagingversiontolerant.LroPagingClient`'s
        :attr:`question_answering_projects` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: LroPagingClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_qnas(
        self,
        project_name: str,
        *,
        source: Optional[str] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable[JSON]:
        """Gets all the QnAs of a project.

        Gets all the QnAs of a project.

        :param project_name: The name of the project to use. Required.
        :type project_name: str
        :keyword source: Source of the QnA. Default value is None.
        :paramtype source: str
        :keyword top: The maximum number of resources to return from the collection. Default value is
         None.
        :paramtype top: int
        :keyword skip: An offset into the collection of the first resource to be returned. Default
         value is None.
        :paramtype skip: int
        :return: An iterator like instance of JSON object
        :rtype: ~azure.core.paging.ItemPaged[JSON]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "activeLearningSuggestions": [
                        {
                            "clusterHead": "str",
                            "suggestedQuestions": [
                                {
                                    "autoSuggestedCount": 0,
                                    "question": "str",
                                    "userSuggestedCount": 0
                                }
                            ]
                        }
                    ],
                    "answer": "str",
                    "dialog": {
                        "isContextOnly": bool,
                        "prompts": [
                            {
                                "displayOrder": 0,
                                "displayText": "str",
                                "qna": {
                                    "activeLearningSuggestions": [
                                        {
                                            "clusterHead": "str",
                                            "suggestedQuestions": [
                                                {
                "autoSuggestedCount": 0,
                                                    "question":
                                                      "str",
                "userSuggestedCount": 0
                                                }
                                            ]
                                        }
                                    ],
                                    "answer": "str",
                                    "dialog": ...,
                                    "id": 0,
                                    "metadata": {
                                        "str": "str"
                                    },
                                    "questions": [
                                        "str"
                                    ],
                                    "source": "str"
                                },
                                "qnaId": 0
                            }
                        ]
                    },
                    "id": 0,
                    "lastUpdatedDateTime": "2020-02-20 00:00:00",
                    "metadata": {
                        "str": "str"
                    },
                    "questions": [
                        "str"
                    ],
                    "source": "str"
                }
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        maxpagesize = kwargs.pop("maxpagesize", None)
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_question_answering_projects_get_qnas_request(
                    project_name=project_name,
                    source=source,
                    top=top,
                    skip=skip,
                    maxpagesize=maxpagesize,
                    api_version=self._config.api_version,
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
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = deserialized.get("value", [])
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
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    def _update_qnas_initial(
        self, project_name: str, body: Union[List[JSON], IO[bytes]], **kwargs: Any
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
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _json = body

        _request = build_question_answering_projects_update_qnas_request(
            project_name=project_name,
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

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
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Operation-Location"] = self._deserialize(
                "str", response.headers.get("Operation-Location")
            )

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(Iterator[bytes], deserialized), response_headers)  # type: ignore

        return cast(Iterator[bytes], deserialized)  # type: ignore

    @overload
    def begin_update_qnas(
        self, project_name: str, body: List[JSON], *, content_type: str = "application/json", **kwargs: Any
    ) -> LROPoller[Iterable[JSON]]:
        """Updates the QnAs of a project.

        Updates the QnAs of a project.

        :param project_name: The name of the project to use. Required.
        :type project_name: str
        :param body: Update QnAs parameters of a project. Required.
        :type body: list[JSON]
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns an iterator like instance of JSON object
        :rtype: ~azure.core.polling.LROPoller[~azure.core.paging.ItemPaged[JSON]]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = [
                    {
                        "op": "str",
                        "value": {
                            "activeLearningSuggestions": [
                                {
                                    "clusterHead": "str",
                                    "suggestedQuestions": [
                                        {
                                            "autoSuggestedCount": 0,
                                            "question": "str",
                                            "userSuggestedCount": 0
                                        }
                                    ]
                                }
                            ],
                            "answer": "str",
                            "dialog": {
                                "isContextOnly": bool,
                                "prompts": [
                                    {
                                        "displayOrder": 0,
                                        "displayText": "str",
                                        "qna": ...,
                                        "qnaId": 0
                                    }
                                ]
                            },
                            "id": 0,
                            "metadata": {
                                "str": "str"
                            },
                            "questions": [
                                "str"
                            ],
                            "source": "str"
                        }
                    }
                ]

                # response body for status code(s): 200, 202
                response == {
                    "activeLearningSuggestions": [
                        {
                            "clusterHead": "str",
                            "suggestedQuestions": [
                                {
                                    "autoSuggestedCount": 0,
                                    "question": "str",
                                    "userSuggestedCount": 0
                                }
                            ]
                        }
                    ],
                    "answer": "str",
                    "dialog": {
                        "isContextOnly": bool,
                        "prompts": [
                            {
                                "displayOrder": 0,
                                "displayText": "str",
                                "qna": {
                                    "activeLearningSuggestions": [
                                        {
                                            "clusterHead": "str",
                                            "suggestedQuestions": [
                                                {
                "autoSuggestedCount": 0,
                                                    "question":
                                                      "str",
                "userSuggestedCount": 0
                                                }
                                            ]
                                        }
                                    ],
                                    "answer": "str",
                                    "dialog": ...,
                                    "id": 0,
                                    "metadata": {
                                        "str": "str"
                                    },
                                    "questions": [
                                        "str"
                                    ],
                                    "source": "str"
                                },
                                "qnaId": 0
                            }
                        ]
                    },
                    "id": 0,
                    "lastUpdatedDateTime": "2020-02-20 00:00:00",
                    "metadata": {
                        "str": "str"
                    },
                    "questions": [
                        "str"
                    ],
                    "source": "str"
                }
        """

    @overload
    def begin_update_qnas(
        self, project_name: str, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> LROPoller[Iterable[JSON]]:
        """Updates the QnAs of a project.

        Updates the QnAs of a project.

        :param project_name: The name of the project to use. Required.
        :type project_name: str
        :param body: Update QnAs parameters of a project. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns an iterator like instance of JSON object
        :rtype: ~azure.core.polling.LROPoller[~azure.core.paging.ItemPaged[JSON]]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200, 202
                response == {
                    "activeLearningSuggestions": [
                        {
                            "clusterHead": "str",
                            "suggestedQuestions": [
                                {
                                    "autoSuggestedCount": 0,
                                    "question": "str",
                                    "userSuggestedCount": 0
                                }
                            ]
                        }
                    ],
                    "answer": "str",
                    "dialog": {
                        "isContextOnly": bool,
                        "prompts": [
                            {
                                "displayOrder": 0,
                                "displayText": "str",
                                "qna": {
                                    "activeLearningSuggestions": [
                                        {
                                            "clusterHead": "str",
                                            "suggestedQuestions": [
                                                {
                "autoSuggestedCount": 0,
                                                    "question":
                                                      "str",
                "userSuggestedCount": 0
                                                }
                                            ]
                                        }
                                    ],
                                    "answer": "str",
                                    "dialog": ...,
                                    "id": 0,
                                    "metadata": {
                                        "str": "str"
                                    },
                                    "questions": [
                                        "str"
                                    ],
                                    "source": "str"
                                },
                                "qnaId": 0
                            }
                        ]
                    },
                    "id": 0,
                    "lastUpdatedDateTime": "2020-02-20 00:00:00",
                    "metadata": {
                        "str": "str"
                    },
                    "questions": [
                        "str"
                    ],
                    "source": "str"
                }
        """

    @distributed_trace
    def begin_update_qnas(
        self, project_name: str, body: Union[List[JSON], IO[bytes]], **kwargs: Any
    ) -> LROPoller[Iterable[JSON]]:
        """Updates the QnAs of a project.

        Updates the QnAs of a project.

        :param project_name: The name of the project to use. Required.
        :type project_name: str
        :param body: Update QnAs parameters of a project. Is either a [JSON] type or a IO[bytes] type.
         Required.
        :type body: list[JSON] or IO[bytes]
        :return: An instance of LROPoller that returns an iterator like instance of JSON object
        :rtype: ~azure.core.polling.LROPoller[~azure.core.paging.ItemPaged[JSON]]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200, 202
                response == {
                    "activeLearningSuggestions": [
                        {
                            "clusterHead": "str",
                            "suggestedQuestions": [
                                {
                                    "autoSuggestedCount": 0,
                                    "question": "str",
                                    "userSuggestedCount": 0
                                }
                            ]
                        }
                    ],
                    "answer": "str",
                    "dialog": {
                        "isContextOnly": bool,
                        "prompts": [
                            {
                                "displayOrder": 0,
                                "displayText": "str",
                                "qna": {
                                    "activeLearningSuggestions": [
                                        {
                                            "clusterHead": "str",
                                            "suggestedQuestions": [
                                                {
                "autoSuggestedCount": 0,
                                                    "question":
                                                      "str",
                "userSuggestedCount": 0
                                                }
                                            ]
                                        }
                                    ],
                                    "answer": "str",
                                    "dialog": ...,
                                    "id": 0,
                                    "metadata": {
                                        "str": "str"
                                    },
                                    "questions": [
                                        "str"
                                    ],
                                    "source": "str"
                                },
                                "qnaId": 0
                            }
                        ]
                    },
                    "id": 0,
                    "lastUpdatedDateTime": "2020-02-20 00:00:00",
                    "metadata": {
                        "str": "str"
                    },
                    "questions": [
                        "str"
                    ],
                    "source": "str"
                }
        """

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _json = body

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_question_answering_projects_update_qnas_request(
                    project_name=project_name,
                    content_type=content_type,
                    api_version=self._config.api_version,
                    json=_json,
                    content=_content,
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
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = deserialized.get("value", [])
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
                raise HttpResponseError(response=response)

            return pipeline_response

        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._update_qnas_initial(
                project_name=project_name,
                body=body,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            def internal_get_next(next_link=None):
                if next_link is None:
                    return pipeline_response
                return get_next(next_link)

            return ItemPaged(internal_get_next, extract_data)

        if polling is True:
            polling_method: PollingMethod = cast(PollingMethod, LROBasePolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[Iterable[JSON]].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[Iterable[JSON]](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )
