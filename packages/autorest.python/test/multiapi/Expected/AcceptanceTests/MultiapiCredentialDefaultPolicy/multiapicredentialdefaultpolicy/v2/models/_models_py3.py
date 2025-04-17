# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from .. import serialization as _serialization


class Error(serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

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


class ModelTwo(serialization.Model):
    """Only exists in api version 2.0.0.

    All required parameters must be populated in order to send to server.

    :ivar id: Required.
    :vartype id: int
    :ivar message:
    :vartype message: str
    """

    _validation = {
        "id": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(
        self, *, id: int, message: Optional[str] = None, **kwargs: Any  # pylint: disable=redefined-builtin
    ) -> None:
        """
        :keyword id: Required.
        :paramtype id: int
        :keyword message:
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.id = id
        self.message = message
