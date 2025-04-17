# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from .._vendor import serialization as _serialization


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


class Product(serialization.Model):
    """Product.

    :ivar integer:
    :vartype integer: int
    :ivar string:
    :vartype string: str
    """

    _attribute_map = {
        "integer": {"key": "integer", "type": "int"},
        "string": {"key": "string", "type": "str"},
    }

    def __init__(self, *, integer: Optional[int] = None, string: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword integer:
        :paramtype integer: int
        :keyword string:
        :paramtype string: str
        """
        super().__init__(**kwargs)
        self.integer = integer
        self.string = string
