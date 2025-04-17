# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, Optional, overload

from .._vendor.model_base import Model as _Model, rest_field


class User(_Model):
    """Sample Model.

    :ivar id: The user's id. Required.
    :vartype id: int
    :ivar name: The user's name.
    :vartype name: str
    """

    id: int = rest_field(visibility=["read"])
    """The user's id. Required."""
    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The user's name."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UserActionParam(_Model):
    """User action param.

    :ivar user_action_value: User action value. Required.
    :vartype user_action_value: str
    """

    user_action_value: str = rest_field(
        name="userActionValue", visibility=["read", "create", "update", "delete", "query"]
    )
    """User action value. Required."""

    @overload
    def __init__(
        self,
        *,
        user_action_value: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UserActionResponse(_Model):
    """User action response.

    :ivar user_action_result: User action result. Required.
    :vartype user_action_result: str
    """

    user_action_result: str = rest_field(
        name="userActionResult", visibility=["read", "create", "update", "delete", "query"]
    )
    """User action result. Required."""

    @overload
    def __init__(
        self,
        *,
        user_action_result: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
