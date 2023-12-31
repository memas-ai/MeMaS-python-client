# coding: utf-8

"""
    MeMaS DP APIs

    This is the Data Plane client for MeMaS (Memory Management Service).  See https://github.com/memas-ai/MeMaS for more details.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: max.yu@memas.ai
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "memas-client"
VERSION = "0.1.4"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi >= 14.5.14",
    "frozendict ~= 2.3.4",
    "python-dateutil >= 2.7.0, < 3.0.0",
    "setuptools >= 21.0.0",
    "typing_extensions >= 4.3.0",
    "urllib3 ~= 1.26.7",
]

setup(
    name=NAME,
    version=VERSION,
    description="MeMaS DP APIs",
    author="OpenAPI Generator community",
    author_email="max.yu@memas.ai",
    url="https://github.com/memas-ai/MeMaS-python-client",
    keywords=["OpenAPI", "OpenAPI-Generator", "MeMaS DP APIs"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    This is the Data Plane client for MeMaS (Memory Management Service).  See https://github.com/memas-ai/MeMaS for more details.  # noqa: E501
    """
)
