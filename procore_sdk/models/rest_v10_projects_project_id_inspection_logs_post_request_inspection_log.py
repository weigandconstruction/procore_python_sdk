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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdInspectionLogsPostRequestInspectionLog(BaseModel):
    """
    RestV10ProjectsProjectIdInspectionLogsPostRequestInspectionLog
    """ # noqa: E501
    area: Optional[StrictStr] = Field(default=None, description="Area within the specified location")
    comments: Optional[StrictStr] = Field(default=None, description="Additional comments")
    var_date: Optional[date] = Field(default=None, description="Date of inspection. Format: YYYY-MM-DD Example: 2016-04-19", alias="date")
    datetime: Optional[datetime] = Field(default=None, description="Datetime of record. Mutually exclusive with the date property.")
    end_hour: Annotated[int, Field(le=23, strict=True, ge=0)] = Field(description="Ending time of inspection - hour")
    end_minute: Annotated[int, Field(le=59, strict=True, ge=0)] = Field(description="Ending time of inspection - minute")
    inspecting_entity: Optional[StrictStr] = Field(default=None, description="Type of inspector that performing the inspection")
    inspection_type: Optional[StrictStr] = Field(default=None, description="Type of inspection performed")
    inspector_name: Optional[StrictStr] = Field(default=None, description="Name of the inspector")
    start_hour: Annotated[int, Field(le=23, strict=True, ge=0)] = Field(description="Starting time of inspection - hour")
    start_minute: Annotated[int, Field(le=59, strict=True, ge=0)] = Field(description="Starting time of inspection - minute")
    location_id: Optional[StrictInt] = Field(default=None, description="The ID of the Location of the Inspection Log. `location_id` takes precedence over `mt_location`")
    mt_location: Optional[List[StrictStr]] = Field(default=None, description="Use this for creating a new multi-tier or single-tier Location. This will be ignored if `location_id` is provided. Look at Daily Log Guide for more info.")
    __properties: ClassVar[List[str]] = ["area", "comments", "date", "datetime", "end_hour", "end_minute", "inspecting_entity", "inspection_type", "inspector_name", "start_hour", "start_minute", "location_id", "mt_location"]

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
        """Create an instance of RestV10ProjectsProjectIdInspectionLogsPostRequestInspectionLog from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdInspectionLogsPostRequestInspectionLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "area": obj.get("area"),
            "comments": obj.get("comments"),
            "date": obj.get("date"),
            "datetime": obj.get("datetime"),
            "end_hour": obj.get("end_hour"),
            "end_minute": obj.get("end_minute"),
            "inspecting_entity": obj.get("inspecting_entity"),
            "inspection_type": obj.get("inspection_type"),
            "inspector_name": obj.get("inspector_name"),
            "start_hour": obj.get("start_hour"),
            "start_minute": obj.get("start_minute"),
            "location_id": obj.get("location_id"),
            "mt_location": obj.get("mt_location")
        })
        return _obj


