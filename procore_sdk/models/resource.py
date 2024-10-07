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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Resource(BaseModel):
    """
    Resource
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Resource id")
    company_id: Optional[StrictInt] = Field(default=None, description="Company id")
    deleted_at: Optional[datetime] = Field(default=None, description="Timestamp of deletion")
    name: Optional[StrictStr] = Field(default=None, description="Resource name")
    project_id: Optional[StrictInt] = Field(default=None, description="Project id")
    schedule_attributes: Optional[Dict[str, StrictStr]] = Field(default=None, description="When a schedule is imported from an external system, any attributes which are not otherwise represented in this object will appear as key-value pairs here. Note that the set of keys present in this object will depend on the application from which the schedule was obtained.")
    source_uid: Optional[StrictStr] = Field(default=None, description="The unique identifier for this resource from the external system which owns the schedule data.")
    __properties: ClassVar[List[str]] = ["id", "company_id", "deleted_at", "name", "project_id", "schedule_attributes", "source_uid"]

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
        """Create an instance of Resource from a JSON string"""
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
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deleted_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Resource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "company_id": obj.get("company_id"),
            "deleted_at": obj.get("deleted_at"),
            "name": obj.get("name"),
            "project_id": obj.get("project_id"),
            "schedule_attributes": obj.get("schedule_attributes"),
            "source_uid": obj.get("source_uid")
        })
        return _obj


