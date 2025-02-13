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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_attachments_inner import RestV10WorkOrderContractsPost201ResponseAttachmentsInner
from procore_sdk.models.rest_v11_projects_project_id_meetings_post201_response_attendees_inner import RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner
from procore_sdk.models.rest_v11_projects_project_id_meetings_post201_response_meeting_categories_inner import RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner
from typing import Optional, Set
from typing_extensions import Self

class RestV11ProjectsProjectIdMeetingsPost201Response(BaseModel):
    """
    Meeting
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Meeting id")
    meeting_template_id: Optional[StrictInt] = Field(default=None, description="Meeting Template id")
    position: Optional[StrictInt] = Field(default=None, description="Meeting position")
    created_by_id: Optional[StrictInt] = Field(default=None, description="Id of the user who created the meeting (returned only for meetings created after Dec 2023)")
    title: Optional[StrictStr] = Field(default=None, description="Meeting title")
    location: Optional[StrictStr] = Field(default=None, description="Meeting location")
    occurred: Optional[StrictBool] = Field(default=None, description="Meeting occurred status")
    starts_at: Optional[datetime] = Field(default=None, description="Meeting start time")
    ends_at: Optional[datetime] = Field(default=None, description="Meeting finish time")
    time_zone: Optional[StrictStr] = Field(default=None, description="Meeting Timezone")
    is_private: Optional[StrictBool] = Field(default=None, description="Meeting private status")
    is_draft: Optional[StrictBool] = Field(default=None, description="Meeting draft status")
    mode: Optional[StrictStr] = Field(default=None, description="Meeting mode")
    created_at: Optional[datetime] = Field(default=None, description="Meeting created at")
    updated_at: Optional[datetime] = Field(default=None, description="Meeting updated at")
    description: Optional[StrictStr] = Field(default=None, description="Meeting description")
    conclusion: Optional[StrictStr] = Field(default=None, description="Meeting conclusion")
    remote_meeting_url: Optional[StrictStr] = Field(default=None, description="Url to join remote meeting")
    attachments: Optional[List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]] = Field(default=None, description="Meeting attachments")
    attendees: Optional[List[RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner]] = Field(default=None, description="Meeting attendees")
    meeting_categories: Optional[List[RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner]] = Field(default=None, description="Meeting categories")
    __properties: ClassVar[List[str]] = ["id", "meeting_template_id", "position", "created_by_id", "title", "location", "occurred", "starts_at", "ends_at", "time_zone", "is_private", "is_draft", "mode", "created_at", "updated_at", "description", "conclusion", "remote_meeting_url", "attachments", "attendees", "meeting_categories"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['minutes', 'agenda']):
            raise ValueError("must be one of enum values ('minutes', 'agenda')")
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
        """Create an instance of RestV11ProjectsProjectIdMeetingsPost201Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attendees (list)
        _items = []
        if self.attendees:
            for _item_attendees in self.attendees:
                if _item_attendees:
                    _items.append(_item_attendees.to_dict())
            _dict['attendees'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in meeting_categories (list)
        _items = []
        if self.meeting_categories:
            for _item_meeting_categories in self.meeting_categories:
                if _item_meeting_categories:
                    _items.append(_item_meeting_categories.to_dict())
            _dict['meeting_categories'] = _items
        # set to None if meeting_template_id (nullable) is None
        # and model_fields_set contains the field
        if self.meeting_template_id is None and "meeting_template_id" in self.model_fields_set:
            _dict['meeting_template_id'] = None

        # set to None if created_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.created_by_id is None and "created_by_id" in self.model_fields_set:
            _dict['created_by_id'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if remote_meeting_url (nullable) is None
        # and model_fields_set contains the field
        if self.remote_meeting_url is None and "remote_meeting_url" in self.model_fields_set:
            _dict['remote_meeting_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV11ProjectsProjectIdMeetingsPost201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "meeting_template_id": obj.get("meeting_template_id"),
            "position": obj.get("position"),
            "created_by_id": obj.get("created_by_id"),
            "title": obj.get("title"),
            "location": obj.get("location"),
            "occurred": obj.get("occurred"),
            "starts_at": obj.get("starts_at"),
            "ends_at": obj.get("ends_at"),
            "time_zone": obj.get("time_zone"),
            "is_private": obj.get("is_private"),
            "is_draft": obj.get("is_draft"),
            "mode": obj.get("mode"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "description": obj.get("description"),
            "conclusion": obj.get("conclusion"),
            "remote_meeting_url": obj.get("remote_meeting_url"),
            "attachments": [RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "attendees": [RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner.from_dict(_item) for _item in obj["attendees"]] if obj.get("attendees") is not None else None,
            "meeting_categories": [RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner.from_dict(_item) for _item in obj["meeting_categories"]] if obj.get("meeting_categories") is not None else None
        })
        return _obj


