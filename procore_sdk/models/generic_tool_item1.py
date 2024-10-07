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
from procore_sdk.models.compact import Compact
from procore_sdk.models.generic_tool_item1_cost_impact import GenericToolItem1CostImpact
from procore_sdk.models.generic_tool_item1_created_by import GenericToolItem1CreatedBy
from procore_sdk.models.generic_tool_item1_schedule_impact import GenericToolItem1ScheduleImpact
from procore_sdk.models.generic_tool_item_tasks_inner import GenericToolItemTasksInner
from procore_sdk.models.location1 import Location1
from procore_sdk.models.rest_v10_companies_company_id_generic_tools_generic_tool_id_patch200_response import RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get200_response_inner_custom_fields import RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields
from procore_sdk.models.rest_v10_specification_sections_get200_response_inner import RestV10SpecificationSectionsGet200ResponseInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_attachments_inner import RestV10WorkOrderContractsPost201ResponseAttachmentsInner
from procore_sdk.models.sub_job1 import SubJob1
from procore_sdk.models.trade import Trade
from typing import Optional, Set
from typing_extensions import Self

class GenericToolItem1(BaseModel):
    """
    Generic Tool Item
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the Generic Tool Item")
    closed_at: Optional[datetime] = Field(default=None, description="Generic Tool Item closed at")
    created_at: Optional[datetime] = Field(default=None, description="Generic Tool Item created at")
    description: Optional[StrictStr] = Field(default=None, description="Description of a Generic Tool Item")
    due_date: Optional[date] = Field(default=None, description="Generic Tool Item Due Date")
    issued_at: Optional[datetime] = Field(default=None, description="Generic Tool Item issued at")
    origin_generic_tool_item_id: Optional[StrictInt] = Field(default=None, description="Origin Generic Tool Item ID")
    origin_rfi_id: Optional[StrictInt] = Field(default=None, description="Origin RFI ID")
    position: Optional[StrictStr] = Field(default=None, description="The Number of the Generic Tool Item")
    private: Optional[StrictBool] = Field(default=None, description="If the Generic Tool Item is private")
    schedule_impact: Optional[GenericToolItem1ScheduleImpact] = None
    cost_impact: Optional[GenericToolItem1CostImpact] = None
    updated_at: Optional[datetime] = Field(default=None, description="Generic Tool Item updated at")
    status: Optional[StrictStr] = Field(default=None, description="Status of the Generic Tool Item")
    status_type: Optional[StrictStr] = Field(default=None, description="The default status the Generic Tool Item's status is mapped to.")
    title: Optional[StrictStr] = Field(default=None, description="Title of the Generic Tool Item")
    created_by: Optional[GenericToolItem1CreatedBy] = None
    received_from: Optional[GenericToolItem1CreatedBy] = None
    location: Optional[Location1] = None
    cost_code: Optional[Compact] = None
    specification_section: Optional[RestV10SpecificationSectionsGet200ResponseInner] = None
    trade: Optional[Trade] = None
    trades: Optional[List[Optional[Trade]]] = Field(default=None, description="Trades")
    tasks: Optional[List[GenericToolItemTasksInner]] = Field(default=None, description="Tasks")
    sub_job: Optional[SubJob1] = None
    generic_tool: Optional[RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response] = None
    attachments: Optional[List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]] = Field(default=None, description="Attachments")
    document_management_document_revision_ids: Optional[List[StrictStr]] = Field(default=None, description="PDM document revision IDs")
    distribution_members: Optional[List[GenericToolItem1CreatedBy]] = Field(default=None, description="Distribution Members")
    assignees: Optional[List[GenericToolItem1CreatedBy]] = Field(default=None, description="Assignees")
    custom_fields: Optional[RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields] = None
    __properties: ClassVar[List[str]] = ["id", "closed_at", "created_at", "description", "due_date", "issued_at", "origin_generic_tool_item_id", "origin_rfi_id", "position", "private", "schedule_impact", "cost_impact", "updated_at", "status", "status_type", "title", "created_by", "received_from", "location", "cost_code", "specification_section", "trade", "trades", "tasks", "sub_job", "generic_tool", "attachments", "document_management_document_revision_ids", "distribution_members", "assignees", "custom_fields"]

    @field_validator('status_type')
    def status_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Open', 'Closed', 'Draft']):
            raise ValueError("must be one of enum values ('Open', 'Closed', 'Draft')")
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
        """Create an instance of GenericToolItem1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of received_from
        if self.received_from:
            _dict['received_from'] = self.received_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cost_code
        if self.cost_code:
            _dict['cost_code'] = self.cost_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of specification_section
        if self.specification_section:
            _dict['specification_section'] = self.specification_section.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trade
        if self.trade:
            _dict['trade'] = self.trade.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in trades (list)
        _items = []
        if self.trades:
            for _item_trades in self.trades:
                if _item_trades:
                    _items.append(_item_trades.to_dict())
            _dict['trades'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tasks (list)
        _items = []
        if self.tasks:
            for _item_tasks in self.tasks:
                if _item_tasks:
                    _items.append(_item_tasks.to_dict())
            _dict['tasks'] = _items
        # override the default output from pydantic by calling `to_dict()` of sub_job
        if self.sub_job:
            _dict['sub_job'] = self.sub_job.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generic_tool
        if self.generic_tool:
            _dict['generic_tool'] = self.generic_tool.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in distribution_members (list)
        _items = []
        if self.distribution_members:
            for _item_distribution_members in self.distribution_members:
                if _item_distribution_members:
                    _items.append(_item_distribution_members.to_dict())
            _dict['distribution_members'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in assignees (list)
        _items = []
        if self.assignees:
            for _item_assignees in self.assignees:
                if _item_assignees:
                    _items.append(_item_assignees.to_dict())
            _dict['assignees'] = _items
        # override the default output from pydantic by calling `to_dict()` of custom_fields
        if self.custom_fields:
            _dict['custom_fields'] = self.custom_fields.to_dict()
        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if trade (nullable) is None
        # and model_fields_set contains the field
        if self.trade is None and "trade" in self.model_fields_set:
            _dict['trade'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GenericToolItem1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "closed_at": obj.get("closed_at"),
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "due_date": obj.get("due_date"),
            "issued_at": obj.get("issued_at"),
            "origin_generic_tool_item_id": obj.get("origin_generic_tool_item_id"),
            "origin_rfi_id": obj.get("origin_rfi_id"),
            "position": obj.get("position"),
            "private": obj.get("private"),
            "schedule_impact": GenericToolItem1ScheduleImpact.from_dict(obj["schedule_impact"]) if obj.get("schedule_impact") is not None else None,
            "cost_impact": GenericToolItem1CostImpact.from_dict(obj["cost_impact"]) if obj.get("cost_impact") is not None else None,
            "updated_at": obj.get("updated_at"),
            "status": obj.get("status"),
            "status_type": obj.get("status_type"),
            "title": obj.get("title"),
            "created_by": GenericToolItem1CreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "received_from": GenericToolItem1CreatedBy.from_dict(obj["received_from"]) if obj.get("received_from") is not None else None,
            "location": Location1.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "cost_code": Compact.from_dict(obj["cost_code"]) if obj.get("cost_code") is not None else None,
            "specification_section": RestV10SpecificationSectionsGet200ResponseInner.from_dict(obj["specification_section"]) if obj.get("specification_section") is not None else None,
            "trade": Trade.from_dict(obj["trade"]) if obj.get("trade") is not None else None,
            "trades": [Trade.from_dict(_item) for _item in obj["trades"]] if obj.get("trades") is not None else None,
            "tasks": [GenericToolItemTasksInner.from_dict(_item) for _item in obj["tasks"]] if obj.get("tasks") is not None else None,
            "sub_job": SubJob1.from_dict(obj["sub_job"]) if obj.get("sub_job") is not None else None,
            "generic_tool": RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response.from_dict(obj["generic_tool"]) if obj.get("generic_tool") is not None else None,
            "attachments": [RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "document_management_document_revision_ids": obj.get("document_management_document_revision_ids"),
            "distribution_members": [GenericToolItem1CreatedBy.from_dict(_item) for _item in obj["distribution_members"]] if obj.get("distribution_members") is not None else None,
            "assignees": [GenericToolItem1CreatedBy.from_dict(_item) for _item in obj["assignees"]] if obj.get("assignees") is not None else None,
            "custom_fields": RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.from_dict(obj["custom_fields"]) if obj.get("custom_fields") is not None else None
        })
        return _obj


