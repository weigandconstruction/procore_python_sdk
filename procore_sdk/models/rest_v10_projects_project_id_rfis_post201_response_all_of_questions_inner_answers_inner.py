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
from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner_attachments_inner import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner(BaseModel):
    """
    RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    official: Optional[StrictBool] = Field(default=None, description="Official response, true if official")
    answer_date: Optional[datetime] = Field(default=None, description="Date")
    plain_text_body: Optional[StrictStr] = Field(default=None, description="Plain text body")
    rich_text_body: Optional[StrictStr] = Field(default=None, description="Rich text body")
    created_by: Optional[StrictStr] = Field(default=None, description="Creator name")
    created_by_id: Optional[StrictInt] = Field(default=None, description="Creator ID")
    attachments: Optional[List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]] = Field(default=None, description="Attachments")
    __properties: ClassVar[List[str]] = ["id", "official", "answer_date", "plain_text_body", "rich_text_body", "created_by", "created_by_id", "attachments"]

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
        """Create an instance of RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "official": obj.get("official"),
            "answer_date": obj.get("answer_date"),
            "plain_text_body": obj.get("plain_text_body"),
            "rich_text_body": obj.get("rich_text_body"),
            "created_by": obj.get("created_by"),
            "created_by_id": obj.get("created_by_id"),
            "attachments": [RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None
        })
        return _obj


