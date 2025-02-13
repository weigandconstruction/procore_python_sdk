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

class Observation(BaseModel):
    """
    Item object
    """ # noqa: E501
    assignee_id: Optional[StrictInt] = Field(default=None, description="The ID of the User that will be assigned to the Observation Item")
    contributing_behavior_id: Optional[StrictInt] = Field(default=None, description="The ID of the Contributing Behavior associated to the Observation Item")
    contributing_condition_id: Optional[StrictInt] = Field(default=None, description="The ID of the Contributing Condition associated to the Observation Item")
    checklist_item_id: Optional[StrictInt] = Field(default=None, description="Sets the origin to the ID of a Checklist Item (Note: the Item's origin can either be a coordination_issue_id, checklist_list_id or incident_action_id)")
    coordination_issue_id: Optional[StrictInt] = Field(default=None, description="Sets the origin to the ID of a Coordination Issue (Note: the Item's origin can either be a coordination_issue_id, checklist_list_id or incident_action_id)")
    created_by_id: Optional[StrictInt] = Field(default=None, description="The ID of the User creating the Observation Item. Only Observations Admin Users can set the creator")
    description: Optional[StrictStr] = Field(default=None, description="The Description of the Observation Item")
    due_date: Optional[date] = Field(default=None, description="The Due Date of the Observation Item")
    hazard_id: Optional[StrictInt] = Field(default=None, description="The ID of the Hazard associated to the Observation Item")
    incident_action_id: Optional[StrictInt] = Field(default=None, description="Sets the origin to the ID of an Incident Action (Note: the Item's origin can either be a coordination_issue_id, checklist_list_id or incident_action_id)")
    name: StrictStr = Field(description="The Name of the Observation Item")
    number: Optional[StrictInt] = Field(default=None, description="The Number of the Observation Item")
    personal: Optional[StrictBool] = Field(default=None, description="The Privacy status of the Observation Item")
    priority: Optional[StrictStr] = Field(default=None, description="The Priority of the Observation Item")
    specification_section_id: Optional[StrictInt] = Field(default=None, description="The ID of the specification section to set on the Observation.")
    status: Optional[StrictStr] = Field(default=None, description="The Status of the Observation Item")
    trade_id: Optional[StrictInt] = Field(default=None, description="The ID of the Trade of the Observation Item")
    type_id: StrictInt = Field(description="The ID of the Type of the Observation Item")
    distribution_member_ids: Optional[List[StrictInt]] = Field(default=None, description="An array of the User IDs of the Observation Item distribution members")
    location_id: Optional[StrictInt] = Field(default=None, description="The ID of the Location of the Observation Item. `location_id` takes precedence over `mt_location`.")
    mt_location: Optional[List[StrictStr]] = Field(default=None, description="Use this for creating a new multi-tier or single-tier Location. This will be ignored if `location_id` is provided.")
    custom_field_custom_field_definition_id: Optional[WorkOrderContractCustomFieldCustomFieldDefinitionId] = Field(default=None, alias="custom_field_%{custom_field_definition_id}")
    drawing_revision_ids: Optional[List[StrictInt]] = Field(default=None, description="Drawing Revisions to attach to the response")
    file_version_ids: Optional[List[StrictInt]] = Field(default=None, description="File Versions to attach to the response")
    form_ids: Optional[List[StrictInt]] = Field(default=None, description="Forms to attach to the response")
    image_ids: Optional[List[StrictInt]] = Field(default=None, description="Images to attach to the response")
    upload_ids: Optional[List[StrictStr]] = Field(default=None, description="Uploads to attach to the response")
    __properties: ClassVar[List[str]] = ["assignee_id", "contributing_behavior_id", "contributing_condition_id", "checklist_item_id", "coordination_issue_id", "created_by_id", "description", "due_date", "hazard_id", "incident_action_id", "name", "number", "personal", "priority", "specification_section_id", "status", "trade_id", "type_id", "distribution_member_ids", "location_id", "mt_location", "custom_field_%{custom_field_definition_id}", "drawing_revision_ids", "file_version_ids", "form_ids", "image_ids", "upload_ids"]

    @field_validator('priority')
    def priority_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Low', 'Medium', 'High', 'Urgent']):
            raise ValueError("must be one of enum values ('Low', 'Medium', 'High', 'Urgent')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['initiated', 'ready_for_review', 'not_accepted', 'closed']):
            raise ValueError("must be one of enum values ('initiated', 'ready_for_review', 'not_accepted', 'closed')")
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
        """Create an instance of Observation from a JSON string"""
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
        """Create an instance of Observation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assignee_id": obj.get("assignee_id"),
            "contributing_behavior_id": obj.get("contributing_behavior_id"),
            "contributing_condition_id": obj.get("contributing_condition_id"),
            "checklist_item_id": obj.get("checklist_item_id"),
            "coordination_issue_id": obj.get("coordination_issue_id"),
            "created_by_id": obj.get("created_by_id"),
            "description": obj.get("description"),
            "due_date": obj.get("due_date"),
            "hazard_id": obj.get("hazard_id"),
            "incident_action_id": obj.get("incident_action_id"),
            "name": obj.get("name"),
            "number": obj.get("number"),
            "personal": obj.get("personal"),
            "priority": obj.get("priority"),
            "specification_section_id": obj.get("specification_section_id"),
            "status": obj.get("status"),
            "trade_id": obj.get("trade_id"),
            "type_id": obj.get("type_id"),
            "distribution_member_ids": obj.get("distribution_member_ids"),
            "location_id": obj.get("location_id"),
            "mt_location": obj.get("mt_location"),
            "custom_field_%{custom_field_definition_id}": WorkOrderContractCustomFieldCustomFieldDefinitionId.from_dict(obj["custom_field_%{custom_field_definition_id}"]) if obj.get("custom_field_%{custom_field_definition_id}") is not None else None,
            "drawing_revision_ids": obj.get("drawing_revision_ids"),
            "file_version_ids": obj.get("file_version_ids"),
            "form_ids": obj.get("form_ids"),
            "image_ids": obj.get("image_ids"),
            "upload_ids": obj.get("upload_ids")
        })
        return _obj


