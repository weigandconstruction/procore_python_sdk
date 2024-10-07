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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DirectCostItem2(BaseModel):
    """
    Direct Cost Item object
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description")
    direct_cost_date: Optional[date] = Field(default=None, description="Date")
    employee_id: Optional[StrictInt] = Field(default=None, description="ID of the Employee tied to the Direct Cost Item")
    invoice_number: StrictStr = Field(description="Unique identifier for a Direct Cost Item of type invoice. Is required only if `direct_cost_type` is set to `invoice`.")
    origin_data: Optional[StrictStr] = Field(default=None, description="Origin Data")
    origin_id: Optional[StrictStr] = Field(default=None, description="Origin ID")
    payment_date: Optional[date] = Field(default=None, description="Payment Date")
    received_date: Optional[date] = Field(default=None, description="Received Date")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    terms: Optional[StrictStr] = Field(default=None, description="The agreed upon Terms for the date of payment")
    vendor_id: StrictInt = Field(description="Vendor ID")
    direct_cost_type: StrictStr = Field(description="Type")
    __properties: ClassVar[List[str]] = ["description", "direct_cost_date", "employee_id", "invoice_number", "origin_data", "origin_id", "payment_date", "received_date", "status", "terms", "vendor_id", "direct_cost_type"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['draft', 'pending', 'revise_and_resubmit', 'approved']):
            raise ValueError("must be one of enum values ('draft', 'pending', 'revise_and_resubmit', 'approved')")
        return value

    @field_validator('direct_cost_type')
    def direct_cost_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['invoice', 'expense', 'payroll']):
            raise ValueError("must be one of enum values ('invoice', 'expense', 'payroll')")
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
        """Create an instance of DirectCostItem2 from a JSON string"""
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
        """Create an instance of DirectCostItem2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "direct_cost_date": obj.get("direct_cost_date"),
            "employee_id": obj.get("employee_id"),
            "invoice_number": obj.get("invoice_number"),
            "origin_data": obj.get("origin_data"),
            "origin_id": obj.get("origin_id"),
            "payment_date": obj.get("payment_date"),
            "received_date": obj.get("received_date"),
            "status": obj.get("status"),
            "terms": obj.get("terms"),
            "vendor_id": obj.get("vendor_id"),
            "direct_cost_type": obj.get("direct_cost_type")
        })
        return _obj


