# coding=utf-8

from typing import Any, Union

from corehttp.runtime import policies

from .. import models as _models
from .._version import VERSION


class RemovedClientConfiguration:
    """Configuration for RemovedClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Need to be set as '`http://localhost:3000 <http://localhost:3000>`_' in
     client. Required.
    :type endpoint: str
    :param version: Need to be set as 'v1', 'v2preview' or 'v2' in client. Known values are: "v1",
     "v2preview", and "v2". Required.
    :type version: str or ~versioning.removed.models.Versions
    """

    def __init__(self, endpoint: str, version: Union[str, _models.Versions], **kwargs: Any) -> None:
        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if version is None:
            raise ValueError("Parameter 'version' must not be None.")

        self.endpoint = endpoint
        self.version = version
        kwargs.setdefault("sdk_moniker", "versioning-removed/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.AsyncRetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
