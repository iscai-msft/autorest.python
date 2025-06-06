# pylint: disable=line-too-long,useless-suppression,too-many-lines
# coding=utf-8
# pylint: disable=useless-super-delegation

import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_discriminator, rest_field

if TYPE_CHECKING:
    from .. import models as _models


class DifferentSpreadFloatRecord(_model_base.Model):
    """The model spread Record<float32> with the different known property type.

    :ivar name: The id property. Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The id property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DifferentSpreadFloatDerived(DifferentSpreadFloatRecord):
    """The model extends from a model that spread Record<float32> with the different known property
    type.

    :ivar name: The id property. Required.
    :vartype name: str
    :ivar derived_prop: The index property. Required.
    :vartype derived_prop: float
    """

    derived_prop: float = rest_field(name="derivedProp", visibility=["read", "create", "update", "delete", "query"])
    """The index property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        derived_prop: float,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DifferentSpreadModelArrayRecord(_model_base.Model):
    """The model spread Record<ModelForRecord[]> with the different known property type.

    :ivar known_prop: Required.
    :vartype known_prop: str
    """

    known_prop: str = rest_field(name="knownProp", visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DifferentSpreadModelArrayDerived(DifferentSpreadModelArrayRecord):
    """The model extends from a model that spread Record<ModelForRecord[]> with the different known
    property type.

    :ivar known_prop: Required.
    :vartype known_prop: str
    :ivar derived_prop: The index property. Required.
    :vartype derived_prop: list[~typetest.property.additionalproperties.models.ModelForRecord]
    """

    derived_prop: List["_models.ModelForRecord"] = rest_field(
        name="derivedProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """The index property. Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: str,
        derived_prop: List["_models.ModelForRecord"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DifferentSpreadModelRecord(_model_base.Model):
    """The model spread Record<ModelForRecord> with the different known property type.

    :ivar known_prop: Required.
    :vartype known_prop: str
    """

    known_prop: str = rest_field(name="knownProp", visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DifferentSpreadModelDerived(DifferentSpreadModelRecord):
    """The model extends from a model that spread Record<ModelForRecord> with the different known
    property type.

    :ivar known_prop: Required.
    :vartype known_prop: str
    :ivar derived_prop: The index property. Required.
    :vartype derived_prop: ~typetest.property.additionalproperties.models.ModelForRecord
    """

    derived_prop: "_models.ModelForRecord" = rest_field(
        name="derivedProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """The index property. Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: str,
        derived_prop: "_models.ModelForRecord",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DifferentSpreadStringRecord(_model_base.Model):
    """The model spread Record<string> with the different known property type.

    :ivar id: The name property. Required.
    :vartype id: float
    """

    id: float = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        id: float,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DifferentSpreadStringDerived(DifferentSpreadStringRecord):
    """The model extends from a model that spread Record<string> with the different known property
    type.

    :ivar id: The name property. Required.
    :vartype id: float
    :ivar derived_prop: The index property. Required.
    :vartype derived_prop: str
    """

    derived_prop: str = rest_field(name="derivedProp", visibility=["read", "create", "update", "delete", "query"])
    """The index property. Required."""

    @overload
    def __init__(
        self,
        *,
        id: float,  # pylint: disable=redefined-builtin
        derived_prop: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ExtendsFloatAdditionalProperties(_model_base.Model):
    """The model extends from Record<float32> type.

    :ivar id: The id property. Required.
    :vartype id: float
    """

    id: float = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The id property. Required."""

    @overload
    def __init__(
        self,
        *,
        id: float,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ExtendsModelAdditionalProperties(_model_base.Model):
    """The model extends from Record<ModelForRecord> type.

    :ivar known_prop: Required.
    :vartype known_prop: ~typetest.property.additionalproperties.models.ModelForRecord
    """

    known_prop: "_models.ModelForRecord" = rest_field(
        name="knownProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: "_models.ModelForRecord",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ExtendsModelArrayAdditionalProperties(_model_base.Model):
    """The model extends from Record<ModelForRecord[]> type.

    :ivar known_prop: Required.
    :vartype known_prop: list[~typetest.property.additionalproperties.models.ModelForRecord]
    """

    known_prop: List["_models.ModelForRecord"] = rest_field(
        name="knownProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: List["_models.ModelForRecord"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ExtendsStringAdditionalProperties(_model_base.Model):
    """The model extends from Record<string> type.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ExtendsUnknownAdditionalProperties(_model_base.Model):
    """The model extends from Record<unknown> type.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ExtendsUnknownAdditionalPropertiesDerived(ExtendsUnknownAdditionalProperties):  # pylint: disable=name-too-long
    """The model extends from a type that extends from Record<unknown>.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    index: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The index property. Required."""
    age: Optional[float] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ExtendsUnknownAdditionalPropertiesDiscriminated(_model_base.Model):  # pylint: disable=name-too-long
    """The model extends from Record<unknown> with a discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    ExtendsUnknownAdditionalPropertiesDiscriminatedDerived

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: The discriminator. Required. Default value is None.
    :vartype kind: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""
    kind: str = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])
    """The discriminator. Required. Default value is None."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        kind: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ExtendsUnknownAdditionalPropertiesDiscriminatedDerived(
    ExtendsUnknownAdditionalPropertiesDiscriminated, discriminator="derived"
):  # pylint: disable=name-too-long
    """The derived discriminated type.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: Required. Default value is "derived".
    :vartype kind: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    kind: Literal["derived"] = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Required. Default value is \"derived\"."""
    index: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The index property. Required."""
    age: Optional[float] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="derived", **kwargs)


class IsFloatAdditionalProperties(_model_base.Model):
    """The model is from Record<float32> type.

    :ivar id: The id property. Required.
    :vartype id: float
    """

    id: float = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The id property. Required."""

    @overload
    def __init__(
        self,
        *,
        id: float,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class IsModelAdditionalProperties(_model_base.Model):
    """The model is from Record<ModelForRecord> type.

    :ivar known_prop: Required.
    :vartype known_prop: ~typetest.property.additionalproperties.models.ModelForRecord
    """

    known_prop: "_models.ModelForRecord" = rest_field(
        name="knownProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: "_models.ModelForRecord",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class IsModelArrayAdditionalProperties(_model_base.Model):
    """The model is from Record<ModelForRecord[]> type.

    :ivar known_prop: Required.
    :vartype known_prop: list[~typetest.property.additionalproperties.models.ModelForRecord]
    """

    known_prop: List["_models.ModelForRecord"] = rest_field(
        name="knownProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: List["_models.ModelForRecord"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class IsStringAdditionalProperties(_model_base.Model):
    """The model is from Record<string> type.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class IsUnknownAdditionalProperties(_model_base.Model):
    """The model is from Record<unknown> type.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class IsUnknownAdditionalPropertiesDerived(IsUnknownAdditionalProperties):
    """The model extends from a type that is Record<unknown> type.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    index: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The index property. Required."""
    age: Optional[float] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class IsUnknownAdditionalPropertiesDiscriminated(_model_base.Model):  # pylint: disable=name-too-long
    """The model is Record<unknown> with a discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    IsUnknownAdditionalPropertiesDiscriminatedDerived

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: The discriminator. Required. Default value is None.
    :vartype kind: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""
    kind: str = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])
    """The discriminator. Required. Default value is None."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        kind: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class IsUnknownAdditionalPropertiesDiscriminatedDerived(
    IsUnknownAdditionalPropertiesDiscriminated, discriminator="derived"
):  # pylint: disable=name-too-long
    """The derived discriminated type.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: Required. Default value is "derived".
    :vartype kind: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    kind: Literal["derived"] = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Required. Default value is \"derived\"."""
    index: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The index property. Required."""
    age: Optional[float] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="derived", **kwargs)


class ModelForRecord(_model_base.Model):
    """model for record.

    :ivar state: The state property. Required.
    :vartype state: str
    """

    state: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The state property. Required."""

    @overload
    def __init__(
        self,
        *,
        state: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class MultipleSpreadRecord(_model_base.Model):
    """The model spread Record<string> and Record<float32>.

    :ivar flag: The name property. Required.
    :vartype flag: bool
    """

    flag: bool = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        flag: bool,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SpreadFloatRecord(_model_base.Model):
    """The model spread Record<float32> with the same known property type.

    :ivar id: The id property. Required.
    :vartype id: float
    """

    id: float = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The id property. Required."""

    @overload
    def __init__(
        self,
        *,
        id: float,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SpreadModelArrayRecord(_model_base.Model):
    """SpreadModelArrayRecord.

    :ivar known_prop: Required.
    :vartype known_prop: list[~typetest.property.additionalproperties.models.ModelForRecord]
    """

    known_prop: List["_models.ModelForRecord"] = rest_field(
        name="knownProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: List["_models.ModelForRecord"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SpreadModelRecord(_model_base.Model):
    """The model spread Record<ModelForRecord> with the same known property type.

    :ivar known_prop: Required.
    :vartype known_prop: ~typetest.property.additionalproperties.models.ModelForRecord
    """

    known_prop: "_models.ModelForRecord" = rest_field(
        name="knownProp", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: "_models.ModelForRecord",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SpreadRecordForNonDiscriminatedUnion(_model_base.Model):
    """The model spread Record<WidgetData0 | WidgetData1>.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SpreadRecordForNonDiscriminatedUnion2(_model_base.Model):
    """The model spread Record<WidgetData2 | WidgetData1>.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SpreadRecordForNonDiscriminatedUnion3(_model_base.Model):
    """The model spread Record<WidgetData2[] | WidgetData1>.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SpreadRecordForUnion(_model_base.Model):
    """The model spread Record<string | float32>.

    :ivar flag: The name property. Required.
    :vartype flag: bool
    """

    flag: bool = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        flag: bool,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SpreadStringRecord(_model_base.Model):
    """The model spread Record<string> with the same known property type.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class WidgetData0(_model_base.Model):
    """WidgetData0.

    :ivar kind: Required. Default value is "kind0".
    :vartype kind: str
    :ivar foo_prop: Required.
    :vartype foo_prop: str
    """

    kind: Literal["kind0"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required. Default value is \"kind0\"."""
    foo_prop: str = rest_field(name="fooProp", visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        foo_prop: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal["kind0"] = "kind0"


class WidgetData1(_model_base.Model):
    """WidgetData1.

    :ivar kind: Required. Default value is "kind1".
    :vartype kind: str
    :ivar start: Required.
    :vartype start: ~datetime.datetime
    :ivar end:
    :vartype end: ~datetime.datetime
    """

    kind: Literal["kind1"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required. Default value is \"kind1\"."""
    start: datetime.datetime = rest_field(visibility=["read", "create", "update", "delete", "query"], format="rfc3339")
    """Required."""
    end: Optional[datetime.datetime] = rest_field(
        visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )

    @overload
    def __init__(
        self,
        *,
        start: datetime.datetime,
        end: Optional[datetime.datetime] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal["kind1"] = "kind1"


class WidgetData2(_model_base.Model):
    """WidgetData2.

    :ivar kind: Required. Default value is "kind1".
    :vartype kind: str
    :ivar start: Required.
    :vartype start: str
    """

    kind: Literal["kind1"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required. Default value is \"kind1\"."""
    start: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        start: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal["kind1"] = "kind1"
