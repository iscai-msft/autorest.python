# coding=utf-8

from copy import deepcopy
from typing import Any
from typing_extensions import Self

from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import XmlClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    ModelWithArrayOfModelValueOperations,
    ModelWithAttributesValueOperations,
    ModelWithDictionaryValueOperations,
    ModelWithEmptyArrayValueOperations,
    ModelWithEncodedNamesValueOperations,
    ModelWithOptionalFieldValueOperations,
    ModelWithRenamedArraysValueOperations,
    ModelWithRenamedFieldsValueOperations,
    ModelWithSimpleArraysValueOperations,
    ModelWithTextValueOperations,
    ModelWithUnwrappedArrayValueOperations,
    SimpleModelValueOperations,
)


class XmlClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Sends and receives bodies in XML format.

    :ivar simple_model_value: SimpleModelValueOperations operations
    :vartype simple_model_value: payload.xml.operations.SimpleModelValueOperations
    :ivar model_with_simple_arrays_value: ModelWithSimpleArraysValueOperations operations
    :vartype model_with_simple_arrays_value:
     payload.xml.operations.ModelWithSimpleArraysValueOperations
    :ivar model_with_array_of_model_value: ModelWithArrayOfModelValueOperations operations
    :vartype model_with_array_of_model_value:
     payload.xml.operations.ModelWithArrayOfModelValueOperations
    :ivar model_with_optional_field_value: ModelWithOptionalFieldValueOperations operations
    :vartype model_with_optional_field_value:
     payload.xml.operations.ModelWithOptionalFieldValueOperations
    :ivar model_with_attributes_value: ModelWithAttributesValueOperations operations
    :vartype model_with_attributes_value: payload.xml.operations.ModelWithAttributesValueOperations
    :ivar model_with_unwrapped_array_value: ModelWithUnwrappedArrayValueOperations operations
    :vartype model_with_unwrapped_array_value:
     payload.xml.operations.ModelWithUnwrappedArrayValueOperations
    :ivar model_with_renamed_arrays_value: ModelWithRenamedArraysValueOperations operations
    :vartype model_with_renamed_arrays_value:
     payload.xml.operations.ModelWithRenamedArraysValueOperations
    :ivar model_with_renamed_fields_value: ModelWithRenamedFieldsValueOperations operations
    :vartype model_with_renamed_fields_value:
     payload.xml.operations.ModelWithRenamedFieldsValueOperations
    :ivar model_with_empty_array_value: ModelWithEmptyArrayValueOperations operations
    :vartype model_with_empty_array_value:
     payload.xml.operations.ModelWithEmptyArrayValueOperations
    :ivar model_with_text_value: ModelWithTextValueOperations operations
    :vartype model_with_text_value: payload.xml.operations.ModelWithTextValueOperations
    :ivar model_with_dictionary_value: ModelWithDictionaryValueOperations operations
    :vartype model_with_dictionary_value: payload.xml.operations.ModelWithDictionaryValueOperations
    :ivar model_with_encoded_names_value: ModelWithEncodedNamesValueOperations operations
    :vartype model_with_encoded_names_value:
     payload.xml.operations.ModelWithEncodedNamesValueOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = XmlClientConfiguration(endpoint=endpoint, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.logging_policy,
            ]
        self._client: PipelineClient = PipelineClient(endpoint=_endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.simple_model_value = SimpleModelValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_simple_arrays_value = ModelWithSimpleArraysValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_array_of_model_value = ModelWithArrayOfModelValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_optional_field_value = ModelWithOptionalFieldValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_attributes_value = ModelWithAttributesValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_unwrapped_array_value = ModelWithUnwrappedArrayValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_renamed_arrays_value = ModelWithRenamedArraysValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_renamed_fields_value = ModelWithRenamedFieldsValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_empty_array_value = ModelWithEmptyArrayValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_text_value = ModelWithTextValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_dictionary_value = ModelWithDictionaryValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_encoded_names_value = ModelWithEncodedNamesValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from corehttp.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~corehttp.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~corehttp.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
