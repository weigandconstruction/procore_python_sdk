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

class Company(BaseModel):
    """
    Company
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Company id")
    name: Optional[StrictStr] = Field(default=None, description="Company name")
    is_active: Optional[StrictBool] = Field(default=None, description="Company is active status")
    logo_url: Optional[StrictStr] = Field(default=None, description="Company Logo URL")
    pcn_business_experience: Optional[StrictBool] = Field(default=None, description="Company has business experience enabled")
    my_company: Optional[StrictBool] = Field(default=None, description="The current user is an active employee of this company. This will only return as true for a single company in the response.")
    __properties: ClassVar[List[str]] = ["id", "name", "is_active", "logo_url", "pcn_business_experience", "my_company"]

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
        """Create an instance of Company from a JSON string"""
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
        # set to None if pcn_business_experience (nullable) is None
        # and model_fields_set contains the field
        if self.pcn_business_experience is None and "pcn_business_experience" in self.model_fields_set:
            _dict['pcn_business_experience'] = None

        # set to None if my_company (nullable) is None
        # and model_fields_set contains the field
        if self.my_company is None and "my_company" in self.model_fields_set:
            _dict['my_company'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Company from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "is_active": obj.get("is_active"),
            "logo_url": obj.get("logo_url"),
            "pcn_business_experience": obj.get("pcn_business_experience"),
            "my_company": obj.get("my_company")
        })
        return _obj


