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
from procore_sdk.models.incident_environmental_update_parameters import IncidentEnvironmentalUpdateParameters
from procore_sdk.models.incident_injury_update_parameters import IncidentInjuryUpdateParameters
from procore_sdk.models.incident_near_miss_update_parameters import IncidentNearMissUpdateParameters
from procore_sdk.models.incident_property_damage_update_parameters import IncidentPropertyDamageUpdateParameters
from procore_sdk.models.incident_witness_statement_update_parameters1 import IncidentWitnessStatementUpdateParameters1
from procore_sdk.models.work_order_contract_custom_field_custom_field_definition_id import WorkOrderContractCustomFieldCustomFieldDefinitionId
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdIncidentsPostRequestIncident(BaseModel):
    """
    RestV10ProjectsProjectIdIncidentsPostRequestIncident
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description of the Incident")
    event_date: Optional[datetime] = Field(default=None, description="Iso8601 datetime of Incident occurrence. If time is unknown, send in the date at 0:00 project time converted to UTC.")
    distribution_member_ids: Optional[List[StrictInt]] = Field(default=None, description="An Array of the IDs of the Distribution Members")
    private: Optional[StrictBool] = Field(default=None, description="Indicates whether an Incident is private")
    recordable: Optional[StrictBool] = Field(default=None, description="Indicates whether an Incident is recordable")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    time_unknown: Optional[StrictBool] = Field(default=None, description="Indicates that the time of the Incident occurrence is unknown")
    title: Optional[StrictStr] = Field(default=None, description="Incident Title")
    contributing_behavior_id: Optional[StrictInt] = Field(default=None, description="The ID of a Contributing Behavior")
    contributing_condition_id: Optional[StrictInt] = Field(default=None, description="The ID of a Contributing Condition")
    hazard_id: Optional[StrictInt] = Field(default=None, description="The ID of a Hazard")
    location_id: Optional[StrictInt] = Field(default=None, description="The ID of a Location")
    environmentals: Optional[List[IncidentEnvironmentalUpdateParameters]] = Field(default=None, description="Associated Environmentals to create")
    injuries: Optional[List[IncidentInjuryUpdateParameters]] = Field(default=None, description="Associated Injuries to create")
    near_misses: Optional[List[IncidentNearMissUpdateParameters]] = Field(default=None, description="Associated Near Misses to create")
    property_damages: Optional[List[IncidentPropertyDamageUpdateParameters]] = Field(default=None, description="Associated Property Damages to create")
    witness_statements_attributes: Optional[List[IncidentWitnessStatementUpdateParameters1]] = Field(default=None, description="Associated Witness Statement to create")
    upload_uuids: Optional[List[StrictStr]] = Field(default=None, description="Array of uploaded file UUIDs.")
    custom_field_custom_field_definition_id: Optional[WorkOrderContractCustomFieldCustomFieldDefinitionId] = Field(default=None, alias="custom_field_%{custom_field_definition_id}")
    drawing_revision_ids: Optional[List[StrictInt]] = Field(default=None, description="Drawing Revisions to attach to the response")
    file_version_ids: Optional[List[StrictInt]] = Field(default=None, description="File Versions to attach to the response")
    form_ids: Optional[List[StrictInt]] = Field(default=None, description="Forms to attach to the response")
    image_ids: Optional[List[StrictInt]] = Field(default=None, description="Images to attach to the response")
    __properties: ClassVar[List[str]] = ["description", "event_date", "distribution_member_ids", "private", "recordable", "status", "time_unknown", "title", "contributing_behavior_id", "contributing_condition_id", "hazard_id", "location_id", "environmentals", "injuries", "near_misses", "property_damages", "witness_statements_attributes", "upload_uuids", "custom_field_%{custom_field_definition_id}", "drawing_revision_ids", "file_version_ids", "form_ids", "image_ids"]

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
        """Create an instance of RestV10ProjectsProjectIdIncidentsPostRequestIncident from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in environmentals (list)
        _items = []
        if self.environmentals:
            for _item_environmentals in self.environmentals:
                if _item_environmentals:
                    _items.append(_item_environmentals.to_dict())
            _dict['environmentals'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in injuries (list)
        _items = []
        if self.injuries:
            for _item_injuries in self.injuries:
                if _item_injuries:
                    _items.append(_item_injuries.to_dict())
            _dict['injuries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in near_misses (list)
        _items = []
        if self.near_misses:
            for _item_near_misses in self.near_misses:
                if _item_near_misses:
                    _items.append(_item_near_misses.to_dict())
            _dict['near_misses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in property_damages (list)
        _items = []
        if self.property_damages:
            for _item_property_damages in self.property_damages:
                if _item_property_damages:
                    _items.append(_item_property_damages.to_dict())
            _dict['property_damages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in witness_statements_attributes (list)
        _items = []
        if self.witness_statements_attributes:
            for _item_witness_statements_attributes in self.witness_statements_attributes:
                if _item_witness_statements_attributes:
                    _items.append(_item_witness_statements_attributes.to_dict())
            _dict['witness_statements_attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of custom_field_custom_field_definition_id
        if self.custom_field_custom_field_definition_id:
            _dict['custom_field_%{custom_field_definition_id}'] = self.custom_field_custom_field_definition_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdIncidentsPostRequestIncident from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "event_date": obj.get("event_date"),
            "distribution_member_ids": obj.get("distribution_member_ids"),
            "private": obj.get("private"),
            "recordable": obj.get("recordable"),
            "status": obj.get("status"),
            "time_unknown": obj.get("time_unknown"),
            "title": obj.get("title"),
            "contributing_behavior_id": obj.get("contributing_behavior_id"),
            "contributing_condition_id": obj.get("contributing_condition_id"),
            "hazard_id": obj.get("hazard_id"),
            "location_id": obj.get("location_id"),
            "environmentals": [IncidentEnvironmentalUpdateParameters.from_dict(_item) for _item in obj["environmentals"]] if obj.get("environmentals") is not None else None,
            "injuries": [IncidentInjuryUpdateParameters.from_dict(_item) for _item in obj["injuries"]] if obj.get("injuries") is not None else None,
            "near_misses": [IncidentNearMissUpdateParameters.from_dict(_item) for _item in obj["near_misses"]] if obj.get("near_misses") is not None else None,
            "property_damages": [IncidentPropertyDamageUpdateParameters.from_dict(_item) for _item in obj["property_damages"]] if obj.get("property_damages") is not None else None,
            "witness_statements_attributes": [IncidentWitnessStatementUpdateParameters1.from_dict(_item) for _item in obj["witness_statements_attributes"]] if obj.get("witness_statements_attributes") is not None else None,
            "upload_uuids": obj.get("upload_uuids"),
            "custom_field_%{custom_field_definition_id}": WorkOrderContractCustomFieldCustomFieldDefinitionId.from_dict(obj["custom_field_%{custom_field_definition_id}"]) if obj.get("custom_field_%{custom_field_definition_id}") is not None else None,
            "drawing_revision_ids": obj.get("drawing_revision_ids"),
            "file_version_ids": obj.get("file_version_ids"),
            "form_ids": obj.get("form_ids"),
            "image_ids": obj.get("image_ids")
        })
        return _obj


