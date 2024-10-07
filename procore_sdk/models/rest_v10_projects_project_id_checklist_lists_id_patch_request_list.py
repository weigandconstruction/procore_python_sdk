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
from procore_sdk.models.work_order_contract_custom_field_custom_field_definition_id import WorkOrderContractCustomFieldCustomFieldDefinitionId
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdChecklistListsIdPatchRequestList(BaseModel):
    """
    RestV10ProjectsProjectIdChecklistListsIdPatchRequestList
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The Name of the Inspection")
    description: Optional[StrictStr] = Field(default=None, description="Description of the Inspection")
    due_at: Optional[datetime] = Field(default=None, description="Timestamp indicating when the Inspection is due.")
    inspection_date: Optional[date] = Field(default=None, description="Date of the Inspection")
    inspection_type_id: Optional[StrictInt] = Field(default=None, description="The ID of the Inspection's Type")
    number: Optional[StrictInt] = Field(default=None, description="The Number of the Checklist. If no number is passed in, the next available number will be used.")
    point_of_contact_id: Optional[StrictInt] = Field(default=None, description="The ID of the Inspection's Point of Contact")
    inspector_ids: Optional[List[StrictInt]] = Field(default=None, description="The IDs of the Inspectors performing the Inspection")
    private: Optional[StrictBool] = Field(default=True, description="Indicates whether this Inspection is private")
    responsible_contractor_id: Optional[StrictInt] = Field(default=None, description="The ID of the Inspection's Responsible Contractor")
    spec_section_id: Optional[StrictInt] = Field(default=None, description="The ID of the Inspection's Specification Section")
    status: Optional[StrictStr] = Field(default=None, description="The Inspection's status")
    trade_id: Optional[StrictInt] = Field(default=None, description="The ID of the Trade involved in the Inspection")
    distribution_member_ids: Optional[List[StrictInt]] = Field(default=None, description="The IDs of the Distribution Members for the Inspection")
    location_id: Optional[StrictInt] = Field(default=None, description="The ID of the Location of the Inspection")
    custom_field_custom_field_definition_id: Optional[WorkOrderContractCustomFieldCustomFieldDefinitionId] = Field(default=None, alias="custom_field_%{custom_field_definition_id}")
    __properties: ClassVar[List[str]] = ["name", "description", "due_at", "inspection_date", "inspection_type_id", "number", "point_of_contact_id", "inspector_ids", "private", "responsible_contractor_id", "spec_section_id", "status", "trade_id", "distribution_member_ids", "location_id", "custom_field_%{custom_field_definition_id}"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['open', 'in_review', 'closed']):
            raise ValueError("must be one of enum values ('open', 'in_review', 'closed')")
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
        """Create an instance of RestV10ProjectsProjectIdChecklistListsIdPatchRequestList from a JSON string"""
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
        """Create an instance of RestV10ProjectsProjectIdChecklistListsIdPatchRequestList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "due_at": obj.get("due_at"),
            "inspection_date": obj.get("inspection_date"),
            "inspection_type_id": obj.get("inspection_type_id"),
            "number": obj.get("number"),
            "point_of_contact_id": obj.get("point_of_contact_id"),
            "inspector_ids": obj.get("inspector_ids"),
            "private": obj.get("private") if obj.get("private") is not None else True,
            "responsible_contractor_id": obj.get("responsible_contractor_id"),
            "spec_section_id": obj.get("spec_section_id"),
            "status": obj.get("status"),
            "trade_id": obj.get("trade_id"),
            "distribution_member_ids": obj.get("distribution_member_ids"),
            "location_id": obj.get("location_id"),
            "custom_field_%{custom_field_definition_id}": WorkOrderContractCustomFieldCustomFieldDefinitionId.from_dict(obj["custom_field_%{custom_field_definition_id}"]) if obj.get("custom_field_%{custom_field_definition_id}") is not None else None
        })
        return _obj


