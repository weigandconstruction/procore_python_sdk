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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_comments_get200_response_inner_created_by import RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInnerCreatedBy
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_attachments_inner import RestV10WorkOrderContractsPost201ResponseAttachmentsInner
from typing import Optional, Set
from typing_extensions import Self

class RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner(BaseModel):
    """
    Normal view of task item comment
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique ID of the comment")
    comment: Optional[StrictStr] = Field(default=None, description="The actual message of the comment")
    status: Optional[StrictStr] = Field(default=None, description="The status of the task item at the time this comment was created")
    attachments: Optional[RestV10WorkOrderContractsPost201ResponseAttachmentsInner] = None
    created_by: Optional[RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInnerCreatedBy] = None
    task_item_id: Optional[StrictInt] = Field(default=None, description="The task item id associated with the comment")
    created_at: Optional[datetime] = Field(default=None, description="The UTC datetime for the creation of the resource in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="The UTC datetime for the last update of the resource in ISO 8601 format.")
    __properties: ClassVar[List[str]] = ["id", "comment", "status", "attachments", "created_by", "task_item_id", "created_at", "updated_at"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['initiated', 'in_progress', 'ready_for_review', 'closed', 'void']):
            raise ValueError("must be one of enum values ('initiated', 'in_progress', 'ready_for_review', 'closed', 'void')")
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
        """Create an instance of RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attachments
        if self.attachments:
            _dict['attachments'] = self.attachments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "comment": obj.get("comment"),
            "status": obj.get("status"),
            "attachments": RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(obj["attachments"]) if obj.get("attachments") is not None else None,
            "created_by": RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInnerCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "task_item_id": obj.get("task_item_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


