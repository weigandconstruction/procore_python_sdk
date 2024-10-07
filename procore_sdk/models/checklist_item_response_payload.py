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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.checklist_item_response_payload_response_option import ChecklistItemResponsePayloadResponseOption
from typing import Optional, Set
from typing_extensions import Self

class ChecklistItemResponsePayload(BaseModel):
    """
    ChecklistItemResponsePayload
    """ # noqa: E501
    text_value: Optional[StrictStr] = Field(default=None, description="Response for an Open Ended Text Item")
    number_value: Optional[StrictInt] = Field(default=None, description="Response for an Open Ended Number Item")
    date_value: Optional[date] = Field(default=None, description="Response for an Open Ended Date Item")
    response_option: Optional[ChecklistItemResponsePayloadResponseOption] = None
    __properties: ClassVar[List[str]] = ["text_value", "number_value", "date_value", "response_option"]

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
        """Create an instance of ChecklistItemResponsePayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of response_option
        if self.response_option:
            _dict['response_option'] = self.response_option.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChecklistItemResponsePayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "text_value": obj.get("text_value"),
            "number_value": obj.get("number_value"),
            "date_value": obj.get("date_value"),
            "response_option": ChecklistItemResponsePayloadResponseOption.from_dict(obj["response_option"]) if obj.get("response_option") is not None else None
        })
        return _obj


