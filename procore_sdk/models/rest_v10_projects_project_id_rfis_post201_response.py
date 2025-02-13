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
from procore_sdk.models.array_of_task_items_that_were_sent_out_inner_all_of_assignee import ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee
from procore_sdk.models.location import Location
from procore_sdk.models.rest_v10_projects_project_id_rfis_get200_response_inner_all_of_cost_impact import RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfCostImpact
from procore_sdk.models.rest_v10_projects_project_id_rfis_get200_response_inner_all_of_schedule_impact import RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfScheduleImpact
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response_all_of_custom_textfield1 import RestV10ProjectsProjectIdRfisPost201ResponseAllOfCustomTextfield1
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response_all_of_custom_textfield2 import RestV10ProjectsProjectIdRfisPost201ResponseAllOfCustomTextfield2
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner import RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response_all_of_specification_section import RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection
from procore_sdk.models.rest_v10_projects_project_id_waste_logs_get200_response_inner_vendor import RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_custom_fields import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields
from procore_sdk.models.timecard_entry_full_cost_code import TimecardEntryFullCostCode
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdRfisPost201Response(BaseModel):
    """
    RestV10ProjectsProjectIdRfisPost201Response
    """ # noqa: E501
    accepted: Optional[StrictBool] = Field(default=None, description="RFI Acceptance status, true means the RFI is accepted and closed")
    ball_in_court_role: Optional[StrictStr] = Field(default=None, description="Ball in Court Role (can be Assignees, Creator, or RFI Manager)")
    custom_textfield_1: Optional[RestV10ProjectsProjectIdRfisPost201ResponseAllOfCustomTextfield1] = None
    custom_textfield_2: Optional[RestV10ProjectsProjectIdRfisPost201ResponseAllOfCustomTextfield2] = None
    distribution_list: Optional[List[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee]] = Field(default=None, description="RFI Distribution List of Users")
    draft: Optional[StrictBool] = Field(default=None, description="Draft status, true if draft")
    drawing_ids: Optional[List[StrictInt]] = Field(default=None, description="Array of IDs for associated Drawings")
    drawing_number: Optional[StrictStr] = Field(default=None, description="Drawing Number")
    questions: Optional[List[RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner]] = Field(default=None, description="List of questions")
    specification_section: Optional[RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection] = None
    custom_fields: Optional[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields] = None
    id: Optional[StrictInt] = Field(default=None, description="ID")
    assignee: Optional[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee] = None
    assignees: Optional[List[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee]] = Field(default=None, description="RFI Assignees")
    ball_in_court: Optional[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee] = None
    ball_in_courts: Optional[List[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee]] = Field(default=None, description="Ball In Courts")
    cost_code: Optional[TimecardEntryFullCostCode] = None
    cost_impact: Optional[RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfCostImpact] = None
    created_at: Optional[datetime] = Field(default=None, description="Date created")
    deleted: Optional[StrictBool] = Field(default=None, description="Deleted status (this is only shown on deleted records)")
    deleted_at: Optional[datetime] = Field(default=None, description="Time deleted (this is only shown on deleted records)")
    due_date: Optional[date] = Field(default=None, description="Due Date")
    initiated_at: Optional[datetime] = Field(default=None, description="Date initiated")
    location: Optional[Location] = None
    full_number: Optional[StrictStr] = Field(default=None, description="Full Number")
    number: Optional[StrictStr] = Field(default=None, description="Number")
    prefix: Optional[StrictStr] = Field(default=None, description="Prefix")
    private: Optional[StrictBool] = Field(default=None, description="Private Status")
    received_from: Optional[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee] = None
    reference: Optional[StrictStr] = Field(default=None, description="Reference")
    responsible_contractor: Optional[RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor] = None
    rfi_manager: Optional[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee] = None
    schedule_impact: Optional[RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfScheduleImpact] = None
    status: Optional[StrictStr] = Field(default=None, description="Status")
    translated_status: Optional[StrictStr] = Field(default=None, description="Translated RFI status")
    subject: Optional[StrictStr] = Field(default=None, description="Subject")
    time_resolved: Optional[datetime] = Field(default=None, description="Time RFI was closed")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    __properties: ClassVar[List[str]] = ["accepted", "ball_in_court_role", "custom_textfield_1", "custom_textfield_2", "distribution_list", "draft", "drawing_ids", "drawing_number", "questions", "specification_section", "custom_fields", "id", "assignee", "assignees", "ball_in_court", "ball_in_courts", "cost_code", "cost_impact", "created_at", "deleted", "deleted_at", "due_date", "initiated_at", "location", "full_number", "number", "prefix", "private", "received_from", "reference", "responsible_contractor", "rfi_manager", "schedule_impact", "status", "translated_status", "subject", "time_resolved", "updated_at"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['open', 'closed', 'draft', 'recycled']):
            raise ValueError("must be one of enum values ('open', 'closed', 'draft', 'recycled')")
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
        """Create an instance of RestV10ProjectsProjectIdRfisPost201Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_textfield_1
        if self.custom_textfield_1:
            _dict['custom_textfield_1'] = self.custom_textfield_1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_textfield_2
        if self.custom_textfield_2:
            _dict['custom_textfield_2'] = self.custom_textfield_2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in distribution_list (list)
        _items = []
        if self.distribution_list:
            for _item_distribution_list in self.distribution_list:
                if _item_distribution_list:
                    _items.append(_item_distribution_list.to_dict())
            _dict['distribution_list'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in questions (list)
        _items = []
        if self.questions:
            for _item_questions in self.questions:
                if _item_questions:
                    _items.append(_item_questions.to_dict())
            _dict['questions'] = _items
        # override the default output from pydantic by calling `to_dict()` of specification_section
        if self.specification_section:
            _dict['specification_section'] = self.specification_section.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_fields
        if self.custom_fields:
            _dict['custom_fields'] = self.custom_fields.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assignee
        if self.assignee:
            _dict['assignee'] = self.assignee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in assignees (list)
        _items = []
        if self.assignees:
            for _item_assignees in self.assignees:
                if _item_assignees:
                    _items.append(_item_assignees.to_dict())
            _dict['assignees'] = _items
        # override the default output from pydantic by calling `to_dict()` of ball_in_court
        if self.ball_in_court:
            _dict['ball_in_court'] = self.ball_in_court.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ball_in_courts (list)
        _items = []
        if self.ball_in_courts:
            for _item_ball_in_courts in self.ball_in_courts:
                if _item_ball_in_courts:
                    _items.append(_item_ball_in_courts.to_dict())
            _dict['ball_in_courts'] = _items
        # override the default output from pydantic by calling `to_dict()` of cost_code
        if self.cost_code:
            _dict['cost_code'] = self.cost_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cost_impact
        if self.cost_impact:
            _dict['cost_impact'] = self.cost_impact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of received_from
        if self.received_from:
            _dict['received_from'] = self.received_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of responsible_contractor
        if self.responsible_contractor:
            _dict['responsible_contractor'] = self.responsible_contractor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rfi_manager
        if self.rfi_manager:
            _dict['rfi_manager'] = self.rfi_manager.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule_impact
        if self.schedule_impact:
            _dict['schedule_impact'] = self.schedule_impact.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdRfisPost201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accepted": obj.get("accepted"),
            "ball_in_court_role": obj.get("ball_in_court_role"),
            "custom_textfield_1": RestV10ProjectsProjectIdRfisPost201ResponseAllOfCustomTextfield1.from_dict(obj["custom_textfield_1"]) if obj.get("custom_textfield_1") is not None else None,
            "custom_textfield_2": RestV10ProjectsProjectIdRfisPost201ResponseAllOfCustomTextfield2.from_dict(obj["custom_textfield_2"]) if obj.get("custom_textfield_2") is not None else None,
            "distribution_list": [ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.from_dict(_item) for _item in obj["distribution_list"]] if obj.get("distribution_list") is not None else None,
            "draft": obj.get("draft"),
            "drawing_ids": obj.get("drawing_ids"),
            "drawing_number": obj.get("drawing_number"),
            "questions": [RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner.from_dict(_item) for _item in obj["questions"]] if obj.get("questions") is not None else None,
            "specification_section": RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection.from_dict(obj["specification_section"]) if obj.get("specification_section") is not None else None,
            "custom_fields": RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.from_dict(obj["custom_fields"]) if obj.get("custom_fields") is not None else None,
            "id": obj.get("id"),
            "assignee": ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.from_dict(obj["assignee"]) if obj.get("assignee") is not None else None,
            "assignees": [ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.from_dict(_item) for _item in obj["assignees"]] if obj.get("assignees") is not None else None,
            "ball_in_court": ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.from_dict(obj["ball_in_court"]) if obj.get("ball_in_court") is not None else None,
            "ball_in_courts": [ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.from_dict(_item) for _item in obj["ball_in_courts"]] if obj.get("ball_in_courts") is not None else None,
            "cost_code": TimecardEntryFullCostCode.from_dict(obj["cost_code"]) if obj.get("cost_code") is not None else None,
            "cost_impact": RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfCostImpact.from_dict(obj["cost_impact"]) if obj.get("cost_impact") is not None else None,
            "created_at": obj.get("created_at"),
            "deleted": obj.get("deleted"),
            "deleted_at": obj.get("deleted_at"),
            "due_date": obj.get("due_date"),
            "initiated_at": obj.get("initiated_at"),
            "location": Location.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "full_number": obj.get("full_number"),
            "number": obj.get("number"),
            "prefix": obj.get("prefix"),
            "private": obj.get("private"),
            "received_from": ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.from_dict(obj["received_from"]) if obj.get("received_from") is not None else None,
            "reference": obj.get("reference"),
            "responsible_contractor": RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.from_dict(obj["responsible_contractor"]) if obj.get("responsible_contractor") is not None else None,
            "rfi_manager": ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.from_dict(obj["rfi_manager"]) if obj.get("rfi_manager") is not None else None,
            "schedule_impact": RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfScheduleImpact.from_dict(obj["schedule_impact"]) if obj.get("schedule_impact") is not None else None,
            "status": obj.get("status"),
            "translated_status": obj.get("translated_status"),
            "subject": obj.get("subject"),
            "time_resolved": obj.get("time_resolved"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


