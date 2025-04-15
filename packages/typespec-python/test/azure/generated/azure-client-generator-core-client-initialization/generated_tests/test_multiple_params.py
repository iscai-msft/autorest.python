# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import MultipleParamsClientTestBase, MultipleParamsPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMultipleParams(MultipleParamsClientTestBase):
    @MultipleParamsPreparer()
    @recorded_by_proxy
    def test_with_query(self, multipleparams_endpoint):
        client = self.create_client(endpoint=multipleparams_endpoint)
        response = client.with_query(
            id="str",
        )

        # please add some check logic here by yourself
        # ...

    @MultipleParamsPreparer()
    @recorded_by_proxy
    def test_with_body(self, multipleparams_endpoint):
        client = self.create_client(endpoint=multipleparams_endpoint)
        response = client.with_body(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...
