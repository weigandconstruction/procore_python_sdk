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
from typing import Any, ClassVar, Dict, List
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_references_post_request1_plan_template_reference_payload import RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReference(BaseModel):
    """
    RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReference
    """ # noqa: E501
    plan_template_item_id: StrictInt = Field(description="Project Action Plan Template Item ID")
    type: StrictStr = Field(description="Action Plan Reference Type")
    payload: RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload
    __properties: ClassVar[List[str]] = ["plan_template_item_id", "type", "payload"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['attachment', 'drawing', 'document', 'specification_section', 'generic_tool_item', 'form', 'image', 'meeting', 'observation_item']):
            raise ValueError("must be one of enum values ('attachment', 'drawing', 'document', 'specification_section', 'generic_tool_item', 'form', 'image', 'meeting', 'observation_item')")
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
        """Create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReference from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plan_template_item_id": obj.get("plan_template_item_id"),
            "type": obj.get("type"),
            "payload": RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload.from_dict(obj["payload"]) if obj.get("payload") is not None else None
        })
        return _obj


