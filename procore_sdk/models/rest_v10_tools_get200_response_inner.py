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

class RestV10ToolsGet200ResponseInner(BaseModel):
    """
    RestV10ToolsGet200ResponseInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The ID of the Tool")
    engine_name: Optional[StrictStr] = Field(default=None, description="The name of the Tool engine")
    is_active: Optional[StrictBool] = Field(default=None, description="Indicates whether the tool is currently active")
    position: Optional[StrictInt] = Field(default=None, description="The ordering position of the Tool")
    required: Optional[StrictBool] = Field(default=None, description="Indicates whether the tool must be active")
    user_access_level: Optional[StrictStr] = Field(default=None, description="The user access level")
    provider_id: Optional[StrictInt] = Field(default=None, description="The Provider id")
    provider_type: Optional[StrictStr] = Field(default=None, description="The Provider type")
    __properties: ClassVar[List[str]] = ["id", "engine_name", "is_active", "position", "required", "user_access_level", "provider_id", "provider_type"]

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
        """Create an instance of RestV10ToolsGet200ResponseInner from a JSON string"""
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
        """Create an instance of RestV10ToolsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "engine_name": obj.get("engine_name"),
            "is_active": obj.get("is_active"),
            "position": obj.get("position"),
            "required": obj.get("required"),
            "user_access_level": obj.get("user_access_level"),
            "provider_id": obj.get("provider_id"),
            "provider_type": obj.get("provider_type")
        })
        return _obj


