# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# pylint: disable=useless-super-delegation

import datetime
from typing import Any, Dict, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class ErrorAdditionalInfo(_model_base.Model):
    """The resource management error additional info.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: any
    """

    type: Optional[str] = rest_field(visibility=["read"])
    """The additional info type."""
    info: Optional[Any] = rest_field(visibility=["read"])
    """The additional info."""


class ErrorDetail(_model_base.Model):
    """The error detail.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.resourcemanager.resources.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.resourcemanager.resources.models.ErrorAdditionalInfo]
    """

    code: Optional[str] = rest_field(visibility=["read"])
    """The error code."""
    message: Optional[str] = rest_field(visibility=["read"])
    """The error message."""
    target: Optional[str] = rest_field(visibility=["read"])
    """The error target."""
    details: Optional[List["_models.ErrorDetail"]] = rest_field(visibility=["read"])
    """The error details."""
    additional_info: Optional[List["_models.ErrorAdditionalInfo"]] = rest_field(
        name="additionalInfo", visibility=["read"]
    )
    """The error additional info."""


class ErrorResponse(_model_base.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations.

    :ivar error: The error object.
    :vartype error: ~azure.resourcemanager.resources.models.ErrorDetail
    """

    error: Optional["_models.ErrorDetail"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The error object."""

    @overload
    def __init__(
        self,
        *,
        error: Optional["_models.ErrorDetail"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Resource(_model_base.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.resources.models.SystemData
    """

    id: Optional[str] = rest_field(visibility=["read"])
    """Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}."""
    name: Optional[str] = rest_field(visibility=["read"])
    """The name of the resource."""
    type: Optional[str] = rest_field(visibility=["read"])
    """The type of the resource. E.g. \"Microsoft.Compute/virtualMachines\" or
     \"Microsoft.Storage/storageAccounts\"."""
    system_data: Optional["_models.SystemData"] = rest_field(name="systemData", visibility=["read"])
    """Azure Resource Manager metadata containing createdBy and modifiedBy information."""


class ExtensionResource(Resource):
    """The base extension resource.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.resources.models.SystemData
    """


class ExtensionsResource(ExtensionResource):
    """Concrete extension resource types can be created by aliasing this type using a specific
    property type.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.resources.models.SystemData
    :ivar properties: The resource-specific properties for this resource.
    :vartype properties: ~azure.resourcemanager.resources.models.ExtensionsResourceProperties
    """

    properties: Optional["_models.ExtensionsResourceProperties"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The resource-specific properties for this resource."""

    @overload
    def __init__(
        self,
        *,
        properties: Optional["_models.ExtensionsResourceProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ExtensionsResourceProperties(_model_base.Model):
    """ExtensionsResource properties.

    :ivar description: The description of the resource.
    :vartype description: str
    :ivar provisioning_state: The status of the last operation. Known values are: "Succeeded",
     "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".
    :vartype provisioning_state: str or ~azure.resourcemanager.resources.models.ProvisioningState
    """

    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The description of the resource."""
    provisioning_state: Optional[Union[str, "_models.ProvisioningState"]] = rest_field(
        name="provisioningState", visibility=["read"]
    )
    """The status of the last operation. Known values are: \"Succeeded\", \"Failed\", \"Canceled\",
     \"Provisioning\", \"Updating\", \"Deleting\", and \"Accepted\"."""

    @overload
    def __init__(
        self,
        *,
        description: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ProxyResource(Resource):
    """The resource model definition for a Azure Resource Manager proxy resource. It will not have
    tags and a location.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.resources.models.SystemData
    """


class LocationResource(ProxyResource):
    """Concrete proxy resource types can be created by aliasing this type using a specific property
    type.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.resources.models.SystemData
    :ivar properties: The resource-specific properties for this resource.
    :vartype properties: ~azure.resourcemanager.resources.models.LocationResourceProperties
    """

    properties: Optional["_models.LocationResourceProperties"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The resource-specific properties for this resource."""

    @overload
    def __init__(
        self,
        *,
        properties: Optional["_models.LocationResourceProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class LocationResourceProperties(_model_base.Model):
    """Location resource properties.

    :ivar description: The description of the resource.
    :vartype description: str
    :ivar provisioning_state: The status of the last operation. Known values are: "Succeeded",
     "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".
    :vartype provisioning_state: str or ~azure.resourcemanager.resources.models.ProvisioningState
    """

    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The description of the resource."""
    provisioning_state: Optional[Union[str, "_models.ProvisioningState"]] = rest_field(
        name="provisioningState", visibility=["read"]
    )
    """The status of the last operation. Known values are: \"Succeeded\", \"Failed\", \"Canceled\",
     \"Provisioning\", \"Updating\", \"Deleting\", and \"Accepted\"."""

    @overload
    def __init__(
        self,
        *,
        description: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class NestedProxyResource(ProxyResource):
    """Nested child of Top Level Tracked Resource.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.resources.models.SystemData
    :ivar properties: The resource-specific properties for this resource.
    :vartype properties: ~azure.resourcemanager.resources.models.NestedProxyResourceProperties
    """

    properties: Optional["_models.NestedProxyResourceProperties"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The resource-specific properties for this resource."""

    @overload
    def __init__(
        self,
        *,
        properties: Optional["_models.NestedProxyResourceProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class NestedProxyResourceProperties(_model_base.Model):
    """Nested Proxy Resource Properties.

    :ivar provisioning_state: Provisioning State of the nested child Resource. Known values are:
     "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".
    :vartype provisioning_state: str or ~azure.resourcemanager.resources.models.ProvisioningState
    :ivar description: Nested resource description.
    :vartype description: str
    """

    provisioning_state: Optional[Union[str, "_models.ProvisioningState"]] = rest_field(
        name="provisioningState", visibility=["read"]
    )
    """Provisioning State of the nested child Resource. Known values are: \"Succeeded\", \"Failed\",
     \"Canceled\", \"Provisioning\", \"Updating\", \"Deleting\", and \"Accepted\"."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Nested resource description."""

    @overload
    def __init__(
        self,
        *,
        description: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class NotificationDetails(_model_base.Model):
    """The details of a user notification.

    :ivar message: The notification message. Required.
    :vartype message: str
    :ivar urgent: If true, the notification is urgent. Required.
    :vartype urgent: bool
    """

    message: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The notification message. Required."""
    urgent: bool = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """If true, the notification is urgent. Required."""

    @overload
    def __init__(
        self,
        *,
        message: str,
        urgent: bool,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which
    has 'tags' and a 'location'.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.resources.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    tags: Optional[Dict[str, str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Resource tags."""
    location: str = rest_field(visibility=["read", "create"])
    """The geo-location where the resource lives. Required."""

    @overload
    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SingletonTrackedResource(TrackedResource):
    """Concrete tracked resource types can be created by aliasing this type using a specific property
    type.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.resources.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar properties: The resource-specific properties for this resource.
    :vartype properties: ~azure.resourcemanager.resources.models.SingletonTrackedResourceProperties
    """

    properties: Optional["_models.SingletonTrackedResourceProperties"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The resource-specific properties for this resource."""

    @overload
    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["_models.SingletonTrackedResourceProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SingletonTrackedResourceProperties(_model_base.Model):
    """Singleton Arm Resource Properties.

    :ivar provisioning_state: The status of the last operation. Known values are: "Succeeded",
     "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".
    :vartype provisioning_state: str or ~azure.resourcemanager.resources.models.ProvisioningState
    :ivar description: The description of the resource.
    :vartype description: str
    """

    provisioning_state: Optional[Union[str, "_models.ProvisioningState"]] = rest_field(
        name="provisioningState", visibility=["read"]
    )
    """The status of the last operation. Known values are: \"Succeeded\", \"Failed\", \"Canceled\",
     \"Provisioning\", \"Updating\", \"Deleting\", and \"Accepted\"."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The description of the resource."""

    @overload
    def __init__(
        self,
        *,
        description: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SystemData(_model_base.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or ~azure.resourcemanager.resources.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or ~azure.resourcemanager.resources.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    created_by: Optional[str] = rest_field(name="createdBy", visibility=["read", "create", "update", "delete", "query"])
    """The identity that created the resource."""
    created_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(
        name="createdByType", visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of identity that created the resource. Known values are: \"User\", \"Application\",
     \"ManagedIdentity\", and \"Key\"."""
    created_at: Optional[datetime.datetime] = rest_field(
        name="createdAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The timestamp of resource creation (UTC)."""
    last_modified_by: Optional[str] = rest_field(
        name="lastModifiedBy", visibility=["read", "create", "update", "delete", "query"]
    )
    """The identity that last modified the resource."""
    last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(
        name="lastModifiedByType", visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of identity that last modified the resource. Known values are: \"User\",
     \"Application\", \"ManagedIdentity\", and \"Key\"."""
    last_modified_at: Optional[datetime.datetime] = rest_field(
        name="lastModifiedAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The timestamp of resource last modification (UTC)."""

    @overload
    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TopLevelTrackedResource(TrackedResource):
    """Concrete tracked resource types can be created by aliasing this type using a specific property
    type.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.resources.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar properties: The resource-specific properties for this resource.
    :vartype properties: ~azure.resourcemanager.resources.models.TopLevelTrackedResourceProperties
    """

    properties: Optional["_models.TopLevelTrackedResourceProperties"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The resource-specific properties for this resource."""

    @overload
    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["_models.TopLevelTrackedResourceProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TopLevelTrackedResourceProperties(_model_base.Model):
    """Top Level Arm Resource Properties.

    :ivar provisioning_state: The status of the last operation. Known values are: "Succeeded",
     "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".
    :vartype provisioning_state: str or ~azure.resourcemanager.resources.models.ProvisioningState
    :ivar description: The description of the resource.
    :vartype description: str
    """

    provisioning_state: Optional[Union[str, "_models.ProvisioningState"]] = rest_field(
        name="provisioningState", visibility=["read"]
    )
    """The status of the last operation. Known values are: \"Succeeded\", \"Failed\", \"Canceled\",
     \"Provisioning\", \"Updating\", \"Deleting\", and \"Accepted\"."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The description of the resource."""

    @overload
    def __init__(
        self,
        *,
        description: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
