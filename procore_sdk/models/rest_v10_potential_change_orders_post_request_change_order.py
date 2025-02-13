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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RestV10PotentialChangeOrdersPostRequestChangeOrder(BaseModel):
    """
    RestV10PotentialChangeOrdersPostRequestChangeOrder
    """ # noqa: E501
    commitment_change_event_id: Optional[StrictInt] = Field(default=None, description="Commitment Change Event ID")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    due_date: Optional[datetime] = Field(default=None, description="Due date")
    grand_total: Optional[StrictStr] = Field(default=None, description="Total including markup")
    invoiced_date: Optional[date] = Field(default=None, description="Invoiced date")
    number: Optional[StrictStr] = Field(default=None, description="Number")
    origin_data: Optional[StrictStr] = Field(default=None, description="Origin data")
    origin_id: Optional[StrictStr] = Field(default=None, description="Origin ID")
    paid_date: Optional[date] = Field(default=None, description="Paid date")
    prime_change_event_id: Optional[StrictInt] = Field(default=None, description="Prime Contract Change Event ID")
    schedule_impact_amount: Optional[StrictInt] = Field(default=None, description="Schedule impact in days")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    __properties: ClassVar[List[str]] = ["commitment_change_event_id", "description", "due_date", "grand_total", "invoiced_date", "number", "origin_data", "origin_id", "paid_date", "prime_change_event_id", "schedule_impact_amount", "status", "title"]

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
        """Create an instance of RestV10PotentialChangeOrdersPostRequestChangeOrder from a JSON string"""
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
        # set to None if origin_data (nullable) is None
        # and model_fields_set contains the field
        if self.origin_data is None and "origin_data" in self.model_fields_set:
            _dict['origin_data'] = None

        # set to None if origin_id (nullable) is None
        # and model_fields_set contains the field
        if self.origin_id is None and "origin_id" in self.model_fields_set:
            _dict['origin_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10PotentialChangeOrdersPostRequestChangeOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "commitment_change_event_id": obj.get("commitment_change_event_id"),
            "description": obj.get("description"),
            "due_date": obj.get("due_date"),
            "grand_total": obj.get("grand_total"),
            "invoiced_date": obj.get("invoiced_date"),
            "number": obj.get("number"),
            "origin_data": obj.get("origin_data"),
            "origin_id": obj.get("origin_id"),
            "paid_date": obj.get("paid_date"),
            "prime_change_event_id": obj.get("prime_change_event_id"),
            "schedule_impact_amount": obj.get("schedule_impact_amount"),
            "status": obj.get("status"),
            "title": obj.get("title")
        })
        return _obj


