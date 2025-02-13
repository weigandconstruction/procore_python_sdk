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
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_get200_response_inner_attachments_inner import RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner
from typing import Optional, Set
from typing_extensions import Self

class RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner(BaseModel):
    """
    Weather Log
    """ # noqa: E501
    id: Optional[StrictInt] = None
    attachments: Optional[List[RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner]] = None
    average: Optional[StrictStr] = Field(default=None, description="Average temperature for the workday")
    calamity: Optional[StrictStr] = Field(default=None, description="Translated Calamity condition based on user's locale. List of possible values can be retrieved using Weather Conditions API https://developers.procore.com/reference/rest/v1/weather-conditions?version=1.0")
    comments: Optional[StrictStr] = Field(default=None, description="Additional comments")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    created_by: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    var_date: Optional[date] = Field(default=None, description="Format: YYYY-MM-DD", alias="date")
    datetime: Optional[datetime] = Field(default=None, description="Estimated UTC datetime of record")
    deleted_at: Optional[datetime] = Field(default=None, description="Deleted at")
    is_weather_delay: Optional[StrictStr] = Field(default=None, description="Weather delay status")
    ground: Optional[StrictStr] = Field(default=None, description="Translated Ground condition based on user's locale. List of possible values can be retrieved using Weather Conditions API https://developers.procore.com/reference/rest/v1/weather-conditions?version=1.0")
    position: Optional[StrictInt] = Field(default=None, description="Order in which this entry was recorded for the day")
    precipitation: Optional[StrictStr] = Field(default=None, description="Precipitation conditions")
    sky: Optional[StrictStr] = Field(default=None, description="Translated Sky condition based on user's locale. List of possible values can be retrieved using Weather Conditions API https://developers.procore.com/reference/rest/v1/weather-conditions?version=1.0")
    temperature: Optional[StrictStr] = Field(default=None, description="Translated Temperature condition based on user's locale. List of possible values can be retrieved using Weather Conditions API https://developers.procore.com/reference/rest/v1/weather-conditions?version=1.0")
    time: Optional[datetime] = Field(default=None, description="UTC time weather conditions were observed")
    wind: Optional[StrictStr] = Field(default=None, description="Translated Wind condition based on user's locale. List of possible values can be retrieved using Weather Conditions API https://developers.procore.com/reference/rest/v1/weather-conditions?version=1.0")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    __properties: ClassVar[List[str]] = ["id", "attachments", "average", "calamity", "comments", "created_at", "created_by", "date", "datetime", "deleted_at", "is_weather_delay", "ground", "position", "precipitation", "sky", "temperature", "time", "wind", "updated_at"]

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
        """Create an instance of RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "attachments": [RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "average": obj.get("average"),
            "calamity": obj.get("calamity"),
            "comments": obj.get("comments"),
            "created_at": obj.get("created_at"),
            "created_by": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "date": obj.get("date"),
            "datetime": obj.get("datetime"),
            "deleted_at": obj.get("deleted_at"),
            "is_weather_delay": obj.get("is_weather_delay"),
            "ground": obj.get("ground"),
            "position": obj.get("position"),
            "precipitation": obj.get("precipitation"),
            "sky": obj.get("sky"),
            "temperature": obj.get("temperature"),
            "time": obj.get("time"),
            "wind": obj.get("wind"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


