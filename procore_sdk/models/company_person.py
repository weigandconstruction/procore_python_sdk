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
from procore_sdk.models.company_person_contact import CompanyPersonContact
from typing import Optional, Set
from typing_extensions import Self

class CompanyPerson(BaseModel):
    """
    The Company Person object.
    """ # noqa: E501
    contact: Optional[CompanyPersonContact] = None
    employee_id: Optional[StrictStr] = Field(default=None, description="The employee id of the Company Person.")
    first_name: Optional[StrictStr] = Field(default=None, description="The first name of the Company Person.")
    id: Optional[StrictInt] = Field(default=None, description="The unique identifier of the Company Person.")
    is_employee: Optional[StrictBool] = Field(default=None, description="The employee status of the Company Person. If this property is set to true, the Company Person is an employee.")
    last_name: Optional[StrictStr] = Field(default=None, description="The last name of the Company Person.")
    user_id: Optional[StrictInt] = Field(default=None, description="The unique identifier if this Company Person represents a user. This value is set to NULL for a Reference User.")
    user_uuid: Optional[StrictInt] = Field(default=None, description="The user UUID for if this Company Person represents a user. This value is set to NULL for a Reference User.")
    work_classification_id: Optional[StrictInt] = Field(default=None, description="The unique identifier for the work classification of the Company Person.")
    origin_id: Optional[StrictStr] = Field(default=None, description="The Origin ID of the Company User")
    __properties: ClassVar[List[str]] = ["contact", "employee_id", "first_name", "id", "is_employee", "last_name", "user_id", "user_uuid", "work_classification_id", "origin_id"]

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
        """Create an instance of CompanyPerson from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
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

        # set to None if user_uuid (nullable) is None
        # and model_fields_set contains the field
        if self.user_uuid is None and "user_uuid" in self.model_fields_set:
            _dict['user_uuid'] = None

        # set to None if work_classification_id (nullable) is None
        # and model_fields_set contains the field
        if self.work_classification_id is None and "work_classification_id" in self.model_fields_set:
            _dict['work_classification_id'] = None

        # set to None if origin_id (nullable) is None
        # and model_fields_set contains the field
        if self.origin_id is None and "origin_id" in self.model_fields_set:
            _dict['origin_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CompanyPerson from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact": CompanyPersonContact.from_dict(obj["contact"]) if obj.get("contact") is not None else None,
            "employee_id": obj.get("employee_id"),
            "first_name": obj.get("first_name"),
            "id": obj.get("id"),
            "is_employee": obj.get("is_employee"),
            "last_name": obj.get("last_name"),
            "user_id": obj.get("user_id"),
            "user_uuid": obj.get("user_uuid"),
            "work_classification_id": obj.get("work_classification_id"),
            "origin_id": obj.get("origin_id")
        })
        return _obj


