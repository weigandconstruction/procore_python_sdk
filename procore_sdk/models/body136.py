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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.body136_bim_level import Body136BimLevel
from typing import Optional, Set
from typing_extensions import Self

class Body136(BaseModel):
    """
    Body136
    """ # noqa: E501
    project_id: StrictInt = Field(description="Unique identifier for the project.")
    view: Optional[StrictStr] = Field(default=None, description="Specify response schema view")
    bim_level: Body136BimLevel
    __properties: ClassVar[List[str]] = ["project_id", "view", "bim_level"]

    @field_validator('view')
    def view_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['compact', 'normal', 'extended']):
            raise ValueError("must be one of enum values ('compact', 'normal', 'extended')")
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
        """Create an instance of Body136 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bim_level
        if self.bim_level:
            _dict['bim_level'] = self.bim_level.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Body136 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "project_id": obj.get("project_id"),
            "view": obj.get("view"),
            "bim_level": Body136BimLevel.from_dict(obj["bim_level"]) if obj.get("bim_level") is not None else None
        })
        return _obj


