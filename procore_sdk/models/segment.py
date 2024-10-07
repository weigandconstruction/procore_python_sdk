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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Segment(BaseModel):
    """
    Segment
    """ # noqa: E501
    name: StrictStr = Field(description="Segment Name")
    project_can_modify_origin_project: Optional[StrictBool] = Field(default=None, description="Whether project-specific Segment Items are able to be added/edited/removed from a Project.")
    project_can_delete_origin_company: Optional[StrictBool] = Field(default=None, description="Whether Segment Items inherited from the company-level are able to be deleted from a Project.")
    structure: StrictStr = Field(description="The Structure for this Wbs Segment.")
    __properties: ClassVar[List[str]] = ["name", "project_can_modify_origin_project", "project_can_delete_origin_company", "structure"]

    @field_validator('structure')
    def structure_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['tiered', 'flat']):
            raise ValueError("must be one of enum values ('tiered', 'flat')")
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
        """Create an instance of Segment from a JSON string"""
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
        """Create an instance of Segment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "project_can_modify_origin_project": obj.get("project_can_modify_origin_project"),
            "project_can_delete_origin_company": obj.get("project_can_delete_origin_company"),
            "structure": obj.get("structure")
        })
        return _obj


