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
from typing import Optional, Set
from typing_extensions import Self

class TimecardEntry6(BaseModel):
    """
    TimecardEntry6
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Timecard entry id")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    var_date: Optional[date] = Field(default=None, description="Timecard entry date", alias="date")
    deleted_at: Optional[datetime] = Field(default=None, description="Deleted at")
    description: Optional[StrictStr] = Field(default=None, description="Timecard entry description")
    hours: Optional[StrictStr] = Field(default=None, description="Timecard entry hours")
    login_information: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    origin_id: Optional[StrictInt] = Field(default=None, description="ID of related external data")
    origin_data: Optional[StrictStr] = Field(default=None, description="Value of related external data")
    updated_at: Optional[datetime] = Field(default=None, description="Timecard entry updated at")
    __properties: ClassVar[List[str]] = ["id", "created_at", "date", "deleted_at", "description", "hours", "login_information", "origin_id", "origin_data", "updated_at"]

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
        """Create an instance of TimecardEntry6 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of login_information
        if self.login_information:
            _dict['login_information'] = self.login_information.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimecardEntry6 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "date": obj.get("date"),
            "deleted_at": obj.get("deleted_at"),
            "description": obj.get("description"),
            "hours": obj.get("hours"),
            "login_information": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["login_information"]) if obj.get("login_information") is not None else None,
            "origin_id": obj.get("origin_id"),
            "origin_data": obj.get("origin_data"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


