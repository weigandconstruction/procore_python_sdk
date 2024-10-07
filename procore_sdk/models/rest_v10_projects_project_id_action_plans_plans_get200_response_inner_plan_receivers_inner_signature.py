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
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_attachment import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureAttachment
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_captured_by import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature(BaseModel):
    """
    Action Plan Receiver Signature (Show)
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    attachment: Optional[RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureAttachment] = None
    captured_at: Optional[datetime] = Field(default=None, description="Timestamp of when signature was added.")
    captured_by: Optional[RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy] = None
    __properties: ClassVar[List[str]] = ["id", "attachment", "captured_at", "captured_by"]

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
        """Create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attachment
        if self.attachment:
            _dict['attachment'] = self.attachment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of captured_by
        if self.captured_by:
            _dict['captured_by'] = self.captured_by.to_dict()
        # set to None if captured_by (nullable) is None
        # and model_fields_set contains the field
        if self.captured_by is None and "captured_by" in self.model_fields_set:
            _dict['captured_by'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "attachment": RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureAttachment.from_dict(obj["attachment"]) if obj.get("attachment") is not None else None,
            "captured_at": obj.get("captured_at"),
            "captured_by": RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy.from_dict(obj["captured_by"]) if obj.get("captured_by") is not None else None
        })
        return _obj


