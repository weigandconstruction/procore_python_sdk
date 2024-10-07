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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequestPlanItemAssignee(BaseModel):
    """
    RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequestPlanItemAssignee
    """ # noqa: E501
    plan_item_id: StrictInt = Field(description="Action Plan Item ID of the Action Plan Item Assignee to be set")
    is_holding: Optional[StrictBool] = Field(default=None, description="Indicates whether or not the Action  Item Assignee's signature is holding")
    party_id: Optional[StrictInt] = Field(default=None, description="Party Person ID of the Action Plan Item Assignee to be set")
    role: Optional[StrictStr] = Field(default=None, description="Role of the Action Plan Item Assignee to be set")
    verification_method_id: Optional[StrictInt] = Field(default=None, description="Verification Method ID of the Action Plan Item Assignee to be set")
    __properties: ClassVar[List[str]] = ["plan_item_id", "is_holding", "party_id", "role", "verification_method_id"]

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['contractor', 'specialty_contractor', 'client', 'architect', 'third_party', 'internal']):
            raise ValueError("must be one of enum values ('contractor', 'specialty_contractor', 'client', 'architect', 'third_party', 'internal')")
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
        """Create an instance of RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequestPlanItemAssignee from a JSON string"""
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
        """Create an instance of RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequestPlanItemAssignee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plan_item_id": obj.get("plan_item_id"),
            "is_holding": obj.get("is_holding"),
            "party_id": obj.get("party_id"),
            "role": obj.get("role"),
            "verification_method_id": obj.get("verification_method_id")
        })
        return _obj


