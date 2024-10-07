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
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.checklist_comment_created_by import ChecklistCommentCreatedBy
from procore_sdk.models.checklist_item_attachment_attachment import ChecklistItemAttachmentAttachment
from typing import Optional, Set
from typing_extensions import Self

class ChecklistItemAttachment(BaseModel):
    """
    ChecklistItemAttachment
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Attachment ID")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp of creation")
    created_by: Optional[ChecklistCommentCreatedBy] = None
    attachment: Optional[ChecklistItemAttachmentAttachment] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "created_by", "attachment"]

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
        """Create an instance of ChecklistItemAttachment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attachment
        if self.attachment:
            _dict['attachment'] = self.attachment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChecklistItemAttachment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "created_by": ChecklistCommentCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "attachment": ChecklistItemAttachmentAttachment.from_dict(obj["attachment"]) if obj.get("attachment") is not None else None
        })
        return _obj


