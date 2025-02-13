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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_manager_vendor import RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManagerVendor
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdActionPlansPartiesGet200ResponseInner(BaseModel):
    """
    RestV10ProjectsProjectIdActionPlansPartiesGet200ResponseInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Party Person ID")
    first_name: Optional[StrictStr] = Field(default=None, description="First name of the Party Person")
    last_name: Optional[StrictStr] = Field(default=None, description="Last name of the Party Person")
    name: Optional[StrictStr] = Field(default=None, description="Full name of the Party Person")
    vendor: Optional[RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManagerVendor] = None
    user_id: Optional[StrictInt] = Field(default=None, description="Login Information ID associated with the Party Person")
    is_employee: Optional[StrictBool] = Field(default=None, description="Indicates whether Party is an Employee of the current Company")
    employee_id: Optional[StrictStr] = Field(default=None, description="Employee ID of the Party")
    potential_approver: Optional[StrictBool] = Field(default=None, description="Flag denoting if Party Person can act as Action Plan Approver")
    potential_assignee: Optional[StrictBool] = Field(default=None, description="Flag denoting if Party Person can act as Action Plan Item Assignee")
    potential_manager: Optional[StrictBool] = Field(default=None, description="Flag denoting if Party Person can act as Action Plan Manager")
    potential_receiver: Optional[StrictBool] = Field(default=None, description="Flag denoting if Party Person can act as Action Plan Receiver")
    updated_at: Optional[datetime] = Field(default=None, description="Time the Party Person was updated")
    login: Optional[StrictStr] = Field(default=None, description="Login of the Party Person")
    __properties: ClassVar[List[str]] = ["id", "first_name", "last_name", "name", "vendor", "user_id", "is_employee", "employee_id", "potential_approver", "potential_assignee", "potential_manager", "potential_receiver", "updated_at", "login"]

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
        """Create an instance of RestV10ProjectsProjectIdActionPlansPartiesGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of vendor
        if self.vendor:
            _dict['vendor'] = self.vendor.to_dict()
        # set to None if vendor (nullable) is None
        # and model_fields_set contains the field
        if self.vendor is None and "vendor" in self.model_fields_set:
            _dict['vendor'] = None

        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['user_id'] = None

        # set to None if employee_id (nullable) is None
        # and model_fields_set contains the field
        if self.employee_id is None and "employee_id" in self.model_fields_set:
            _dict['employee_id'] = None

        # set to None if login (nullable) is None
        # and model_fields_set contains the field
        if self.login is None and "login" in self.model_fields_set:
            _dict['login'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdActionPlansPartiesGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "name": obj.get("name"),
            "vendor": RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManagerVendor.from_dict(obj["vendor"]) if obj.get("vendor") is not None else None,
            "user_id": obj.get("user_id"),
            "is_employee": obj.get("is_employee"),
            "employee_id": obj.get("employee_id"),
            "potential_approver": obj.get("potential_approver"),
            "potential_assignee": obj.get("potential_assignee"),
            "potential_manager": obj.get("potential_manager"),
            "potential_receiver": obj.get("potential_receiver"),
            "updated_at": obj.get("updated_at"),
            "login": obj.get("login")
        })
        return _obj


