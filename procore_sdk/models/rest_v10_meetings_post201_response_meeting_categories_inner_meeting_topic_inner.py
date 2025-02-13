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
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_attachments_inner import RestV10WorkOrderContractsPost201ResponseAttachmentsInner
from procore_sdk.models.rest_v11_projects_project_id_meetings_post201_response_meeting_categories_inner_meeting_topic_inner_meeting_category import RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInnerMeetingCategory
from typing import Optional, Set
from typing_extensions import Self

class RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner(BaseModel):
    """
    Meeting topic
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Meeting topic id")
    number: Optional[StrictStr] = Field(default=None, description="Meeting topic number")
    created_on: Optional[date] = Field(default=None, description="Meeting topic created on")
    position: Optional[StrictInt] = Field(default=None, description="Meeting topic position")
    due_date: Optional[date] = Field(default=None, description="Meeting topic due date")
    priority: Optional[StrictStr] = Field(default=None, description="Meeting topic priority")
    status: Optional[StrictStr] = Field(default=None, description="Meeting topic status")
    title: Optional[StrictStr] = Field(default=None, description="Meeting topic title")
    minutes: Optional[StrictStr] = Field(default=None, description="Meeting topic minutes")
    description: Optional[StrictStr] = Field(default=None, description="Meeting topic description")
    meeting_category: Optional[RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInnerMeetingCategory] = None
    assignments: Optional[List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]] = Field(default=None, description="Meeting topic assignments")
    attachments: Optional[List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]] = Field(default=None, description="Meeting topic attachments")
    __properties: ClassVar[List[str]] = ["id", "number", "created_on", "position", "due_date", "priority", "status", "title", "minutes", "description", "meeting_category", "assignments", "attachments"]

    @field_validator('priority')
    def priority_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['', 'High', 'Medium', 'Low']):
            raise ValueError("must be one of enum values ('', 'High', 'Medium', 'Low')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Open', 'On Hold', 'Closed']):
            raise ValueError("must be one of enum values ('Open', 'On Hold', 'Closed')")
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
        """Create an instance of RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of meeting_category
        if self.meeting_category:
            _dict['meeting_category'] = self.meeting_category.to_dict()
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "number": obj.get("number"),
            "created_on": obj.get("created_on"),
            "position": obj.get("position"),
            "due_date": obj.get("due_date"),
            "priority": obj.get("priority"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "minutes": obj.get("minutes"),
            "description": obj.get("description"),
            "meeting_category": RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInnerMeetingCategory.from_dict(obj["meeting_category"]) if obj.get("meeting_category") is not None else None,
            "assignments": [RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(_item) for _item in obj["assignments"]] if obj.get("assignments") is not None else None,
            "attachments": [RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None
        })
        return _obj


