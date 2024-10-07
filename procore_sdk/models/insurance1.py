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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Insurance1(BaseModel):
    """
    Insurance1
    """ # noqa: E501
    effective_date: Optional[date] = Field(default=None, description="Effective date")
    enable_expired_insurance_notifications: Optional[StrictBool] = Field(default=True, description="Enable/Disable expired insurance notifications")
    exempt: Optional[StrictBool] = Field(default=None, description="Exempt status")
    expiration_date: Optional[date] = Field(default=None, description="Expiration date")
    info_received: Optional[StrictBool] = Field(default=None, description="Information received (or not)")
    insurance_type: Optional[StrictStr] = Field(default=None, description="Insurance type")
    limit: Optional[StrictStr] = Field(default=None, description="Limit")
    name: Optional[StrictStr] = Field(default=None, description="Provider name")
    notes: Optional[StrictStr] = Field(default=None, description="Notes")
    policy_number: Optional[StrictStr] = Field(default=None, description="Policy number")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    additional_insured: Optional[StrictStr] = Field(default=None, description="Additional Individuals and/or Companies Insured")
    division_template: Optional[StrictStr] = Field(default=None, description="Division Template")
    insurance_sets: Optional[StrictStr] = Field(default=None, description="Insurance Sets")
    origin_data: Optional[StrictStr] = Field(default=None, description="Origin data")
    origin_id: Optional[StrictStr] = Field(default=None, description="Origin ID")
    __properties: ClassVar[List[str]] = ["effective_date", "enable_expired_insurance_notifications", "exempt", "expiration_date", "info_received", "insurance_type", "limit", "name", "notes", "policy_number", "status", "additional_insured", "division_template", "insurance_sets", "origin_data", "origin_id"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['compliant', 'compliant_in_progress', 'expired', 'non_compliant', 'non_compliant_in_progress', 'undecided', 'unregistered']):
            raise ValueError("must be one of enum values ('compliant', 'compliant_in_progress', 'expired', 'non_compliant', 'non_compliant_in_progress', 'undecided', 'unregistered')")
        return value

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
        """Create an instance of Insurance1 from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Insurance1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "effective_date": obj.get("effective_date"),
            "enable_expired_insurance_notifications": obj.get("enable_expired_insurance_notifications") if obj.get("enable_expired_insurance_notifications") is not None else True,
            "exempt": obj.get("exempt"),
            "expiration_date": obj.get("expiration_date"),
            "info_received": obj.get("info_received"),
            "insurance_type": obj.get("insurance_type"),
            "limit": obj.get("limit"),
            "name": obj.get("name"),
            "notes": obj.get("notes"),
            "policy_number": obj.get("policy_number"),
            "status": obj.get("status"),
            "additional_insured": obj.get("additional_insured"),
            "division_template": obj.get("division_template"),
            "insurance_sets": obj.get("insurance_sets"),
            "origin_data": obj.get("origin_data"),
            "origin_id": obj.get("origin_id")
        })
        return _obj


