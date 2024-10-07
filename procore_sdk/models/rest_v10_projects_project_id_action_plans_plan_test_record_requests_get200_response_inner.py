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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_record_requests_get200_response_inner_payload import RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInner(BaseModel):
    """
    Action Plan Test Record Request (Show)
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    plan_item_id: Optional[StrictInt] = Field(default=None, description="ID of the associated Action Plan Item")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp of creation")
    payload: Optional[RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload] = None
    plan_id: Optional[StrictInt] = Field(default=None, description="Action Plan ID")
    plan_test_records_count: Optional[StrictInt] = Field(default=None, description="Count of Action Plan Test Records linked to this Action Plan Test Record Request")
    type: Optional[StrictStr] = Field(default=None, description="Action Plan Test Record Type")
    type_id: Optional[StrictInt] = Field(default=None, description="Action Plan Test Record Type ID")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp of last update")
    __properties: ClassVar[List[str]] = ["id", "plan_item_id", "created_at", "payload", "plan_id", "plan_test_records_count", "type", "type_id", "updated_at"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['attachment', 'checklist', 'form', 'generic_tool', 'meeting', 'observation', 'photo', 'submittal_log']):
            raise ValueError("must be one of enum values ('attachment', 'checklist', 'form', 'generic_tool', 'meeting', 'observation', 'photo', 'submittal_log')")
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
        """Create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payload
        if self.payload:
            _dict['payload'] = self.payload.to_dict()
        # set to None if payload (nullable) is None
        # and model_fields_set contains the field
        if self.payload is None and "payload" in self.model_fields_set:
            _dict['payload'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "plan_item_id": obj.get("plan_item_id"),
            "created_at": obj.get("created_at"),
            "payload": RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload.from_dict(obj["payload"]) if obj.get("payload") is not None else None,
            "plan_id": obj.get("plan_id"),
            "plan_test_records_count": obj.get("plan_test_records_count"),
            "type": obj.get("type"),
            "type_id": obj.get("type_id"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


