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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner_attachments_inner import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdPlanRevisionLogsGet200ResponseInner(BaseModel):
    """
    RestV10ProjectsProjectIdPlanRevisionLogsGet200ResponseInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    category: Optional[StrictStr] = Field(default=None, description="Category of discipline that appears on the revision")
    comments: Optional[StrictStr] = Field(default=None, description="Additional comments")
    var_date: Optional[date] = Field(default=None, description="Date of record", alias="date")
    datetime: Optional[datetime] = Field(default=None, description="Estimated UTC datetime of record")
    deleted_at: Optional[datetime] = Field(default=None, description="Deleted at")
    plan_number: Optional[StrictStr] = Field(default=None, description="Number that appears on the plan submitted")
    position: Optional[StrictInt] = Field(default=None, description="Order in which this entry was recorded for the day")
    revision: Optional[StrictStr] = Field(default=None, description="Revision number")
    title: Optional[StrictStr] = Field(default=None, description="Title of the plans")
    created_by: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    attachments: Optional[List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]] = Field(default=None, description="Plan Revision Log Attachments are not viewable or used on web")
    __properties: ClassVar[List[str]] = ["id", "category", "comments", "date", "datetime", "deleted_at", "plan_number", "position", "revision", "title", "created_by", "attachments"]

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
        """Create an instance of RestV10ProjectsProjectIdPlanRevisionLogsGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
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
        """Create an instance of RestV10ProjectsProjectIdPlanRevisionLogsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "category": obj.get("category"),
            "comments": obj.get("comments"),
            "date": obj.get("date"),
            "datetime": obj.get("datetime"),
            "deleted_at": obj.get("deleted_at"),
            "plan_number": obj.get("plan_number"),
            "position": obj.get("position"),
            "revision": obj.get("revision"),
            "title": obj.get("title"),
            "created_by": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "attachments": [RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None
        })
        return _obj


