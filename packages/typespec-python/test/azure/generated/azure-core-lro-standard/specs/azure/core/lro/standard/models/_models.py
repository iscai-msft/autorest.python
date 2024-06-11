# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class ExportedUser(_model_base.Model):
    """The exported user data.


    :ivar name: The name of user. Required.
    :vartype name: str
    :ivar resource_uri: The exported URI. Required.
    :vartype resource_uri: str
    """

    name: str = rest_field()
    """The name of user. Required."""
    resource_uri: str = rest_field(name="resourceUri")
    """The exported URI. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        resource_uri: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class User(_model_base.Model):
    """Details about a user.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar name: The name of user. Required.
    :vartype name: str
    :ivar role: The role of user. Required.
    :vartype role: str
    """

    name: str = rest_field(visibility=["read"])
    """The name of user. Required."""
    role: str = rest_field()
    """The role of user. Required."""

    @overload
    def __init__(
        self,
        *,
        role: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
