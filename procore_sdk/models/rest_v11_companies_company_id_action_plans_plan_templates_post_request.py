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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from procore_sdk.models.rest_v11_companies_company_id_action_plans_plan_templates_post_request_plan_template import RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate
from typing import Optional, Set
from typing_extensions import Self

class RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequest(BaseModel):
    """
    RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequest
    """ # noqa: E501
    plan_template: RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate
    __properties: ClassVar[List[str]] = ["plan_template"]

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
        """Create an instance of RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of plan_template
        if self.plan_template:
            _dict['plan_template'] = self.plan_template.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plan_template": RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate.from_dict(obj["plan_template"]) if obj.get("plan_template") is not None else None
        })
        return _obj


