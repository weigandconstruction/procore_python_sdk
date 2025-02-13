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

class RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner(BaseModel):
    """
    Invoice Change History
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    column: Optional[StrictStr] = Field(default=None, description="Name of the column changed")
    old_value: Optional[StrictStr] = Field(default=None, description="Value of the column before change")
    new_value: Optional[StrictStr] = Field(default=None, description="Value of the column after change")
    action_by: Optional[StrictStr] = Field(default=None, description="Name of the person who made the change")
    action_by_id: Optional[StrictInt] = Field(default=None, description="ID of the person who made the change")
    created_at: Optional[datetime] = Field(default=None, description="Created date")
    ref_id: Optional[StrictInt] = Field(default=None, description="The reference ID for the change")
    ref_type: Optional[StrictStr] = Field(default=None, description="The rereference type for the change")
    __properties: ClassVar[List[str]] = ["id", "column", "old_value", "new_value", "action_by", "action_by_id", "created_at", "ref_id", "ref_type"]

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
        """Create an instance of RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner from a JSON string"""
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
        """Create an instance of RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "column": obj.get("column"),
            "old_value": obj.get("old_value"),
            "new_value": obj.get("new_value"),
            "action_by": obj.get("action_by"),
            "action_by_id": obj.get("action_by_id"),
            "created_at": obj.get("created_at"),
            "ref_id": obj.get("ref_id"),
            "ref_type": obj.get("ref_type")
        })
        return _obj


