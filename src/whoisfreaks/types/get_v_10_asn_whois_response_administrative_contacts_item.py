# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetV10AsnWhoisResponseAdministrativeContactsItem(UniversalBaseModel):
    handle: typing.Optional[str] = None
    name: typing.Optional[str] = None
    address: typing.Optional[typing.List[str]] = None
    street: typing.Optional[str] = None
    city: typing.Optional[str] = None
    state: typing.Optional[str] = None
    zip_code: typing.Optional[str] = None
    country: typing.Optional[str] = None
    mnt_by: typing.Optional[typing.List[str]] = None
    date_created: typing.Optional[str] = None
    date_updated: typing.Optional[str] = None
    source: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
