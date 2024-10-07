# coding: utf-8

"""
    Procore Rest API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Contact: apisupport@procore.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner_attachments_inner import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner
from typing import Optional, Set
from typing_extensions import Self

class Office1(BaseModel):
    """
    Office
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Office id")
    name: Optional[StrictStr] = Field(default=None, description="Office name")
    address: Optional[StrictStr] = Field(default=None, description="Office address")
    city: Optional[StrictStr] = Field(default=None, description="Office city")
    state_code: Optional[StrictStr] = Field(default=None, description="Office state code (ISO-3166 Alpha-2 format)")
    country_code: Optional[StrictStr] = Field(default=None, description="Office country code (ISO-3166 Alpha-2 format)")
    zip: Optional[StrictStr] = Field(default=None, description="Office zip")
    phone: Optional[StrictStr] = Field(default=None, description="Office phone")
    fax: Optional[StrictStr] = Field(default=None, description="Office fax")
    division: Optional[StrictStr] = Field(default=None, description="Office division")
    logo: Optional[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner] = None
    __properties: ClassVar[List[str]] = ["id", "name", "address", "city", "state_code", "country_code", "zip", "phone", "fax", "division", "logo"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Office1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Office1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "address": obj.get("address"),
            "city": obj.get("city"),
            "state_code": obj.get("state_code"),
            "country_code": obj.get("country_code"),
            "zip": obj.get("zip"),
            "phone": obj.get("phone"),
            "fax": obj.get("fax"),
            "division": obj.get("division"),
            "logo": RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.from_dict(obj["logo"]) if obj.get("logo") is not None else None
        })
        return _obj


