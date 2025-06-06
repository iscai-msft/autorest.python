# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, overload

from ... import _model_base
from ..._model_base import rest_field


class JsonEncodedNameModel(_model_base.Model):
    """JsonEncodedNameModel.

    :ivar default_name: Pass in true. Required.
    :vartype default_name: bool
    """

    default_name: bool = rest_field(name="wireName", visibility=["read", "create", "update", "delete", "query"])
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        default_name: bool,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
