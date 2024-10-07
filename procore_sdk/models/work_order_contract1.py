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

class WorkOrderContract1(BaseModel):
    """
    Work Order Contract object
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    accounting_method: Optional[StrictStr] = Field(default=None, description="Accounting method")
    actual_completion_date: Optional[date] = Field(default=None, description="Actual completion date")
    approval_letter_date: Optional[StrictStr] = Field(default=None, description="Approval letter date")
    contract_date: Optional[date] = Field(default=None, description="Contract date")
    contract_estimated_completion_date: Optional[date] = Field(default=None, description="Estimated completion date")
    contract_start_date: Optional[date] = Field(default=None, description="Start Date")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    exclusions: Optional[StrictStr] = Field(default=None, description="Exclusions")
    executed: Optional[StrictBool] = Field(default=False, description="Executed (or not)")
    execution_date: Optional[date] = Field(default=None, description="Execution date")
    inclusions: Optional[StrictStr] = Field(default=None, description="Inclusions")
    issued_on_date: Optional[date] = Field(default=None, description="Issued on date")
    letter_of_intent_date: Optional[date] = Field(default=None, description="Letter of intent date")
    origin_code: Optional[StrictStr] = Field(default=None, description="Origin code")
    origin_data: Optional[StrictStr] = Field(default=None, description="Origin Data")
    origin_id: Optional[StrictStr] = Field(default=None, description="Origin ID")
    number: Optional[StrictStr] = Field(default=None, description="Number")
    private: Optional[StrictBool] = Field(default=None, description="If true, visible to admins and whitelisted accessors; otherwise visible to those with read only access.")
    retainage_percent: Optional[StrictStr] = Field(default=None, description="Retainage percent")
    returned_date: Optional[date] = Field(default=None, description="Returned date")
    signed_contract_received_date: Optional[date] = Field(default=None, description="Signed contract received date")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    vendor_id: Optional[StrictInt] = Field(default=None, description="Vendor ID")
    __properties: ClassVar[List[str]] = ["id", "accounting_method", "actual_completion_date", "approval_letter_date", "contract_date", "contract_estimated_completion_date", "contract_start_date", "description", "exclusions", "executed", "execution_date", "inclusions", "issued_on_date", "letter_of_intent_date", "origin_code", "origin_data", "origin_id", "number", "private", "retainage_percent", "returned_date", "signed_contract_received_date", "status", "title", "vendor_id"]

    @field_validator('accounting_method')
    def accounting_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['amount', 'unit']):
            raise ValueError("must be one of enum values ('amount', 'unit')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Draft', 'Out For Bid', 'Out For Signature', 'Approved', 'Complete', 'Terminated', 'Void']):
            raise ValueError("must be one of enum values ('Draft', 'Out For Bid', 'Out For Signature', 'Approved', 'Complete', 'Terminated', 'Void')")
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
        """Create an instance of WorkOrderContract1 from a JSON string"""
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
        """Create an instance of WorkOrderContract1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "accounting_method": obj.get("accounting_method"),
            "actual_completion_date": obj.get("actual_completion_date"),
            "approval_letter_date": obj.get("approval_letter_date"),
            "contract_date": obj.get("contract_date"),
            "contract_estimated_completion_date": obj.get("contract_estimated_completion_date"),
            "contract_start_date": obj.get("contract_start_date"),
            "description": obj.get("description"),
            "exclusions": obj.get("exclusions"),
            "executed": obj.get("executed") if obj.get("executed") is not None else False,
            "execution_date": obj.get("execution_date"),
            "inclusions": obj.get("inclusions"),
            "issued_on_date": obj.get("issued_on_date"),
            "letter_of_intent_date": obj.get("letter_of_intent_date"),
            "origin_code": obj.get("origin_code"),
            "origin_data": obj.get("origin_data"),
            "origin_id": obj.get("origin_id"),
            "number": obj.get("number"),
            "private": obj.get("private"),
            "retainage_percent": obj.get("retainage_percent"),
            "returned_date": obj.get("returned_date"),
            "signed_contract_received_date": obj.get("signed_contract_received_date"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "vendor_id": obj.get("vendor_id")
        })
        return _obj


