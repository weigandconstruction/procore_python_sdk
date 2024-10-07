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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.location2 import Location2
from procore_sdk.models.rest_v10_projects_project_id_notes_logs_get200_response_inner_attachments_inner import RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get200_response_inner_custom_fields import RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get200_response_inner_permissions import RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdNotesLogsGet200ResponseInner(BaseModel):
    """
    RestV10ProjectsProjectIdNotesLogsGet200ResponseInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    comment: Optional[StrictStr] = Field(default=None, description="Additional comments")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    var_date: Optional[date] = Field(default=None, description="Date of record", alias="date")
    datetime: Optional[datetime] = Field(default=None, description="Estimated UTC datetime of record")
    daily_log_header_id: Optional[StrictInt] = Field(default=None, description="Daily Log Header ID")
    deleted_at: Optional[datetime] = Field(default=None, description="Deleted at")
    is_issue_day: Optional[StrictBool] = Field(default=None, description="The note being added is an issue affecting the projet")
    permissions: Optional[RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions] = None
    position: Optional[StrictInt] = Field(default=None, description="Order in which this entry was recorded")
    status: Optional[StrictStr] = Field(default=None, description="Is a log pending or approved")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    created_by: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    created_by_collaborator: Optional[StrictBool] = None
    custom_fields: Optional[RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields] = None
    location: Optional[Location2] = None
    attachments: Optional[List[RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner]] = Field(default=None, description=":filename to be deprecated, use :name")
    __properties: ClassVar[List[str]] = ["id", "comment", "created_at", "date", "datetime", "daily_log_header_id", "deleted_at", "is_issue_day", "permissions", "position", "status", "updated_at", "created_by", "created_by_collaborator", "custom_fields", "location", "attachments"]

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
        """Create an instance of RestV10ProjectsProjectIdNotesLogsGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_fields
        if self.custom_fields:
            _dict['custom_fields'] = self.custom_fields.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # set to None if daily_log_header_id (nullable) is None
        # and model_fields_set contains the field
        if self.daily_log_header_id is None and "daily_log_header_id" in self.model_fields_set:
            _dict['daily_log_header_id'] = None

        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deleted_at'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdNotesLogsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "comment": obj.get("comment"),
            "created_at": obj.get("created_at"),
            "date": obj.get("date"),
            "datetime": obj.get("datetime"),
            "daily_log_header_id": obj.get("daily_log_header_id"),
            "deleted_at": obj.get("deleted_at"),
            "is_issue_day": obj.get("is_issue_day"),
            "permissions": RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "position": obj.get("position"),
            "status": obj.get("status"),
            "updated_at": obj.get("updated_at"),
            "created_by": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "created_by_collaborator": obj.get("created_by_collaborator"),
            "custom_fields": RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.from_dict(obj["custom_fields"]) if obj.get("custom_fields") is not None else None,
            "location": Location2.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "attachments": [RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None
        })
        return _obj


