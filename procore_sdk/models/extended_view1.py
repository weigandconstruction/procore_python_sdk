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
from procore_sdk.models.extended_view_work_classification import ExtendedViewWorkClassification
from typing import Optional, Set
from typing_extensions import Self

class ExtendedView1(BaseModel):
    """
    Customer signee party
    """ # noqa: E501
    employee_id: Optional[StrictStr] = Field(default=None, description="Employee ID for the Party Person")
    first_name: Optional[StrictStr] = Field(default=None, description="Party Person first name")
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the Party Person.")
    is_employee: Optional[StrictBool] = Field(default=None, description="Employee status for the Party Person")
    last_name: Optional[StrictStr] = Field(default=None, description="Party Person last name")
    user_id: Optional[StrictInt] = Field(default=None, description="User ID if this Party Person represents a User. NULL for a Reference User.")
    work_classification: Optional[ExtendedViewWorkClassification] = None
    __properties: ClassVar[List[str]] = ["employee_id", "first_name", "id", "is_employee", "last_name", "user_id", "work_classification"]

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
        """Create an instance of ExtendedView1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of work_classification
        if self.work_classification:
            _dict['work_classification'] = self.work_classification.to_dict()
        # set to None if employee_id (nullable) is None
        # and model_fields_set contains the field
        if self.employee_id is None and "employee_id" in self.model_fields_set:
            _dict['employee_id'] = None

        # set to None if is_employee (nullable) is None
        # and model_fields_set contains the field
        if self.is_employee is None and "is_employee" in self.model_fields_set:
            _dict['is_employee'] = None

        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['user_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExtendedView1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "employee_id": obj.get("employee_id"),
            "first_name": obj.get("first_name"),
            "id": obj.get("id"),
            "is_employee": obj.get("is_employee"),
            "last_name": obj.get("last_name"),
            "user_id": obj.get("user_id"),
            "work_classification": ExtendedViewWorkClassification.from_dict(obj["work_classification"]) if obj.get("work_classification") is not None else None
        })
        return _obj


