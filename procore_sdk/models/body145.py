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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.body145_alternates_inner import Body145AlternatesInner
from procore_sdk.models.body145_base_bid_inner import Body145BaseBidInner
from typing import Optional, Set
from typing_extensions import Self

class Body145(BaseModel):
    """
    Body145
    """ # noqa: E501
    title: StrictStr = Field(description="Bid Form Title")
    base_bid: Optional[List[Body145BaseBidInner]] = Field(default=None, description="Base Bids")
    alternates: Optional[List[Body145AlternatesInner]] = Field(default=None, description="Alternate bids")
    __properties: ClassVar[List[str]] = ["title", "base_bid", "alternates"]

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
        """Create an instance of Body145 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in base_bid (list)
        _items = []
        if self.base_bid:
            for _item_base_bid in self.base_bid:
                if _item_base_bid:
                    _items.append(_item_base_bid.to_dict())
            _dict['base_bid'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in alternates (list)
        _items = []
        if self.alternates:
            for _item_alternates in self.alternates:
                if _item_alternates:
                    _items.append(_item_alternates.to_dict())
            _dict['alternates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Body145 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "base_bid": [Body145BaseBidInner.from_dict(_item) for _item in obj["base_bid"]] if obj.get("base_bid") is not None else None,
            "alternates": [Body145AlternatesInner.from_dict(_item) for _item in obj["alternates"]] if obj.get("alternates") is not None else None
        })
        return _obj


