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
from procore_sdk.models.rest_v10_companies_company_id_meeting_templates_get200_response_inner_agendas_inner_attachments_inner import RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner
from typing import Optional, Set
from typing_extensions import Self

class RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInner(BaseModel):
    """
    RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Id")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    category: Optional[StrictStr] = Field(default=None, description="Category")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    attachments: Optional[List[RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner]] = Field(default=None, description="Attachments")
    __properties: ClassVar[List[str]] = ["id", "title", "category", "description", "attachments"]

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
        """Create an instance of RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInner from a JSON string"""
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
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "category": obj.get("category"),
            "description": obj.get("description"),
            "attachments": [RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None
        })
        return _obj


