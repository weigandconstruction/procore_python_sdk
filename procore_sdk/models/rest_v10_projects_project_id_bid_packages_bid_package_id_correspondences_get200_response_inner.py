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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.correspondence_attachments_inner import CorrespondenceAttachmentsInner
from procore_sdk.models.correspondence_from import CorrespondenceFrom
from procore_sdk.models.correspondence_recipients_inner_inner import CorrespondenceRecipientsInnerInner
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner(BaseModel):
    """
    RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    bid_package_id: Optional[StrictInt] = Field(default=None, description="Bid package ID")
    bid_package_title: Optional[StrictStr] = Field(default=None, description="Bid package title")
    created_at: Optional[StrictStr] = Field(default=None, description="Correspondence created-at")
    subject: Optional[StrictStr] = Field(default=None, description="Subject within Correspondence")
    attachments: Optional[List[CorrespondenceAttachmentsInner]] = None
    message: Optional[StrictStr] = Field(default=None, description="Body of Correspondence")
    recipients: Optional[List[List[CorrespondenceRecipientsInnerInner]]] = Field(default=None, description="List of recipient names Correspondence was sent to")
    var_from: Optional[CorrespondenceFrom] = Field(default=None, alias="from")
    __properties: ClassVar[List[str]] = ["id", "bid_package_id", "bid_package_title", "created_at", "subject", "attachments", "message", "recipients", "from"]

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
        """Create an instance of RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recipients (list of list)
        _items = []
        if self.recipients:
            for _item_recipients in self.recipients:
                if _item_recipients:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item_recipients if _inner_item is not None]
                    )
            _dict['recipients'] = _items
        # override the default output from pydantic by calling `to_dict()` of var_from
        if self.var_from:
            _dict['from'] = self.var_from.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "bid_package_id": obj.get("bid_package_id"),
            "bid_package_title": obj.get("bid_package_title"),
            "created_at": obj.get("created_at"),
            "subject": obj.get("subject"),
            "attachments": [CorrespondenceAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "message": obj.get("message"),
            "recipients": [
                    [CorrespondenceRecipientsInnerInner.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["recipients"]
                ] if obj.get("recipients") is not None else None,
            "from": CorrespondenceFrom.from_dict(obj["from"]) if obj.get("from") is not None else None
        })
        return _obj


