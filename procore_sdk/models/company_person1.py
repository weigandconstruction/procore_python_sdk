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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CompanyPerson1(BaseModel):
    """
    CompanyPerson1
    """ # noqa: E501
    first_name: Optional[StrictStr] = Field(default=None, description="The First Name of the Company Person")
    last_name: StrictStr = Field(description="The Last Name of the Company Person")
    is_employee: Optional[StrictBool] = Field(default=False, description="The Employee status of the Company Person")
    employee_id: Optional[StrictStr] = Field(default=None, description="The Employee ID of the Company Person")
    active: Optional[StrictBool] = Field(default=None, description="The active status of the Company Person")
    origin_id: Optional[StrictStr] = Field(default=None, description="The Origin ID of the Company User")
    __properties: ClassVar[List[str]] = ["first_name", "last_name", "is_employee", "employee_id", "active", "origin_id"]

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
        """Create an instance of CompanyPerson1 from a JSON string"""
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
        """Create an instance of CompanyPerson1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "is_employee": obj.get("is_employee") if obj.get("is_employee") is not None else False,
            "employee_id": obj.get("employee_id"),
            "active": obj.get("active"),
            "origin_id": obj.get("origin_id")
        })
        return _obj


