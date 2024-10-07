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
from typing_extensions import Annotated
from procore_sdk.models.work_order_contract_custom_field_custom_field_definition_id import WorkOrderContractCustomFieldCustomFieldDefinitionId
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdEquipmentLogsPostRequest1EquipmentLog(BaseModel):
    """
    RestV10ProjectsProjectIdEquipmentLogsPostRequest1EquipmentLog
    """ # noqa: E501
    var_date: Optional[date] = Field(default=None, description="Date of record. Format: YYYY-MM-DD", alias="date")
    datetime: Optional[datetime] = Field(default=None, description="Datetime of record. Mutually exclusive with the date property.")
    hours_idle: Optional[StrictInt] = Field(default=None, description="Number of hours the Equipment was idle")
    hours_operating: Optional[StrictInt] = Field(default=None, description="Number of hours the Equipment was in operation")
    inspected: Optional[StrictBool] = Field(default=None, description="Inspection status of Equipment before operation")
    inspection_hour: Annotated[int, Field(le=23, strict=True, ge=0)] = Field(description="Time of inspection - hour")
    inspection_minute: Annotated[int, Field(le=59, strict=True, ge=0)] = Field(description="Time of inspection - minute")
    notes: Optional[StrictStr] = Field(default=None, description="Notes")
    location_id: Optional[StrictInt] = Field(default=None, description="The ID of the Location of the Inspection Log. `location_id` takes precedence over `mt_location`")
    mt_location: Optional[List[StrictStr]] = Field(default=None, description="Use this for creating a new multi-tier or single-tier Location. This will be ignored if `location_id` is provided.")
    cost_code_id: Optional[StrictInt] = Field(default=None, description="Cost Code ID")
    equipment_id: Optional[StrictInt] = Field(default=None, description="Equipment ID")
    equipment_name: Optional[StrictStr] = Field(default=None, description="Equipment name. This Equipment will create on the fly if it doesn't exist and will take precedence over Equipment ID.")
    custom_field_custom_field_definition_id: Optional[WorkOrderContractCustomFieldCustomFieldDefinitionId] = Field(default=None, alias="custom_field_%{custom_field_definition_id}")
    __properties: ClassVar[List[str]] = ["date", "datetime", "hours_idle", "hours_operating", "inspected", "inspection_hour", "inspection_minute", "notes", "location_id", "mt_location", "cost_code_id", "equipment_id", "equipment_name", "custom_field_%{custom_field_definition_id}"]

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
        """Create an instance of RestV10ProjectsProjectIdEquipmentLogsPostRequest1EquipmentLog from a JSON string"""
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
        # set to None if location_id (nullable) is None
        # and model_fields_set contains the field
        if self.location_id is None and "location_id" in self.model_fields_set:
            _dict['location_id'] = None

        # set to None if mt_location (nullable) is None
        # and model_fields_set contains the field
        if self.mt_location is None and "mt_location" in self.model_fields_set:
            _dict['mt_location'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdEquipmentLogsPostRequest1EquipmentLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "datetime": obj.get("datetime"),
            "hours_idle": obj.get("hours_idle"),
            "hours_operating": obj.get("hours_operating"),
            "inspected": obj.get("inspected"),
            "inspection_hour": obj.get("inspection_hour"),
            "inspection_minute": obj.get("inspection_minute"),
            "notes": obj.get("notes"),
            "location_id": obj.get("location_id"),
            "mt_location": obj.get("mt_location"),
            "cost_code_id": obj.get("cost_code_id"),
            "equipment_id": obj.get("equipment_id"),
            "equipment_name": obj.get("equipment_name"),
            "custom_field_%{custom_field_definition_id}": WorkOrderContractCustomFieldCustomFieldDefinitionId.from_dict(obj["custom_field_%{custom_field_definition_id}"]) if obj.get("custom_field_%{custom_field_definition_id}") is not None else None
        })
        return _obj


