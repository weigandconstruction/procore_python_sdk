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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RestV10CompaniesCompanyIdConciergePatch200Response(BaseModel):
    """
    RestV10CompaniesCompanyIdConciergePatch200Response
    """ # noqa: E501
    id: Optional[StrictInt] = None
    implementation_manager_origin_id: Optional[StrictInt] = Field(default=None, description="ID for the IM in Liftoff")
    estimated_initial_projects: Optional[StrictInt] = Field(default=None, description="Estimates number of projects in first 3 month")
    estimated_initial_users: Optional[StrictInt] = Field(default=None, description="Estimates number of staff users in first 3 month")
    __properties: ClassVar[List[str]] = ["id", "implementation_manager_origin_id", "estimated_initial_projects", "estimated_initial_users"]

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
        """Create an instance of RestV10CompaniesCompanyIdConciergePatch200Response from a JSON string"""
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
        # set to None if implementation_manager_origin_id (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_manager_origin_id is None and "implementation_manager_origin_id" in self.model_fields_set:
            _dict['implementation_manager_origin_id'] = None

        # set to None if estimated_initial_projects (nullable) is None
        # and model_fields_set contains the field
        if self.estimated_initial_projects is None and "estimated_initial_projects" in self.model_fields_set:
            _dict['estimated_initial_projects'] = None

        # set to None if estimated_initial_users (nullable) is None
        # and model_fields_set contains the field
        if self.estimated_initial_users is None and "estimated_initial_users" in self.model_fields_set:
            _dict['estimated_initial_users'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10CompaniesCompanyIdConciergePatch200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "implementation_manager_origin_id": obj.get("implementation_manager_origin_id"),
            "estimated_initial_projects": obj.get("estimated_initial_projects"),
            "estimated_initial_users": obj.get("estimated_initial_users")
        })
        return _obj


