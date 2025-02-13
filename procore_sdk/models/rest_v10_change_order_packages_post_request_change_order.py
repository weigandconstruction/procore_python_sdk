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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RestV10ChangeOrderPackagesPostRequestChangeOrder(BaseModel):
    """
    RestV10ChangeOrderPackagesPostRequestChangeOrder
    """ # noqa: E501
    status: Optional[StrictStr] = Field(default=None, description="Status")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    grand_total: Optional[StrictStr] = Field(default=None, description="Total including markup")
    schedule_impact_amount: Optional[StrictInt] = Field(default=None, description="Schedule impact in days")
    origin_code: Optional[StrictStr] = Field(default=None, description="Origin code")
    origin_data: Optional[StrictStr] = Field(default=None, description="Origin data")
    origin_id: Optional[StrictStr] = Field(default=None, description="Origin ID")
    paid_date: Optional[date] = Field(default=None, description="Paid date")
    invoiced_date: Optional[date] = Field(default=None, description="Invoiced date")
    due_date: Optional[date] = Field(default=None, description="Due date")
    executed: Optional[StrictBool] = Field(default=None, description="Executed")
    signed_change_order_received_date: Optional[date] = Field(default=None, description="Signed change order received date")
    __properties: ClassVar[List[str]] = ["status", "title", "description", "grand_total", "schedule_impact_amount", "origin_code", "origin_data", "origin_id", "paid_date", "invoiced_date", "due_date", "executed", "signed_change_order_received_date"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['draft', 'not_pricing', 'pricing', 'pending', 'revised', 'proceeding', 'not_proceeding', 'no_charge', 'approved', 'rejected', 'void']):
            raise ValueError("must be one of enum values ('draft', 'not_pricing', 'pricing', 'pending', 'revised', 'proceeding', 'not_proceeding', 'no_charge', 'approved', 'rejected', 'void')")
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
        """Create an instance of RestV10ChangeOrderPackagesPostRequestChangeOrder from a JSON string"""
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
        """Create an instance of RestV10ChangeOrderPackagesPostRequestChangeOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "grand_total": obj.get("grand_total"),
            "schedule_impact_amount": obj.get("schedule_impact_amount"),
            "origin_code": obj.get("origin_code"),
            "origin_data": obj.get("origin_data"),
            "origin_id": obj.get("origin_id"),
            "paid_date": obj.get("paid_date"),
            "invoiced_date": obj.get("invoiced_date"),
            "due_date": obj.get("due_date"),
            "executed": obj.get("executed"),
            "signed_change_order_received_date": obj.get("signed_change_order_received_date")
        })
        return _obj


