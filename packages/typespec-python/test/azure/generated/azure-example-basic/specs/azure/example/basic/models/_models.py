# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

from typing import Any, Dict, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class ActionRequest(_model_base.Model):
    """ActionRequest.

    :ivar string_property: Required.
    :vartype string_property: str
    :ivar model_property:
    :vartype model_property: ~specs.azure.example.basic.models.Model
    :ivar array_property:
    :vartype array_property: list[str]
    :ivar record_property:
    :vartype record_property: dict[str, str]
    """

    string_property: str = rest_field(name="stringProperty", visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    model_property: Optional["_models.Model"] = rest_field(
        name="modelProperty", visibility=["read", "create", "update", "delete", "query"]
    )
    array_property: Optional[List[str]] = rest_field(
        name="arrayProperty", visibility=["read", "create", "update", "delete", "query"]
    )
    record_property: Optional[Dict[str, str]] = rest_field(
        name="recordProperty", visibility=["read", "create", "update", "delete", "query"]
    )

    @overload
    def __init__(
        self,
        *,
        string_property: str,
        model_property: Optional["_models.Model"] = None,
        array_property: Optional[List[str]] = None,
        record_property: Optional[Dict[str, str]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ActionResponse(_model_base.Model):
    """ActionResponse.

    :ivar string_property: Required.
    :vartype string_property: str
    :ivar model_property:
    :vartype model_property: ~specs.azure.example.basic.models.Model
    :ivar array_property:
    :vartype array_property: list[str]
    :ivar record_property:
    :vartype record_property: dict[str, str]
    """

    string_property: str = rest_field(name="stringProperty", visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    model_property: Optional["_models.Model"] = rest_field(
        name="modelProperty", visibility=["read", "create", "update", "delete", "query"]
    )
    array_property: Optional[List[str]] = rest_field(
        name="arrayProperty", visibility=["read", "create", "update", "delete", "query"]
    )
    record_property: Optional[Dict[str, str]] = rest_field(
        name="recordProperty", visibility=["read", "create", "update", "delete", "query"]
    )

    @overload
    def __init__(
        self,
        *,
        string_property: str,
        model_property: Optional["_models.Model"] = None,
        array_property: Optional[List[str]] = None,
        record_property: Optional[Dict[str, str]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Model(_model_base.Model):
    """Model.

    :ivar int32_property:
    :vartype int32_property: int
    :ivar float32_property:
    :vartype float32_property: float
    :ivar enum_property: "EnumValue1"
    :vartype enum_property: str or ~specs.azure.example.basic.models.EnumEnum
    """

    int32_property: Optional[int] = rest_field(
        name="int32Property", visibility=["read", "create", "update", "delete", "query"]
    )
    float32_property: Optional[float] = rest_field(
        name="float32Property", visibility=["read", "create", "update", "delete", "query"]
    )
    enum_property: Optional[Union[str, "_models.EnumEnum"]] = rest_field(
        name="enumProperty", visibility=["read", "create", "update", "delete", "query"]
    )
    """\"EnumValue1\""""

    @overload
    def __init__(
        self,
        *,
        int32_property: Optional[int] = None,
        float32_property: Optional[float] = None,
        enum_property: Optional[Union[str, "_models.EnumEnum"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
