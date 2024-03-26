# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# coding: utf-8

import os
import re
from setuptools import setup, find_packages


PACKAGE_NAME = "azure-packagemode-dataplane"
PACKAGE_PPRINT_NAME = "Azure Package Mode Data Plane"

# a-b-c => a/b/c
package_folder_path = PACKAGE_NAME.replace("-", "/")

# Version extraction inspired from 'requests'
with open(os.path.join(package_folder_path, "_version.py"), "r") as fd:
    version = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("Cannot find version information")


setup(
    name=PACKAGE_NAME,
    version=version,
    description="Microsoft {} Client Library for Python".format(PACKAGE_PPRINT_NAME),
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="MIT License",
    author="Microsoft Corporation",
    author_email="azpysdkhelp@microsoft.com",
    url="https://github.com/Azure/azure-sdk-for-python/tree/main/sdk",
    keywords="azure, azure sdk",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False,
    packages=find_packages(
        exclude=[
            "tests",
            # Exclude packages that will be covered by PEP420 or nspkg
            "azure",
            "azure.packagemode",
        ]
    ),
    include_package_data=True,
    package_data={
        "azure.packagemode.dataplane": ["py.typed"],
    },
    install_requires=[
        "msrest>=0.7.1",
        "azure-mgmt-core>=1.3.2",
    ],
    python_requires=">=3.8",
)
