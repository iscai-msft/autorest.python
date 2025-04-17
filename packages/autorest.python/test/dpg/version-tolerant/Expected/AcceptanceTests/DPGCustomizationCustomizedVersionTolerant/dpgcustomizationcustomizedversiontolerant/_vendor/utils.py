# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from abc import ABC
from typing import Generic, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from .serialization import Deserializer, Serializer


TClient = TypeVar("TClient")
TConfig = TypeVar("TConfig")


class ClientMixinABC(ABC, Generic[TClient, TConfig]):
    """DO NOT use this class. It is for internal typing use only."""

    _client: TClient
    _config: TConfig
    _serialize: "Serializer"
    _deserialize: "Deserializer"
