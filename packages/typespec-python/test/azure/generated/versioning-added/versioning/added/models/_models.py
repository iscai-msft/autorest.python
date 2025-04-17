# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, TYPE_CHECKING, Union, overload

from .._vendor.model_base import Model as _Model, rest_field

if TYPE_CHECKING:
    from .. import _types, models as _models


class ModelV1(_Model):
    """ModelV1.

    :ivar prop: Required.
    :vartype prop: str
    :ivar enum_prop: Required. Known values are: "enumMemberV1" and "enumMemberV2".
    :vartype enum_prop: str or ~versioning.added.models.EnumV1
    :ivar union_prop: Required. Is either a str type or a int type.
    :vartype union_prop: str or int
    """

    prop: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    enum_prop: Union[str, "_models.EnumV1"] = rest_field(
        name="enumProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required. Known values are: \"enumMemberV1\" and \"enumMemberV2\"."""
    union_prop: "_types.UnionV1" = rest_field(
        name="unionProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required. Is either a str type or a int type."""

    @overload
    def __init__(
        self,
        *,
        prop: str,
        enum_prop: Union[str, "_models.EnumV1"],
        union_prop: "_types.UnionV1",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelV2(_Model):
    """ModelV2.

    :ivar prop: Required.
    :vartype prop: str
    :ivar enum_prop: Required. "enumMember"
    :vartype enum_prop: str or ~versioning.added.models.EnumV2
    :ivar union_prop: Required. Is either a str type or a int type.
    :vartype union_prop: str or int
    """

    prop: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    enum_prop: Union[str, "_models.EnumV2"] = rest_field(
        name="enumProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required. \"enumMember\""""
    union_prop: "_types.UnionV2" = rest_field(
        name="unionProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required. Is either a str type or a int type."""

    @overload
    def __init__(
        self,
        *,
        prop: str,
        enum_prop: Union[str, "_models.EnumV2"],
        union_prop: "_types.UnionV2",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
