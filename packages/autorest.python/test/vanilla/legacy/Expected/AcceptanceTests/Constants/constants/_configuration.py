# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Literal

from azure.core.pipeline import policies

from ._version import VERSION


class AutoRestSwaggerConstantServiceConfiguration:  # pylint: disable=too-many-instance-attributes,name-too-long
    """Configuration for AutoRestSwaggerConstantService.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :keyword header_constant: Constant header property on the client that is a required parameter
     for operation 'constants_putClientConstants'. Default value is True. Note that overriding this
     default value may result in unsupported behavior.
    :paramtype header_constant: bool
    :keyword query_constant: Constant query property on the client that is a required parameter for
     operation 'constants_putClientConstants'. Default value is 100. Note that overriding this
     default value may result in unsupported behavior.
    :paramtype query_constant: int
    :keyword path_constant: Constant path property on the client that is a required parameter for
     operation 'constants_putClientConstants'. Default value is "path". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype path_constant: str
    """

    def __init__(self, **kwargs: Any) -> None:
        header_constant: Literal[True] = kwargs.pop("header_constant", True)
        query_constant: Literal[100] = kwargs.pop("query_constant", 100)
        path_constant: Literal["path"] = kwargs.pop("path_constant", "path")

        self.header_constant = header_constant
        self.query_constant = query_constant
        self.path_constant = path_constant
        kwargs.setdefault("sdk_moniker", "autorestswaggerconstantservice/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
