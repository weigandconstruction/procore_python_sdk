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
from procore_sdk.models.checklist_template_item_response_set1 import ChecklistTemplateItemResponseSet1
from procore_sdk.models.rest_v11_projects_project_id_checklist_list_templates_id_get200_response_all_of_sections_inner_all_of_items_inner_all_of_synced_to import RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInnerAllOfSyncedTo
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner(BaseModel):
    """
    RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    name: Optional[StrictStr] = Field(default=None, description="Name")
    section_id: Optional[StrictInt] = Field(default=None, description="Checklist Template Section ID")
    position: Optional[StrictInt] = Field(default=None, description="Position")
    response_set: Optional[ChecklistTemplateItemResponseSet1] = None
    details: Optional[StrictStr] = Field(default=None, description="Additional information about item")
    synced_to: Optional[RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInnerAllOfSyncedTo] = None
    __properties: ClassVar[List[str]] = ["id", "name", "section_id", "position", "response_set", "details", "synced_to"]

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
        """Create an instance of RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of response_set
        if self.response_set:
            _dict['response_set'] = self.response_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of synced_to
        if self.synced_to:
            _dict['synced_to'] = self.synced_to.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfSectionsInnerAllOfItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "section_id": obj.get("section_id"),
            "position": obj.get("position"),
            "response_set": ChecklistTemplateItemResponseSet1.from_dict(obj["response_set"]) if obj.get("response_set") is not None else None,
            "details": obj.get("details"),
            "synced_to": RestV11ProjectsProjectIdChecklistListTemplatesIdGet200ResponseAllOfSectionsInnerAllOfItemsInnerAllOfSyncedTo.from_dict(obj["synced_to"]) if obj.get("synced_to") is not None else None
        })
        return _obj


