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
from typing import Optional, Set
from typing_extensions import Self

class WebhooksTrigger(BaseModel):
    """
    WebhooksTrigger
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    webhook_hook_id: Optional[StrictInt] = Field(default=None, description="Hook ID")
    resource_name: Optional[StrictStr] = Field(default=None, description="Resource Name")
    resource_id: Optional[StrictInt] = Field(default=None, description="Resource ID")
    event_type: Optional[StrictStr] = Field(default=None, description="Event Type")
    company_id: Optional[StrictInt] = Field(default=None, description="Company ID (for Company scope)")
    project_id: Optional[StrictInt] = Field(default=None, description="Project ID (for Project scope)")
    user_id: Optional[StrictInt] = Field(default=None, description="User ID")
    __properties: ClassVar[List[str]] = ["id", "webhook_hook_id", "resource_name", "resource_id", "event_type", "company_id", "project_id", "user_id"]

    @field_validator('event_type')
    def event_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CREATE', 'UPDATE', 'DELETE']):
            raise ValueError("must be one of enum values ('CREATE', 'UPDATE', 'DELETE')")
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
        """Create an instance of WebhooksTrigger from a JSON string"""
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
        """Create an instance of WebhooksTrigger from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "webhook_hook_id": obj.get("webhook_hook_id"),
            "resource_name": obj.get("resource_name"),
            "resource_id": obj.get("resource_id"),
            "event_type": obj.get("event_type"),
            "company_id": obj.get("company_id"),
            "project_id": obj.get("project_id"),
            "user_id": obj.get("user_id")
        })
        return _obj


