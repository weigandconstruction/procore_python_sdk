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
from typing import Optional, Set
from typing_extensions import Self

class InspectionType2(BaseModel):
    """
    InspectionType2
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    name: Optional[StrictStr] = Field(default=None, description="Name")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp of creation")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp of last update")
    audit_transaction_timestamp: Optional[datetime] = Field(default=None, description="Timestamp of audit")
    source_id: Optional[StrictInt] = None
    deleted_at: Optional[datetime] = Field(default=None, description="Timestamp of deletion")
    company_id: Optional[StrictInt] = Field(default=None, description="Company ID")
    is_deletable: Optional[StrictBool] = Field(default=None, description="Is deletable")
    __properties: ClassVar[List[str]] = ["id", "name", "created_at", "updated_at", "audit_transaction_timestamp", "source_id", "deleted_at", "company_id", "is_deletable"]

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
        """Create an instance of InspectionType2 from a JSON string"""
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
        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['source_id'] = None

        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deleted_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InspectionType2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "audit_transaction_timestamp": obj.get("audit_transaction_timestamp"),
            "source_id": obj.get("source_id"),
            "deleted_at": obj.get("deleted_at"),
            "company_id": obj.get("company_id"),
            "is_deletable": obj.get("is_deletable")
        })
        return _obj


