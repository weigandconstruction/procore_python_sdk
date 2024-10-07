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
from procore_sdk.models.configurable_field_set_fields import ConfigurableFieldSetFields
from procore_sdk.models.configurable_field_set_sections_inner import ConfigurableFieldSetSectionsInner
from typing import Optional, Set
from typing_extensions import Self

class ConfigurableFieldSet(BaseModel):
    """
    ConfigurableFieldSet
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The unique identifier of the configurable field set.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the configurable field set.")
    type: Optional[StrictStr] = Field(default=None, description="The type of configurable field set")
    category: Optional[StrictStr] = Field(default=None, description="Specifies the category for the configurable field set if it exists or an empty string. This property was added for the ConfigurableFieldSet::Observations::Item class.")
    class_name: Optional[StrictStr] = Field(default=None, description="Specifies the class the configurable field set is associated with.")
    fields: Optional[ConfigurableFieldSetFields] = None
    sections: Optional[List[ConfigurableFieldSetSectionsInner]] = Field(default=None, description="An array of sections that are used for custom fields.")
    inspection_type_id: Optional[StrictInt] = Field(default=None, description="The unique identifier of the inspection type.")
    generic_tool_id: Optional[StrictInt] = Field(default=None, description="The unique idenfitier of the generic tool.")
    action_plan_type_id: Optional[StrictInt] = Field(default=None, description="The unique idenfitier of the action plan type.")
    __properties: ClassVar[List[str]] = ["id", "name", "type", "category", "class_name", "fields", "sections", "inspection_type_id", "generic_tool_id", "action_plan_type_id"]

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
        """Create an instance of ConfigurableFieldSet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fields
        if self.fields:
            _dict['fields'] = self.fields.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sections (list)
        _items = []
        if self.sections:
            for _item_sections in self.sections:
                if _item_sections:
                    _items.append(_item_sections.to_dict())
            _dict['sections'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if inspection_type_id (nullable) is None
        # and model_fields_set contains the field
        if self.inspection_type_id is None and "inspection_type_id" in self.model_fields_set:
            _dict['inspection_type_id'] = None

        # set to None if generic_tool_id (nullable) is None
        # and model_fields_set contains the field
        if self.generic_tool_id is None and "generic_tool_id" in self.model_fields_set:
            _dict['generic_tool_id'] = None

        # set to None if action_plan_type_id (nullable) is None
        # and model_fields_set contains the field
        if self.action_plan_type_id is None and "action_plan_type_id" in self.model_fields_set:
            _dict['action_plan_type_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurableFieldSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "category": obj.get("category"),
            "class_name": obj.get("class_name"),
            "fields": ConfigurableFieldSetFields.from_dict(obj["fields"]) if obj.get("fields") is not None else None,
            "sections": [ConfigurableFieldSetSectionsInner.from_dict(_item) for _item in obj["sections"]] if obj.get("sections") is not None else None,
            "inspection_type_id": obj.get("inspection_type_id"),
            "generic_tool_id": obj.get("generic_tool_id"),
            "action_plan_type_id": obj.get("action_plan_type_id")
        })
        return _obj


