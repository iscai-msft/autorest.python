# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core.pipeline import policies

from ._version import VERSION


class HeaderParamClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for HeaderParamClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param name: The name of the client. This parameter is used as a header in all operations.
     Required.
    :type name: str
    :param endpoint: Service host. Default value is "http://localhost:3000".
    :type endpoint: str
    """

    def __init__(self, name: str, endpoint: str = "http://localhost:3000", **kwargs: Any) -> None:
        if name is None:
            raise ValueError("Parameter 'name' must not be None.")

        self.name = name
        self.endpoint = endpoint
        kwargs.setdefault("sdk_moniker", "specs-azure-clientgenerator-core-clientinitialization/{}".format(VERSION))
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


class MultipleParamsClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for MultipleParamsClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param name: The name of the client. This parameter is used as a header in all operations.
     Required.
    :type name: str
    :param region: The region to use for all operations. This parameter is used as a query
     parameter. Required.
    :type region: str
    :param endpoint: Service host. Default value is "http://localhost:3000".
    :type endpoint: str
    """

    def __init__(self, name: str, region: str, endpoint: str = "http://localhost:3000", **kwargs: Any) -> None:
        if name is None:
            raise ValueError("Parameter 'name' must not be None.")
        if region is None:
            raise ValueError("Parameter 'region' must not be None.")

        self.name = name
        self.region = region
        self.endpoint = endpoint
        kwargs.setdefault("sdk_moniker", "specs-azure-clientgenerator-core-clientinitialization/{}".format(VERSION))
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


class MixedParamsClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for MixedParamsClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param name: The name of the client. This parameter is used as a header in all operations.
     Required.
    :type name: str
    :param endpoint: Service host. Default value is "http://localhost:3000".
    :type endpoint: str
    """

    def __init__(self, name: str, endpoint: str = "http://localhost:3000", **kwargs: Any) -> None:
        if name is None:
            raise ValueError("Parameter 'name' must not be None.")

        self.name = name
        self.endpoint = endpoint
        kwargs.setdefault("sdk_moniker", "specs-azure-clientgenerator-core-clientinitialization/{}".format(VERSION))
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


class PathParamClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for PathParamClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param blob_name: The name of the blob. This parameter is used as a path parameter in all
     operations. Required.
    :type blob_name: str
    :param endpoint: Service host. Default value is "http://localhost:3000".
    :type endpoint: str
    """

    def __init__(self, blob_name: str, endpoint: str = "http://localhost:3000", **kwargs: Any) -> None:
        if blob_name is None:
            raise ValueError("Parameter 'blob_name' must not be None.")

        self.blob_name = blob_name
        self.endpoint = endpoint
        kwargs.setdefault("sdk_moniker", "specs-azure-clientgenerator-core-clientinitialization/{}".format(VERSION))
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


class ParamAliasClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for ParamAliasClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param blob_name: Blob name for the client. Required.
    :type blob_name: str
    :param endpoint: Service host. Default value is "http://localhost:3000".
    :type endpoint: str
    """

    def __init__(self, blob_name: str, endpoint: str = "http://localhost:3000", **kwargs: Any) -> None:
        if blob_name is None:
            raise ValueError("Parameter 'blob_name' must not be None.")

        self.blob_name = blob_name
        self.endpoint = endpoint
        kwargs.setdefault("sdk_moniker", "specs-azure-clientgenerator-core-clientinitialization/{}".format(VERSION))
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
