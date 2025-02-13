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
from procore_sdk.models.rest_v10_submittal_approvers_id_patch_request_submittal_approver_associated_attachments_inner import RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner
from procore_sdk.models.rest_v10_submittal_approvers_id_patch_request_submittal_approver_forward_to import RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo
from typing import Optional, Set
from typing_extensions import Self

class RestV10SubmittalApproversIdPatchRequestSubmittalApprover(BaseModel):
    """
    RestV10SubmittalApproversIdPatchRequestSubmittalApprover
    """ # noqa: E501
    attachments_to_upload: Optional[List[StrictStr]] = Field(default=None, description="Submittal Approver's Attachments. To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments_to_upload[]` as files.")
    attachment_ids: Optional[List[StrictInt]] = Field(default=None, description="Submittal Approver's Attachment IDs. The Attachments specified here will be saved as attachments through the request.")
    comment: Optional[StrictStr] = None
    submittal_response_id: StrictInt
    sent_date: Optional[StrictStr] = Field(default=None, description="Parameter is only available to admins.")
    returned_date: Optional[StrictStr] = Field(default=None, description="Parameter is only available to admins.")
    forward_to: Optional[RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo] = None
    associated_attachments: Optional[List[RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner]] = Field(default=None, description="Submital Approver's Attachments to be carried forward. The Attachments specified here will be carried forward to the next person in the workflow.")
    __properties: ClassVar[List[str]] = ["attachments_to_upload", "attachment_ids", "comment", "submittal_response_id", "sent_date", "returned_date", "forward_to", "associated_attachments"]

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
        """Create an instance of RestV10SubmittalApproversIdPatchRequestSubmittalApprover from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of forward_to
        if self.forward_to:
            _dict['forward_to'] = self.forward_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in associated_attachments (list)
        _items = []
        if self.associated_attachments:
            for _item_associated_attachments in self.associated_attachments:
                if _item_associated_attachments:
                    _items.append(_item_associated_attachments.to_dict())
            _dict['associated_attachments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10SubmittalApproversIdPatchRequestSubmittalApprover from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attachments_to_upload": obj.get("attachments_to_upload"),
            "attachment_ids": obj.get("attachment_ids"),
            "comment": obj.get("comment"),
            "submittal_response_id": obj.get("submittal_response_id"),
            "sent_date": obj.get("sent_date"),
            "returned_date": obj.get("returned_date"),
            "forward_to": RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo.from_dict(obj["forward_to"]) if obj.get("forward_to") is not None else None,
            "associated_attachments": [RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner.from_dict(_item) for _item in obj["associated_attachments"]] if obj.get("associated_attachments") is not None else None
        })
        return _obj


