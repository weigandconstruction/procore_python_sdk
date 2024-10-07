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
from typing import Optional, Set
from typing_extensions import Self

class ProjectUser(BaseModel):
    """
    ProjectUser
    """ # noqa: E501
    address: Optional[StrictStr] = Field(default=None, description="The street Address of the Project User")
    avatar: Optional[StrictStr] = Field(default=None, description="Project User Avatar. To upload avatar you must upload whole payload as `multipart/form-data` content-type and specify each parameter as form-data together with `user[avatar]` as file.")
    business_phone: Optional[StrictStr] = Field(default=None, description="The Business Phone number of the Project User")
    business_phone_extension: Optional[StrictInt] = Field(default=None, description="The Business Phone Extension of the Project User")
    city: Optional[StrictStr] = Field(default=None, description="The City in which the Project User resides")
    country_code: Optional[StrictStr] = Field(default=None, description="The Country Code of the Project User (ISO-3166 Alpha-2 format)")
    email_address: StrictStr = Field(description="The Email Address of the Project User")
    email_signature: Optional[StrictStr] = Field(default=None, description="The Email Signature of the Project User")
    employee_id: Optional[StrictStr] = Field(default=None, description="The Employee ID of the Project User")
    fax_number: Optional[StrictStr] = Field(default=None, description="The Fax Number of the Project User")
    first_name: Optional[StrictStr] = Field(default=None, description="The First Name of the Project User")
    initials: Optional[StrictStr] = Field(default=None, description="The Initials of the Project User")
    is_active: Optional[StrictBool] = Field(default=None, description="The Active status of the Project User")
    is_employee: Optional[StrictBool] = Field(default=False, description="The Employee status of the Project User")
    job_title: Optional[StrictStr] = Field(default=None, description="The Job Title of the Project User")
    last_name: StrictStr = Field(description="The Last Name of the Project User")
    mobile_phone: Optional[StrictStr] = Field(default=None, description="The Mobile Phone number of the Project User")
    notes: Optional[StrictStr] = Field(default=None, description="The Notes (notes/keywords/tags) of the Project User")
    permission_template_id: Optional[StrictInt] = Field(default=None, description="The Permission Template ID of the Project User")
    state_code: Optional[StrictStr] = Field(default=None, description="The State Code of the Project User (ISO-3166 Alpha-2 format)")
    vendor_id: Optional[StrictInt] = Field(default=None, description="The Vendor ID of the Project User")
    zip: Optional[StrictStr] = Field(default=None, description="The Zip Code of the Project User")
    __properties: ClassVar[List[str]] = ["address", "avatar", "business_phone", "business_phone_extension", "city", "country_code", "email_address", "email_signature", "employee_id", "fax_number", "first_name", "initials", "is_active", "is_employee", "job_title", "last_name", "mobile_phone", "notes", "permission_template_id", "state_code", "vendor_id", "zip"]

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
        """Create an instance of ProjectUser from a JSON string"""
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
        """Create an instance of ProjectUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "avatar": obj.get("avatar"),
            "business_phone": obj.get("business_phone"),
            "business_phone_extension": obj.get("business_phone_extension"),
            "city": obj.get("city"),
            "country_code": obj.get("country_code"),
            "email_address": obj.get("email_address"),
            "email_signature": obj.get("email_signature"),
            "employee_id": obj.get("employee_id"),
            "fax_number": obj.get("fax_number"),
            "first_name": obj.get("first_name"),
            "initials": obj.get("initials"),
            "is_active": obj.get("is_active"),
            "is_employee": obj.get("is_employee") if obj.get("is_employee") is not None else False,
            "job_title": obj.get("job_title"),
            "last_name": obj.get("last_name"),
            "mobile_phone": obj.get("mobile_phone"),
            "notes": obj.get("notes"),
            "permission_template_id": obj.get("permission_template_id"),
            "state_code": obj.get("state_code"),
            "vendor_id": obj.get("vendor_id"),
            "zip": obj.get("zip")
        })
        return _obj


