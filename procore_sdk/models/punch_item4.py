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
from procore_sdk.models.work_order_contract_custom_field_custom_field_definition_id import WorkOrderContractCustomFieldCustomFieldDefinitionId
from typing import Optional, Set
from typing_extensions import Self

class PunchItem4(BaseModel):
    """
    PunchItem4
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description")
    due: Optional[date] = Field(default=None, description="Due date")
    name: StrictStr = Field(description="Name")
    schedule_risk: Optional[StrictStr] = Field(default=None, description="Assessed risk level of on-time completion")
    position: Optional[StrictInt] = Field(default=None, description="Position")
    priority: Optional[StrictStr] = Field(default=None, description="Punch item priority - 'low', 'medium', 'high'")
    private: Optional[StrictBool] = Field(default=None, description="Privacy status")
    status: Optional[StrictStr] = Field(default=None, description="Status - 'open' or 'closed'")
    date_initiated: Optional[date] = Field(default=None, description="Date created")
    schedule_impact: Optional[StrictStr] = Field(default=None, description="Schedule impact status - yes_known, yes_unknown, no_impact, tbd, n_a")
    schedule_impact_days: Optional[StrictInt] = Field(default=None, description="Schedule impact value in days")
    reference: Optional[StrictStr] = Field(default=None, description="Used to create a reference point between a punch item within Procore and a corresponding punch item outside of Procore")
    cost_impact: Optional[StrictStr] = Field(default=None, description="Cost impact status - yes_known, yes_unknown, no_impact, tbd, n_a")
    cost_impact_amount: Optional[StrictInt] = Field(default=None, description="Cost impact amount")
    trade_id: Optional[StrictInt] = Field(default=None, description="Trade ID")
    punch_item_type_id: Optional[StrictInt] = Field(default=None, description="Punch Item Type ID")
    login_information_ids: Optional[List[StrictInt]] = Field(default=None, description="Array of the User IDs of the Punch Item Assignments")
    distribution_member_ids: Optional[List[StrictInt]] = Field(default=None, description="Array of the User IDs of the Distribution Members")
    punch_item_manager_id: Optional[StrictInt] = Field(default=None, description="Punch Item Manager ID")
    final_approver_id: Optional[StrictInt] = Field(default=None, description="Punch Item Final Approver ID")
    location_id: Optional[StrictInt] = Field(default=None, description="The ID of the Location of the Punch Item. `location_id` takes precedence over `mt_location`")
    mt_location: Optional[List[StrictStr]] = Field(default=None, description="Use this for creating a new multi-tier or single-tier Location. This will be ignored if `location_id` is provided.")
    workflow_status: Optional[StrictStr] = Field(default=None, description="Workflow status of the Punch Item. These are more granular statuses in the punch item workflow.")
    drawing_revision_ids: Optional[List[StrictInt]] = Field(default=None, description="Drawing Revisions to attach to the response")
    file_version_ids: Optional[List[StrictInt]] = Field(default=None, description="File Versions to attach to the response")
    form_ids: Optional[List[StrictInt]] = Field(default=None, description="Forms to attach to the response")
    image_ids: Optional[List[StrictInt]] = Field(default=None, description="Images to attach to the response")
    upload_ids: Optional[List[StrictStr]] = Field(default=None, description="Uploads to attach to the response")
    custom_field_custom_field_definition_id: Optional[WorkOrderContractCustomFieldCustomFieldDefinitionId] = Field(default=None, alias="custom_field_%{custom_field_definition_id}")
    __properties: ClassVar[List[str]] = ["description", "due", "name", "schedule_risk", "position", "priority", "private", "status", "date_initiated", "schedule_impact", "schedule_impact_days", "reference", "cost_impact", "cost_impact_amount", "trade_id", "punch_item_type_id", "login_information_ids", "distribution_member_ids", "punch_item_manager_id", "final_approver_id", "location_id", "mt_location", "workflow_status", "drawing_revision_ids", "file_version_ids", "form_ids", "image_ids", "upload_ids", "custom_field_%{custom_field_definition_id}"]

    @field_validator('schedule_risk')
    def schedule_risk_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ml_low', 'ml_medium', 'ml_high']):
            raise ValueError("must be one of enum values ('ml_low', 'ml_medium', 'ml_high')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['open', 'closed']):
            raise ValueError("must be one of enum values ('open', 'closed')")
        return value

    @field_validator('workflow_status')
    def workflow_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['draft', 'initiated', 'in_dispute', 'work_required', 'ready_for_review', 'work_not_accepted', 'ready_to_close', 'not_accepted_by_creator', 'closed']):
            raise ValueError("must be one of enum values ('draft', 'initiated', 'in_dispute', 'work_required', 'ready_for_review', 'work_not_accepted', 'ready_to_close', 'not_accepted_by_creator', 'closed')")
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
        """Create an instance of PunchItem4 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_field_custom_field_definition_id
        if self.custom_field_custom_field_definition_id:
            _dict['custom_field_%{custom_field_definition_id}'] = self.custom_field_custom_field_definition_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PunchItem4 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "due": obj.get("due"),
            "name": obj.get("name"),
            "schedule_risk": obj.get("schedule_risk"),
            "position": obj.get("position"),
            "priority": obj.get("priority"),
            "private": obj.get("private"),
            "status": obj.get("status"),
            "date_initiated": obj.get("date_initiated"),
            "schedule_impact": obj.get("schedule_impact"),
            "schedule_impact_days": obj.get("schedule_impact_days"),
            "reference": obj.get("reference"),
            "cost_impact": obj.get("cost_impact"),
            "cost_impact_amount": obj.get("cost_impact_amount"),
            "trade_id": obj.get("trade_id"),
            "punch_item_type_id": obj.get("punch_item_type_id"),
            "login_information_ids": obj.get("login_information_ids"),
            "distribution_member_ids": obj.get("distribution_member_ids"),
            "punch_item_manager_id": obj.get("punch_item_manager_id"),
            "final_approver_id": obj.get("final_approver_id"),
            "location_id": obj.get("location_id"),
            "mt_location": obj.get("mt_location"),
            "workflow_status": obj.get("workflow_status"),
            "drawing_revision_ids": obj.get("drawing_revision_ids"),
            "file_version_ids": obj.get("file_version_ids"),
            "form_ids": obj.get("form_ids"),
            "image_ids": obj.get("image_ids"),
            "upload_ids": obj.get("upload_ids"),
            "custom_field_%{custom_field_definition_id}": WorkOrderContractCustomFieldCustomFieldDefinitionId.from_dict(obj["custom_field_%{custom_field_definition_id}"]) if obj.get("custom_field_%{custom_field_definition_id}") is not None else None
        })
        return _obj


