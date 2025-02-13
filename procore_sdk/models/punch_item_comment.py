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
from procore_sdk.models.punch_item_comment_attachments_inner import PunchItemCommentAttachmentsInner
from procore_sdk.models.punch_item_comment_creator import PunchItemCommentCreator
from typing import Optional, Set
from typing_extensions import Self

class PunchItemComment(BaseModel):
    """
    PunchItemComment
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID of the Punch Item Comment")
    attachments: Optional[List[PunchItemCommentAttachmentsInner]] = Field(default=None, description="Punch Item Comment Attachments")
    body: Optional[StrictStr] = Field(default=None, description="Punch Item Comment Body")
    created_at: Optional[StrictStr] = Field(default=None, description="Date the Punch Item Comment was created")
    created_by: Optional[PunchItemCommentCreator] = None
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "attachments", "body", "created_at", "created_by", "type"]

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
        """Create an instance of PunchItemComment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PunchItemComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "attachments": [PunchItemCommentAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "body": obj.get("body"),
            "created_at": obj.get("created_at"),
            "created_by": PunchItemCommentCreator.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "type": obj.get("type")
        })
        return _obj


