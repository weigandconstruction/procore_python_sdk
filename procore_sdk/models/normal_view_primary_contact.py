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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NormalViewPrimaryContact(BaseModel):
    """
    Primary contact
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    first_name: Optional[StrictStr] = Field(default=None, description="First name")
    last_name: Optional[StrictStr] = Field(default=None, description="Last name")
    business_phone: Optional[StrictStr] = Field(default=None, description="Business phone")
    business_phone_extension: Optional[StrictInt] = Field(default=None, description="Business phone extension")
    fax_number: Optional[StrictStr] = Field(default=None, description="Fax number")
    mobile_phone: Optional[StrictStr] = Field(default=None, description="Mobile phone")
    email_address: Optional[StrictStr] = Field(default=None, description="Email")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    __properties: ClassVar[List[str]] = ["id", "first_name", "last_name", "business_phone", "business_phone_extension", "fax_number", "mobile_phone", "email_address", "created_at", "updated_at"]

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
        """Create an instance of NormalViewPrimaryContact from a JSON string"""
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
        # set to None if business_phone (nullable) is None
        # and model_fields_set contains the field
        if self.business_phone is None and "business_phone" in self.model_fields_set:
            _dict['business_phone'] = None

        # set to None if business_phone_extension (nullable) is None
        # and model_fields_set contains the field
        if self.business_phone_extension is None and "business_phone_extension" in self.model_fields_set:
            _dict['business_phone_extension'] = None

        # set to None if fax_number (nullable) is None
        # and model_fields_set contains the field
        if self.fax_number is None and "fax_number" in self.model_fields_set:
            _dict['fax_number'] = None

        # set to None if mobile_phone (nullable) is None
        # and model_fields_set contains the field
        if self.mobile_phone is None and "mobile_phone" in self.model_fields_set:
            _dict['mobile_phone'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NormalViewPrimaryContact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "business_phone": obj.get("business_phone"),
            "business_phone_extension": obj.get("business_phone_extension"),
            "fax_number": obj.get("fax_number"),
            "mobile_phone": obj.get("mobile_phone"),
            "email_address": obj.get("email_address"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


