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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.array_of_task_items_that_were_sent_out_inner_all_of_assignee import ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee
from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner_attachments_inner import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner
from procore_sdk.models.rest_v11_projects_project_id_submittals_get200_response_inner_approvers_inner_response import RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse
from typing import Optional, Set
from typing_extensions import Self

class RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner(BaseModel):
    """
    RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner
    """ # noqa: E501
    approver_type: Optional[StrictStr] = Field(default=None, description="Role of Approver")
    comment: Optional[StrictStr] = None
    distributed: Optional[StrictBool] = None
    response: Optional[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse] = None
    returned_date: Optional[date] = Field(default=None, description="Returned Date")
    sent_date: Optional[date] = Field(default=None, description="Sent Date")
    due_date: Optional[date] = Field(default=None, description="Due Date")
    response_required: Optional[StrictBool] = None
    user: Optional[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee] = None
    attachments: Optional[List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]] = Field(default=None, description="Attachments")
    submittal_associated_attachment_ids: Optional[List[StrictInt]] = Field(default=None, description="Submittal Associated Attachment IDs")
    id: Optional[StrictInt] = Field(default=None, description="ID")
    __properties: ClassVar[List[str]] = ["approver_type", "comment", "distributed", "response", "returned_date", "sent_date", "due_date", "response_required", "user", "attachments", "submittal_associated_attachment_ids", "id"]

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
        """Create an instance of RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of response
        if self.response:
            _dict['response'] = self.response.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
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
        """Create an instance of RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "approver_type": obj.get("approver_type"),
            "comment": obj.get("comment"),
            "distributed": obj.get("distributed"),
            "response": RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse.from_dict(obj["response"]) if obj.get("response") is not None else None,
            "returned_date": obj.get("returned_date"),
            "sent_date": obj.get("sent_date"),
            "due_date": obj.get("due_date"),
            "response_required": obj.get("response_required"),
            "user": ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "attachments": [RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "submittal_associated_attachment_ids": obj.get("submittal_associated_attachment_ids"),
            "id": obj.get("id")
        })
        return _obj


