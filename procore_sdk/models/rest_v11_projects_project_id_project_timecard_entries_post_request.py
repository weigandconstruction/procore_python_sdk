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
from procore_sdk.models.work_order_contract_custom_field_custom_field_definition_id import WorkOrderContractCustomFieldCustomFieldDefinitionId
from typing import Optional, Set
from typing_extensions import Self

class RestV11ProjectsProjectIdProjectTimecardEntriesPostRequest(BaseModel):
    """
    RestV11ProjectsProjectIdProjectTimecardEntriesPostRequest
    """ # noqa: E501
    hours: Optional[StrictStr] = Field(default=None, description="Total number of hours worked (excluding breaks) for the timecard entry. This property is not required if the timesheet time entry is configured for start time and stop time.")
    lunch_time: Optional[StrictStr] = Field(default=None, description="The duration of the lunch break, in minutes, for the Timecard Entry. This property is only required if the timesheet time entry is configured for start time and stop time.")
    time_in: Optional[StrictStr] = Field(default=None, description="The start time of the Timecard Entry in ISO 8601 format. This property is only required if the timesheet time entry is configured for start time and stop time.")
    time_out: Optional[StrictStr] = Field(default=None, description="The stop time of the Timecard Entry in ISO 8601 format. This property is only required if the timesheet time entry is configured for start time and stop time.")
    billable: Optional[StrictBool] = Field(default=False, description="The billable status of the Timecard Entry. Must be either true or false.")
    var_date: Optional[date] = Field(default=None, description="The date of the Timecard Entry in ISO 8601 format.", alias="date")
    description: Optional[StrictStr] = Field(default=None, description="The description of the Timecard Entry.")
    timecard_time_type_id: Optional[StrictInt] = Field(default=None, description="The ID of the Timecard Time Type corresponding to the Timecard Entry property.")
    timesheet_id: Optional[StrictInt] = Field(default=None, description="The ID of the Timesheet corresponding to the Timecard Entry property.")
    cost_code_id: Optional[StrictInt] = Field(default=None, description="The ID of the Cost Code corresponding to the Timecard Entry property.")
    sub_job_id: Optional[StrictInt] = Field(default=None, description="The ID of the Subjob corresponding to the Timecard Entry property.")
    location_id: Optional[StrictInt] = Field(default=None, description="The ID of the Location corresponding to the Timecard Entry property.")
    login_information_id: Optional[StrictInt] = Field(default=None, description="The ID of the Login Information corresponding to the Timecard Entry property.")
    party_id: Optional[StrictInt] = Field(default=None, description="The ID of the Party corresponding to the Timecard Entry property.")
    origin_id: Optional[StrictInt] = Field(default=None, description="The ID of the related external data.")
    origin_data: Optional[StrictStr] = Field(default=None, description="The value of the related external data.")
    line_item_type_id: Optional[StrictInt] = Field(default=None, description="The ID of the line item type corresponding to the time card entry.")
    custom_field_custom_field_definition_id: Optional[WorkOrderContractCustomFieldCustomFieldDefinitionId] = Field(default=None, alias="custom_field_%{custom_field_definition_id}")
    __properties: ClassVar[List[str]] = ["hours", "lunch_time", "time_in", "time_out", "billable", "date", "description", "timecard_time_type_id", "timesheet_id", "cost_code_id", "sub_job_id", "location_id", "login_information_id", "party_id", "origin_id", "origin_data", "line_item_type_id", "custom_field_%{custom_field_definition_id}"]

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
        """Create an instance of RestV11ProjectsProjectIdProjectTimecardEntriesPostRequest from a JSON string"""
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
        """Create an instance of RestV11ProjectsProjectIdProjectTimecardEntriesPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hours": obj.get("hours"),
            "lunch_time": obj.get("lunch_time"),
            "time_in": obj.get("time_in"),
            "time_out": obj.get("time_out"),
            "billable": obj.get("billable") if obj.get("billable") is not None else False,
            "date": obj.get("date"),
            "description": obj.get("description"),
            "timecard_time_type_id": obj.get("timecard_time_type_id"),
            "timesheet_id": obj.get("timesheet_id"),
            "cost_code_id": obj.get("cost_code_id"),
            "sub_job_id": obj.get("sub_job_id"),
            "location_id": obj.get("location_id"),
            "login_information_id": obj.get("login_information_id"),
            "party_id": obj.get("party_id"),
            "origin_id": obj.get("origin_id"),
            "origin_data": obj.get("origin_data"),
            "line_item_type_id": obj.get("line_item_type_id"),
            "custom_field_%{custom_field_definition_id}": WorkOrderContractCustomFieldCustomFieldDefinitionId.from_dict(obj["custom_field_%{custom_field_definition_id}"]) if obj.get("custom_field_%{custom_field_definition_id}") is not None else None
        })
        return _obj


