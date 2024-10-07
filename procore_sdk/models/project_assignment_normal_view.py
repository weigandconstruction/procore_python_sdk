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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProjectAssignmentNormalView(BaseModel):
    """
    ProjectAssignmentNormalView
    """ # noqa: E501
    project_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the project.")
    name: Optional[StrictStr] = Field(default=None, description="Project name")
    project_number: Optional[StrictStr] = Field(default=None, description="Project number")
    address: Optional[StrictStr] = Field(default=None, description="Project address")
    stage: Optional[StrictStr] = Field(default=None, description="Stage name")
    is_assigned: Optional[StrictBool] = Field(default=None, description="Whether user is assigned to project or not")
    active: Optional[StrictBool] = Field(default=None, description="Whether the project is active or not")
    roles: Optional[List[StrictStr]] = Field(default=None, description="Array of user project role names")
    permission_template_name: Optional[StrictStr] = Field(default=None, description="Project currently assigned user permission template name")
    region: Optional[StrictStr] = Field(default=None, description="Region assigned to the project")
    program: Optional[StrictStr] = Field(default=None, description="Program assigned to the project")
    project_type: Optional[StrictStr] = Field(default=None, description="Project type assigned to the project")
    __properties: ClassVar[List[str]] = ["project_id", "name", "project_number", "address", "stage", "is_assigned", "active", "roles", "permission_template_name", "region", "program", "project_type"]

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
        """Create an instance of ProjectAssignmentNormalView from a JSON string"""
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
        # set to None if project_number (nullable) is None
        # and model_fields_set contains the field
        if self.project_number is None and "project_number" in self.model_fields_set:
            _dict['project_number'] = None

        # set to None if address (nullable) is None
        # and model_fields_set contains the field
        if self.address is None and "address" in self.model_fields_set:
            _dict['address'] = None

        # set to None if stage (nullable) is None
        # and model_fields_set contains the field
        if self.stage is None and "stage" in self.model_fields_set:
            _dict['stage'] = None

        # set to None if permission_template_name (nullable) is None
        # and model_fields_set contains the field
        if self.permission_template_name is None and "permission_template_name" in self.model_fields_set:
            _dict['permission_template_name'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        # set to None if program (nullable) is None
        # and model_fields_set contains the field
        if self.program is None and "program" in self.model_fields_set:
            _dict['program'] = None

        # set to None if project_type (nullable) is None
        # and model_fields_set contains the field
        if self.project_type is None and "project_type" in self.model_fields_set:
            _dict['project_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectAssignmentNormalView from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "project_id": obj.get("project_id"),
            "name": obj.get("name"),
            "project_number": obj.get("project_number"),
            "address": obj.get("address"),
            "stage": obj.get("stage"),
            "is_assigned": obj.get("is_assigned"),
            "active": obj.get("active"),
            "roles": obj.get("roles"),
            "permission_template_name": obj.get("permission_template_name"),
            "region": obj.get("region"),
            "program": obj.get("program"),
            "project_type": obj.get("project_type")
        })
        return _obj


