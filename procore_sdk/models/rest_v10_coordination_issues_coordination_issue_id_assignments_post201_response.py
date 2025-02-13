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
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response(BaseModel):
    """
    Coordination Issue Assignment
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    coordination_issue_id: Optional[StrictInt] = Field(default=None, description="Coordination Issue ID")
    old_assignee_id: Optional[StrictInt] = Field(default=None, description="Coordination Issue Assignee ID before the change")
    new_assignee_id: Optional[StrictInt] = Field(default=None, description="Coordination Issue Assignee ID after the change")
    created_by_id: Optional[StrictInt] = Field(default=None, description="ID of the user responsible for the reassignment")
    created_at: Optional[datetime] = Field(default=None, description="Created date")
    __properties: ClassVar[List[str]] = ["id", "coordination_issue_id", "old_assignee_id", "new_assignee_id", "created_by_id", "created_at"]

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
        """Create an instance of RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response from a JSON string"""
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
        """Create an instance of RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "coordination_issue_id": obj.get("coordination_issue_id"),
            "old_assignee_id": obj.get("old_assignee_id"),
            "new_assignee_id": obj.get("new_assignee_id"),
            "created_by_id": obj.get("created_by_id"),
            "created_at": obj.get("created_at")
        })
        return _obj


