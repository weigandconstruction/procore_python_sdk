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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.checklist_alternative_response_set import ChecklistAlternativeResponseSet
from procore_sdk.models.inspection_type1 import InspectionType1
from procore_sdk.models.project_checklist_template1_synced_to import ProjectChecklistTemplate1SyncedTo
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_created_by import RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post201_response_all_of_sections_inner import RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_attachments_inner import RestV10WorkOrderContractsPost201ResponseAttachmentsInner
from procore_sdk.models.trade import Trade
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatch200Response(BaseModel):
    """
    RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatch200Response
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    name: Optional[StrictStr] = Field(default=None, description="Name")
    company_description: Optional[StrictStr] = Field(default=None, description="Company Description")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    inspection_type: Optional[InspectionType1] = None
    trade: Optional[Trade] = None
    synced_to: Optional[ProjectChecklistTemplate1SyncedTo] = None
    created_at: Optional[datetime] = Field(default=None, description="Timestamp of creation")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp of last update")
    alternative_response_set_id: Optional[StrictInt] = Field(default=None, description="The ID of the associated Alternative Response Set (if null, the default response set is being used)")
    created_by: Optional[RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy] = None
    attachments: Optional[List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]] = Field(default=None, description="Attachments")
    response_set: Optional[ChecklistAlternativeResponseSet] = None
    sections: Optional[List[RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInner]] = Field(default=None, description="Sections")
    company_attachments: Optional[List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]] = Field(default=None, description="Company attachments")
    __properties: ClassVar[List[str]] = ["id", "name", "company_description", "description", "inspection_type", "trade", "synced_to", "created_at", "updated_at", "alternative_response_set_id", "created_by", "attachments", "response_set", "sections", "company_attachments"]

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
        """Create an instance of RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatch200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of inspection_type
        if self.inspection_type:
            _dict['inspection_type'] = self.inspection_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trade
        if self.trade:
            _dict['trade'] = self.trade.to_dict()
        # override the default output from pydantic by calling `to_dict()` of synced_to
        if self.synced_to:
            _dict['synced_to'] = self.synced_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of response_set
        if self.response_set:
            _dict['response_set'] = self.response_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sections (list)
        _items = []
        if self.sections:
            for _item_sections in self.sections:
                if _item_sections:
                    _items.append(_item_sections.to_dict())
            _dict['sections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in company_attachments (list)
        _items = []
        if self.company_attachments:
            for _item_company_attachments in self.company_attachments:
                if _item_company_attachments:
                    _items.append(_item_company_attachments.to_dict())
            _dict['company_attachments'] = _items
        # set to None if company_description (nullable) is None
        # and model_fields_set contains the field
        if self.company_description is None and "company_description" in self.model_fields_set:
            _dict['company_description'] = None

        # set to None if trade (nullable) is None
        # and model_fields_set contains the field
        if self.trade is None and "trade" in self.model_fields_set:
            _dict['trade'] = None

        # set to None if synced_to (nullable) is None
        # and model_fields_set contains the field
        if self.synced_to is None and "synced_to" in self.model_fields_set:
            _dict['synced_to'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatch200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "company_description": obj.get("company_description"),
            "description": obj.get("description"),
            "inspection_type": InspectionType1.from_dict(obj["inspection_type"]) if obj.get("inspection_type") is not None else None,
            "trade": Trade.from_dict(obj["trade"]) if obj.get("trade") is not None else None,
            "synced_to": ProjectChecklistTemplate1SyncedTo.from_dict(obj["synced_to"]) if obj.get("synced_to") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "alternative_response_set_id": obj.get("alternative_response_set_id"),
            "created_by": RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "attachments": [RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "response_set": ChecklistAlternativeResponseSet.from_dict(obj["response_set"]) if obj.get("response_set") is not None else None,
            "sections": [RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInner.from_dict(_item) for _item in obj["sections"]] if obj.get("sections") is not None else None,
            "company_attachments": [RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(_item) for _item in obj["company_attachments"]] if obj.get("company_attachments") is not None else None
        })
        return _obj


