# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ParamAliasPreparer
from testpreparer_async import ParamAliasClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestParamAliasAsync(ParamAliasClientTestBaseAsync):
    @ParamAliasPreparer()
    @recorded_by_proxy_async
    async def test_with_aliased_name(self, paramalias_endpoint):
        client = self.create_async_client(endpoint=paramalias_endpoint)
        response = await client.with_aliased_name()

        # please add some check logic here by yourself
        # ...

    @ParamAliasPreparer()
    @recorded_by_proxy_async
    async def test_with_original_name(self, paramalias_endpoint):
        client = self.create_async_client(endpoint=paramalias_endpoint)
        response = await client.with_original_name()

        # please add some check logic here by yourself
        # ...
