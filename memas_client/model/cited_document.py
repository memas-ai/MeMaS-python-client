# coding: utf-8

"""
    MeMaS DP APIs

    This is the Data Plane APIs for MeMaS (Memory Management Service).  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: max.yu@memas.ai
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from memas_client import schemas  # noqa: F401


class CitedDocument(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            document = schemas.StrSchema
        
            @staticmethod
            def citation() -> typing.Type['Citation']:
                return Citation
            __annotations__ = {
                "document": document,
                "citation": citation,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["document"]) -> MetaOapg.properties.document: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["citation"]) -> 'Citation': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["document", "citation", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["document"]) -> typing.Union[MetaOapg.properties.document, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["citation"]) -> typing.Union['Citation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["document", "citation", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        document: typing.Union[MetaOapg.properties.document, str, schemas.Unset] = schemas.unset,
        citation: typing.Union['Citation', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CitedDocument':
        return super().__new__(
            cls,
            *_args,
            document=document,
            citation=citation,
            _configuration=_configuration,
            **kwargs,
        )

from memas_client.model.citation import Citation