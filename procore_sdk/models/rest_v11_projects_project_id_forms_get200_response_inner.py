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
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_created_by import RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner_attachment import RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner_fillable_pdf import RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner_permissions import RestV11ProjectsProjectIdFormsGet200ResponseInnerPermissions
from typing import Optional, Set
from typing_extensions import Self

class RestV11ProjectsProjectIdFormsGet200ResponseInner(BaseModel):
    """
    RestV11ProjectsProjectIdFormsGet200ResponseInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    created_at: Optional[datetime] = Field(default=None, description="Date created")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    form_template_id: Optional[StrictInt] = Field(default=None, description="Form Template ID")
    form_template_name: Optional[StrictStr] = Field(default=None, description="Form Template Name")
    name: Optional[StrictStr] = Field(default=None, description="Name")
    private: Optional[StrictBool] = Field(default=None, description="private")
    created_by: Optional[RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy] = None
    updated_at: Optional[datetime] = Field(default=None, description="Date updated")
    fillable_pdf: Optional[RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf] = None
    attachments: Optional[List[RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf]] = None
    thumbnail_url: Optional[StrictStr] = None
    viewable: Optional[StrictBool] = Field(default=None, description="Is Form viewable flag")
    viewable_document_id: Optional[StrictInt] = Field(default=None, description="Viewable Document ID")
    holder_class: Optional[StrictStr] = Field(default=None, description="Holder class")
    download_all_uuid: Optional[Dict[str, Any]] = None
    attachment: Optional[RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment] = None
    permissions: Optional[RestV11ProjectsProjectIdFormsGet200ResponseInnerPermissions] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "description", "form_template_id", "form_template_name", "name", "private", "created_by", "updated_at", "fillable_pdf", "attachments", "thumbnail_url", "viewable", "viewable_document_id", "holder_class", "download_all_uuid", "attachment", "permissions"]

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
        """Create an instance of RestV11ProjectsProjectIdFormsGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fillable_pdf
        if self.fillable_pdf:
            _dict['fillable_pdf'] = self.fillable_pdf.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of attachment
        if self.attachment:
            _dict['attachment'] = self.attachment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # set to None if viewable_document_id (nullable) is None
        # and model_fields_set contains the field
        if self.viewable_document_id is None and "viewable_document_id" in self.model_fields_set:
            _dict['viewable_document_id'] = None

        # set to None if download_all_uuid (nullable) is None
        # and model_fields_set contains the field
        if self.download_all_uuid is None and "download_all_uuid" in self.model_fields_set:
            _dict['download_all_uuid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV11ProjectsProjectIdFormsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "form_template_id": obj.get("form_template_id"),
            "form_template_name": obj.get("form_template_name"),
            "name": obj.get("name"),
            "private": obj.get("private"),
            "created_by": RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "updated_at": obj.get("updated_at"),
            "fillable_pdf": RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf.from_dict(obj["fillable_pdf"]) if obj.get("fillable_pdf") is not None else None,
            "attachments": [RestV11ProjectsProjectIdFormsGet200ResponseInnerFillablePdf.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "thumbnail_url": obj.get("thumbnail_url"),
            "viewable": obj.get("viewable"),
            "viewable_document_id": obj.get("viewable_document_id"),
            "holder_class": obj.get("holder_class"),
            "download_all_uuid": obj.get("download_all_uuid"),
            "attachment": RestV11ProjectsProjectIdFormsGet200ResponseInnerAttachment.from_dict(obj["attachment"]) if obj.get("attachment") is not None else None,
            "permissions": RestV11ProjectsProjectIdFormsGet200ResponseInnerPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None
        })
        return _obj


