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
from procore_sdk.models.array_of_task_items_that_were_sent_out_inner_all_of_assignee import ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee
from procore_sdk.models.contributing_behavior import ContributingBehavior
from procore_sdk.models.contributing_condition import ContributingCondition
from procore_sdk.models.hazard import Hazard
from procore_sdk.models.location import Location
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_custom_fields import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields
from typing import Optional, Set
from typing_extensions import Self

class IncidentCompact(BaseModel):
    """
    IncidentCompact
    """ # noqa: E501
    id: Optional[StrictInt] = None
    created_at: Optional[datetime] = Field(default=None, description="Timestamp of creation")
    deleted_at: Optional[datetime] = Field(default=None, description="Timestamp of deletion")
    description: Optional[StrictStr] = Field(default=None, description="Description of the Incident")
    event_date: Optional[datetime] = Field(default=None, description="Date of Incident occurrence")
    number: Optional[StrictInt] = Field(default=None, description="Number")
    private: Optional[StrictBool] = Field(default=None, description="Indicates whether an Incident is private")
    recordable: Optional[StrictBool] = Field(default=None, description="Indicates whether an Incident is recordable")
    records_count: Optional[StrictInt] = Field(default=None, description="Number of Records associated to the Incident")
    open_observations_count: Optional[StrictInt] = Field(default=None, description="Number of Open Observations associated to the Incident")
    closed_observations_count: Optional[StrictInt] = Field(default=None, description="Number of Closed Observations associated to the Incident")
    actions_count: Optional[StrictInt] = Field(default=None, description="Number of Actions associated to the Incident")
    witness_statements_count: Optional[StrictInt] = Field(default=None, description="Number of Witness Statements associated to the Incident")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    time_unknown: Optional[StrictBool] = Field(default=None, description="Indicates that the time of the Incident occurrence is unknown")
    title: Optional[StrictStr] = Field(default=None, description="Incident Title")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp of last update")
    created_by: Optional[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee] = None
    contributing_behavior: Optional[ContributingBehavior] = None
    contributing_condition: Optional[ContributingCondition] = None
    hazard: Optional[Hazard] = None
    location: Optional[Location] = None
    attachments_count: Optional[StrictInt] = Field(default=None, description="Number of Attachments attached to the Incident")
    custom_fields: Optional[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "deleted_at", "description", "event_date", "number", "private", "recordable", "records_count", "open_observations_count", "closed_observations_count", "actions_count", "witness_statements_count", "status", "time_unknown", "title", "updated_at", "created_by", "contributing_behavior", "contributing_condition", "hazard", "location", "attachments_count", "custom_fields"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['open', 'closed']):
            raise ValueError("must be one of enum values ('open', 'closed')")
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
        """Create an instance of IncidentCompact from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contributing_behavior
        if self.contributing_behavior:
            _dict['contributing_behavior'] = self.contributing_behavior.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contributing_condition
        if self.contributing_condition:
            _dict['contributing_condition'] = self.contributing_condition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hazard
        if self.hazard:
            _dict['hazard'] = self.hazard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_fields
        if self.custom_fields:
            _dict['custom_fields'] = self.custom_fields.to_dict()
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deleted_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IncidentCompact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "deleted_at": obj.get("deleted_at"),
            "description": obj.get("description"),
            "event_date": obj.get("event_date"),
            "number": obj.get("number"),
            "private": obj.get("private"),
            "recordable": obj.get("recordable"),
            "records_count": obj.get("records_count"),
            "open_observations_count": obj.get("open_observations_count"),
            "closed_observations_count": obj.get("closed_observations_count"),
            "actions_count": obj.get("actions_count"),
            "witness_statements_count": obj.get("witness_statements_count"),
            "status": obj.get("status"),
            "time_unknown": obj.get("time_unknown"),
            "title": obj.get("title"),
            "updated_at": obj.get("updated_at"),
            "created_by": ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "contributing_behavior": ContributingBehavior.from_dict(obj["contributing_behavior"]) if obj.get("contributing_behavior") is not None else None,
            "contributing_condition": ContributingCondition.from_dict(obj["contributing_condition"]) if obj.get("contributing_condition") is not None else None,
            "hazard": Hazard.from_dict(obj["hazard"]) if obj.get("hazard") is not None else None,
            "location": Location.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "attachments_count": obj.get("attachments_count"),
            "custom_fields": RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.from_dict(obj["custom_fields"]) if obj.get("custom_fields") is not None else None
        })
        return _obj


