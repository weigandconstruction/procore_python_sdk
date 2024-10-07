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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.comment import Comment
from procore_sdk.models.location import Location
from procore_sdk.models.punch_item3_assignments_inner import PunchItem3AssignmentsInner
from procore_sdk.models.punch_item_ball_in_court_inner import PunchItemBallInCourtInner
from procore_sdk.models.punch_item_creator import PunchItemCreator
from procore_sdk.models.punch_item_final_approver import PunchItemFinalApprover
from procore_sdk.models.punch_item_manager import PunchItemManager
from procore_sdk.models.punch_item_type import PunchItemType
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_attachments_inner import RestV10WorkOrderContractsPost201ResponseAttachmentsInner
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_custom_fields import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields
from procore_sdk.models.timecard_entry_full_cost_code import TimecardEntryFullCostCode
from procore_sdk.models.trade2 import Trade2
from typing import Optional, Set
from typing_extensions import Self

class PunchItem3(BaseModel):
    """
    PunchItem3
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    ball_in_court: Optional[List[PunchItemBallInCourtInner]] = Field(default=None, description="Array of Users")
    comments: Optional[List[Comment]] = Field(default=None, description="Punch Item Comments")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    closed_at: Optional[datetime] = Field(default=None, description="Closed at")
    deleted_at: Optional[datetime] = Field(default=None, description="Deleted at")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    due_date: Optional[date] = Field(default=None, description="Due Date")
    name: Optional[StrictStr] = Field(default=None, description="Name")
    schedule_risk: Optional[StrictStr] = Field(default=None, description="Assessed risk level of on-time completion")
    schedule_risk_reason: Optional[StrictStr] = Field(default=None, description="Reason for assessed risk level of on-time completion")
    position: Optional[StrictInt] = Field(default=None, description="Position")
    priority: Optional[StrictStr] = Field(default=None, description="Punch item priority - 'low', 'medium', 'high'")
    private: Optional[StrictBool] = Field(default=None, description="Privacy status")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    date_initiated: Optional[date] = Field(default=None, description="Date created")
    schedule_impact: Optional[StrictStr] = Field(default=None, description="Schedule impact status")
    schedule_impact_days: Optional[StrictInt] = Field(default=None, description="Schedule impact value in days")
    reference: Optional[StrictStr] = Field(default=None, description="Used to create a reference point between a Punch Item within Procore and a corresponding Punch Item outside of Procore")
    cost_impact: Optional[StrictStr] = Field(default=None, description="Cost impact status")
    cost_impact_amount: Optional[StrictInt] = Field(default=None, description="Cost impact amount")
    can_email: Optional[StrictBool] = Field(default=None, description="Punch Item has Punch Item Assignments or distribution members to email to")
    drawing_ids: Optional[List[StrictInt]] = Field(default=None, description="Array of Drawing IDs")
    current_drawing_revision_ids: Optional[List[StrictInt]] = Field(default=None, description="Array of Current Drawing Revision IDs")
    distribution_members: Optional[List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]] = Field(default=None, description="Users on the Punch Item distribution list")
    location: Optional[Location] = None
    trade: Optional[Trade2] = None
    created_by: Optional[PunchItemCreator] = None
    punch_item_manager: Optional[PunchItemManager] = None
    final_approver: Optional[PunchItemFinalApprover] = None
    punch_item_type: Optional[PunchItemType] = None
    cost_code: Optional[TimecardEntryFullCostCode] = None
    assignments: Optional[List[PunchItem3AssignmentsInner]] = Field(default=None, description="Array of Punch Item Assignments")
    attachments: Optional[List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]] = Field(default=None, description="Array of Punch Item Attachments")
    images: Optional[List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]] = Field(default=None, description="Array of Images *DEPRECATED. Please use attachments instead")
    web_images: Optional[List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]] = Field(default=None, description="Array of photo Attachments uploaded from the web application")
    workflow_status: Optional[StrictStr] = Field(default=None, description="Workflow status of the Punch Item")
    custom_fields: Optional[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields] = None
    __properties: ClassVar[List[str]] = ["id", "ball_in_court", "comments", "created_at", "closed_at", "deleted_at", "description", "due_date", "name", "schedule_risk", "schedule_risk_reason", "position", "priority", "private", "status", "updated_at", "date_initiated", "schedule_impact", "schedule_impact_days", "reference", "cost_impact", "cost_impact_amount", "can_email", "drawing_ids", "current_drawing_revision_ids", "distribution_members", "location", "trade", "created_by", "punch_item_manager", "final_approver", "punch_item_type", "cost_code", "assignments", "attachments", "images", "web_images", "workflow_status", "custom_fields"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Open', 'Closed', 'Overdue', 'Pending']):
            raise ValueError("must be one of enum values ('Open', 'Closed', 'Overdue', 'Pending')")
        return value

    @field_validator('schedule_impact')
    def schedule_impact_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['yes_known', 'yes_unknown', 'no_impact', 'tbd', 'n_a']):
            raise ValueError("must be one of enum values ('yes_known', 'yes_unknown', 'no_impact', 'tbd', 'n_a')")
        return value

    @field_validator('cost_impact')
    def cost_impact_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['yes_known', 'yes_unknown', 'no_impact', 'tbd', 'n_a']):
            raise ValueError("must be one of enum values ('yes_known', 'yes_unknown', 'no_impact', 'tbd', 'n_a')")
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
        """Create an instance of PunchItem3 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ball_in_court (list)
        _items = []
        if self.ball_in_court:
            for _item_ball_in_court in self.ball_in_court:
                if _item_ball_in_court:
                    _items.append(_item_ball_in_court.to_dict())
            _dict['ball_in_court'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in comments (list)
        _items = []
        if self.comments:
            for _item_comments in self.comments:
                if _item_comments:
                    _items.append(_item_comments.to_dict())
            _dict['comments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in distribution_members (list)
        _items = []
        if self.distribution_members:
            for _item_distribution_members in self.distribution_members:
                if _item_distribution_members:
                    _items.append(_item_distribution_members.to_dict())
            _dict['distribution_members'] = _items
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trade
        if self.trade:
            _dict['trade'] = self.trade.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of punch_item_manager
        if self.punch_item_manager:
            _dict['punch_item_manager'] = self.punch_item_manager.to_dict()
        # override the default output from pydantic by calling `to_dict()` of final_approver
        if self.final_approver:
            _dict['final_approver'] = self.final_approver.to_dict()
        # override the default output from pydantic by calling `to_dict()` of punch_item_type
        if self.punch_item_type:
            _dict['punch_item_type'] = self.punch_item_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cost_code
        if self.cost_code:
            _dict['cost_code'] = self.cost_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in assignments (list)
        _items = []
        if self.assignments:
            for _item_assignments in self.assignments:
                if _item_assignments:
                    _items.append(_item_assignments.to_dict())
            _dict['assignments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item_images in self.images:
                if _item_images:
                    _items.append(_item_images.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in web_images (list)
        _items = []
        if self.web_images:
            for _item_web_images in self.web_images:
                if _item_web_images:
                    _items.append(_item_web_images.to_dict())
            _dict['web_images'] = _items
        # override the default output from pydantic by calling `to_dict()` of custom_fields
        if self.custom_fields:
            _dict['custom_fields'] = self.custom_fields.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PunchItem3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "ball_in_court": [PunchItemBallInCourtInner.from_dict(_item) for _item in obj["ball_in_court"]] if obj.get("ball_in_court") is not None else None,
            "comments": [Comment.from_dict(_item) for _item in obj["comments"]] if obj.get("comments") is not None else None,
            "created_at": obj.get("created_at"),
            "closed_at": obj.get("closed_at"),
            "deleted_at": obj.get("deleted_at"),
            "description": obj.get("description"),
            "due_date": obj.get("due_date"),
            "name": obj.get("name"),
            "schedule_risk": obj.get("schedule_risk"),
            "schedule_risk_reason": obj.get("schedule_risk_reason"),
            "position": obj.get("position"),
            "priority": obj.get("priority"),
            "private": obj.get("private"),
            "status": obj.get("status"),
            "updated_at": obj.get("updated_at"),
            "date_initiated": obj.get("date_initiated"),
            "schedule_impact": obj.get("schedule_impact"),
            "schedule_impact_days": obj.get("schedule_impact_days"),
            "reference": obj.get("reference"),
            "cost_impact": obj.get("cost_impact"),
            "cost_impact_amount": obj.get("cost_impact_amount"),
            "can_email": obj.get("can_email"),
            "drawing_ids": obj.get("drawing_ids"),
            "current_drawing_revision_ids": obj.get("current_drawing_revision_ids"),
            "distribution_members": [RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(_item) for _item in obj["distribution_members"]] if obj.get("distribution_members") is not None else None,
            "location": Location.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "trade": Trade2.from_dict(obj["trade"]) if obj.get("trade") is not None else None,
            "created_by": PunchItemCreator.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "punch_item_manager": PunchItemManager.from_dict(obj["punch_item_manager"]) if obj.get("punch_item_manager") is not None else None,
            "final_approver": PunchItemFinalApprover.from_dict(obj["final_approver"]) if obj.get("final_approver") is not None else None,
            "punch_item_type": PunchItemType.from_dict(obj["punch_item_type"]) if obj.get("punch_item_type") is not None else None,
            "cost_code": TimecardEntryFullCostCode.from_dict(obj["cost_code"]) if obj.get("cost_code") is not None else None,
            "assignments": [PunchItem3AssignmentsInner.from_dict(_item) for _item in obj["assignments"]] if obj.get("assignments") is not None else None,
            "attachments": [RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "images": [RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "web_images": [RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(_item) for _item in obj["web_images"]] if obj.get("web_images") is not None else None,
            "workflow_status": obj.get("workflow_status"),
            "custom_fields": RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.from_dict(obj["custom_fields"]) if obj.get("custom_fields") is not None else None
        })
        return _obj


