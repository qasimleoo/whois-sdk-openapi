# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_v_10_ip_whois_response_abuse_contacts_item import GetV10IpWhoisResponseAbuseContactsItem
from .get_v_10_ip_whois_response_inet_nums_item import GetV10IpWhoisResponseInetNumsItem
from .get_v_10_ip_whois_response_organization import GetV10IpWhoisResponseOrganization
from .get_v_10_ip_whois_response_technical_contacts_item import GetV10IpWhoisResponseTechnicalContactsItem


class GetV10IpWhoisResponse(UniversalBaseModel):
    status: typing.Optional[bool] = None
    ip_address: typing.Optional[str] = None
    query_time: typing.Optional[str] = None
    whois_server: typing.Optional[str] = None
    inet_nums: typing.Optional[typing.List[GetV10IpWhoisResponseInetNumsItem]] = None
    organization: typing.Optional[GetV10IpWhoisResponseOrganization] = None
    technical_contacts: typing.Optional[typing.List[GetV10IpWhoisResponseTechnicalContactsItem]] = None
    abuse_contacts: typing.Optional[typing.List[GetV10IpWhoisResponseAbuseContactsItem]] = None
    whois_raw_response: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
