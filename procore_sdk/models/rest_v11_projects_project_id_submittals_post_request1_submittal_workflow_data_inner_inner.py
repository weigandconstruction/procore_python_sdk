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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RestV11ProjectsProjectIdSubmittalsPostRequest1SubmittalWorkflowDataInnerInner(BaseModel):
    """
    RestV11ProjectsProjectIdSubmittalsPostRequest1SubmittalWorkflowDataInnerInner
    """ # noqa: E501
    login_information_id: Optional[StrictInt] = Field(default=None, description="The id of the user in the workflow")
    approver_type: Optional[StrictStr] = Field(default=None, description="The role of the user in the workflow")
    days_to_respond: Optional[StrictInt] = Field(default=None, description="The amount of days to respond to workflow item. *Please use either days_to_respond or due_date (days_to_respond takes precedence over due_date)")
    due_date: Optional[date] = Field(default=None, description="The due date for the user's response.")
    response_required: Optional[StrictBool] = Field(default=None, description="Designate whether or not the approver is required to respond")
    __properties: ClassVar[List[str]] = ["login_information_id", "approver_type", "days_to_respond", "due_date", "response_required"]

    @field_validator('approver_type')
    def approver_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Submitter', 'Approver']):
            raise ValueError("must be one of enum values ('Submitter', 'Approver')")
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
        """Create an instance of RestV11ProjectsProjectIdSubmittalsPostRequest1SubmittalWorkflowDataInnerInner from a JSON string"""
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
        """Create an instance of RestV11ProjectsProjectIdSubmittalsPostRequest1SubmittalWorkflowDataInnerInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "login_information_id": obj.get("login_information_id"),
            "approver_type": obj.get("approver_type"),
            "days_to_respond": obj.get("days_to_respond"),
            "due_date": obj.get("due_date"),
            "response_required": obj.get("response_required")
        })
        return _obj


