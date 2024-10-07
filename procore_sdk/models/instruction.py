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
from procore_sdk.models.instruction_cost_impact import InstructionCostImpact
from procore_sdk.models.instruction_schedule_impact import InstructionScheduleImpact
from typing import Optional, Set
from typing_extensions import Self

class Instruction(BaseModel):
    """
    Instruction
    """ # noqa: E501
    number: Optional[StrictStr] = Field(default=None, description="The Number of the Instruction")
    title: StrictStr = Field(description="The Title of the Instruction")
    status: StrictStr = Field(description="The Status of the Instruction")
    instruction_type_id: StrictInt = Field(description="ID of the Instruction Type")
    instruction_from_id: Optional[StrictInt] = Field(default=None, description="ID of the User who the Instruction is from")
    date_received: Optional[date] = None
    schedule_impact: Optional[InstructionScheduleImpact] = None
    cost_impact: Optional[InstructionCostImpact] = None
    private: Optional[StrictBool] = Field(default=False, description="The Private status of the Instruction")
    description: Optional[StrictStr] = Field(default=None, description="The Description of the Instruction")
    attention_ids: Optional[List[StrictInt]] = Field(default=None, description="An array of IDs of the Attentions of the Instruction")
    distribution_member_ids: Optional[List[StrictInt]] = Field(default=None, description="An array of IDs of the Distributions of the Instruction")
    trade_ids: Optional[List[StrictInt]] = Field(default=None, description="An array of IDs of the Trades of the Instruction")
    attachments: Optional[List[StrictStr]] = Field(default=None, description="Instruction's Attachments. To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.")
    __properties: ClassVar[List[str]] = ["number", "title", "status", "instruction_type_id", "instruction_from_id", "date_received", "schedule_impact", "cost_impact", "private", "description", "attention_ids", "distribution_member_ids", "trade_ids", "attachments"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['draft', 'issued']):
            raise ValueError("must be one of enum values ('draft', 'issued')")
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
        """Create an instance of Instruction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of schedule_impact
        if self.schedule_impact:
            _dict['schedule_impact'] = self.schedule_impact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cost_impact
        if self.cost_impact:
            _dict['cost_impact'] = self.cost_impact.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Instruction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "number": obj.get("number"),
            "title": obj.get("title"),
            "status": obj.get("status"),
            "instruction_type_id": obj.get("instruction_type_id"),
            "instruction_from_id": obj.get("instruction_from_id"),
            "date_received": obj.get("date_received"),
            "schedule_impact": InstructionScheduleImpact.from_dict(obj["schedule_impact"]) if obj.get("schedule_impact") is not None else None,
            "cost_impact": InstructionCostImpact.from_dict(obj["cost_impact"]) if obj.get("cost_impact") is not None else None,
            "private": obj.get("private") if obj.get("private") is not None else False,
            "description": obj.get("description"),
            "attention_ids": obj.get("attention_ids"),
            "distribution_member_ids": obj.get("distribution_member_ids"),
            "trade_ids": obj.get("trade_ids"),
            "attachments": obj.get("attachments")
        })
        return _obj


