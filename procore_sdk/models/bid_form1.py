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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.bid_form_base_bid_section_bid_form_items_inner import BidFormBaseBidSectionBidFormItemsInner
from procore_sdk.models.bid_form_base_bid_section_section_totals_inner import BidFormBaseBidSectionSectionTotalsInner
from typing import Optional, Set
from typing_extensions import Self

class BidForm1(BaseModel):
    """
    Bid Form
    """ # noqa: E501
    company_id: Optional[StrictInt] = Field(default=None, description="Company ID")
    project_id: Optional[StrictInt] = Field(default=None, description="Project ID")
    accounting_method: Optional[StrictStr] = None
    company_name: Optional[StrictStr] = Field(default=None, description="Company Name")
    project_name: Optional[StrictStr] = Field(default=None, description="Project Name")
    base_bid_totals: Optional[List[BidFormBaseBidSectionSectionTotalsInner]] = None
    base_bid: Optional[List[BidFormBaseBidSectionBidFormItemsInner]] = None
    alternates: Optional[List[BidFormBaseBidSectionBidFormItemsInner]] = None
    lump_sum_enabled: Optional[StrictBool] = Field(default=None, description="Lump Sum Enabled")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    __properties: ClassVar[List[str]] = ["company_id", "project_id", "accounting_method", "company_name", "project_name", "base_bid_totals", "base_bid", "alternates", "lump_sum_enabled", "title"]

    @field_validator('accounting_method')
    def accounting_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['amount', 'unit']):
            raise ValueError("must be one of enum values ('amount', 'unit')")
        return value

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
        """Create an instance of BidForm1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in base_bid_totals (list)
        _items = []
        if self.base_bid_totals:
            for _item_base_bid_totals in self.base_bid_totals:
                if _item_base_bid_totals:
                    _items.append(_item_base_bid_totals.to_dict())
            _dict['base_bid_totals'] = _items
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
        """Create an instance of BidForm1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "company_id": obj.get("company_id"),
            "project_id": obj.get("project_id"),
            "accounting_method": obj.get("accounting_method"),
            "company_name": obj.get("company_name"),
            "project_name": obj.get("project_name"),
            "base_bid_totals": [BidFormBaseBidSectionSectionTotalsInner.from_dict(_item) for _item in obj["base_bid_totals"]] if obj.get("base_bid_totals") is not None else None,
            "base_bid": [BidFormBaseBidSectionBidFormItemsInner.from_dict(_item) for _item in obj["base_bid"]] if obj.get("base_bid") is not None else None,
            "alternates": [BidFormBaseBidSectionBidFormItemsInner.from_dict(_item) for _item in obj["alternates"]] if obj.get("alternates") is not None else None,
            "lump_sum_enabled": obj.get("lump_sum_enabled"),
            "title": obj.get("title")
        })
        return _obj


