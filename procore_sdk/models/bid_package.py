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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BidPackage(BaseModel):
    """
    Bid Package Object
    """ # noqa: E501
    bid_due_date: datetime = Field(description="Due date")
    bid_email_message: StrictStr = Field(description="Bid package email information details")
    bid_web_message: StrictStr = Field(description="Bid package bidding instructions")
    title: StrictStr = Field(description="Bid package title")
    accounting_method: Optional[StrictStr] = Field(default=None, description="Bid package accounting method, either 'amount' or 'unit'")
    bid_submission_confirmation: Optional[StrictStr] = Field(default=None, description="Bid Package submission confirmation text")
    anticipated_award_date: Optional[date] = Field(default=None, description="Anticipated award date")
    number: Optional[StrictStr] = Field(default=None, description="Bid package number")
    distribution_ids: Optional[List[StrictInt]] = Field(default=None, description="Array of User IDs who will be on the bid package's distribution list")
    blind_bidding: Optional[StrictBool] = Field(default=None, description="Blind bidding enabled")
    pre_bid_walk_through_date: Optional[datetime] = Field(default=None, description="Scheduled pre-bid walkthrough date")
    pre_bid_walk_through_notes: Optional[StrictStr] = Field(default=None, description="Pre-bid walkthrough notes")
    enable_prebid_walkthrough: Optional[StrictBool] = Field(default=None, description="Pre-bid walkthrough enabled")
    manager_id: Optional[StrictInt] = Field(default=None, description="Login Information ID for Manager")
    __properties: ClassVar[List[str]] = ["bid_due_date", "bid_email_message", "bid_web_message", "title", "accounting_method", "bid_submission_confirmation", "anticipated_award_date", "number", "distribution_ids", "blind_bidding", "pre_bid_walk_through_date", "pre_bid_walk_through_notes", "enable_prebid_walkthrough", "manager_id"]

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
        """Create an instance of BidPackage from a JSON string"""
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
        """Create an instance of BidPackage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bid_due_date": obj.get("bid_due_date"),
            "bid_email_message": obj.get("bid_email_message"),
            "bid_web_message": obj.get("bid_web_message"),
            "title": obj.get("title"),
            "accounting_method": obj.get("accounting_method"),
            "bid_submission_confirmation": obj.get("bid_submission_confirmation"),
            "anticipated_award_date": obj.get("anticipated_award_date"),
            "number": obj.get("number"),
            "distribution_ids": obj.get("distribution_ids"),
            "blind_bidding": obj.get("blind_bidding"),
            "pre_bid_walk_through_date": obj.get("pre_bid_walk_through_date"),
            "pre_bid_walk_through_notes": obj.get("pre_bid_walk_through_notes"),
            "enable_prebid_walkthrough": obj.get("enable_prebid_walkthrough"),
            "manager_id": obj.get("manager_id")
        })
        return _obj


