# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from .._utils import serialization as _serialization


class Error(_serialization.Model):
    """Error.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar status:
    :vartype status: int
    :ivar constant_id: Required. Default value is 1.
    :vartype constant_id: int
    :ivar message:
    :vartype message: str
    """

    _validation = {
        "constant_id": {"required": True, "constant": True},
    }

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "constant_id": {"key": "constantId", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    constant_id = 1

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.status = status
        self.message = message


class HeaderCustomNamedRequestIdParamGroupingParameters(_serialization.Model):  # pylint: disable=name-too-long
    """Parameter group.

    All required parameters must be populated in order to send to server.

    :ivar foo_client_request_id: The fooRequestId. Required.
    :vartype foo_client_request_id: str
    """

    _validation = {
        "foo_client_request_id": {"required": True},
    }

    _attribute_map = {
        "foo_client_request_id": {"key": "foo-client-request-id", "type": "str"},
    }

    def __init__(self, *, foo_client_request_id: str, **kwargs: Any) -> None:
        """
        :keyword foo_client_request_id: The fooRequestId. Required.
        :paramtype foo_client_request_id: str
        """
        super().__init__(**kwargs)
        self.foo_client_request_id = foo_client_request_id


class OdataFilter(_serialization.Model):
    """OdataFilter.

    :ivar id:
    :vartype id: int
    :ivar name:
    :vartype name: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,  # pylint: disable=redefined-builtin
        name: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword id:
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        """
        super().__init__(**kwargs)
        self.id = id
        self.name = name
