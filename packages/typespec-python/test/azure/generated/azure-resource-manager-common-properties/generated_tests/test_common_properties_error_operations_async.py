# coding=utf-8
import pytest
from azure.resourcemanager.commonproperties.aio import CommonPropertiesClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCommonPropertiesErrorOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CommonPropertiesClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_error_get_for_predefined_error(self, resource_group):
        response = await self.client.error.get_for_predefined_error(
            resource_group_name=resource_group.name,
            confidential_resource_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_error_create_for_user_defined_error(self, resource_group):
        response = await self.client.error.create_for_user_defined_error(
            resource_group_name=resource_group.name,
            confidential_resource_name="str",
            resource={
                "location": "str",
                "id": "str",
                "name": "str",
                "properties": {"provisioningState": "str", "username": "str"},
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "type": "str",
            },
        )

        # please add some check logic here by yourself
        # ...
