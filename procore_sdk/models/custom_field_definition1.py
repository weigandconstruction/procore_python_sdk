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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.custom_field_lov_entry import CustomFieldLovEntry
from typing import Optional, Set
from typing_extensions import Self

class CustomFieldDefinition1(BaseModel):
    """
    CustomFieldDefinition1
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Custom Field Definition ID")
    label: Optional[StrictStr] = Field(default=None, description="Custom Field Definition Label")
    active: Optional[StrictBool] = Field(default=None, description="Whether or not the Custom Field Definition is active")
    company_id: Optional[StrictInt] = Field(default=None, description="Company ID")
    data_type: Optional[StrictStr] = Field(default=None, description="Type of Custom field")
    variant: Optional[StrictStr] = Field(default=None, description="The variant type of the Custom Field")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    default_value: Optional[StrictStr] = Field(default=None, description="Text displayed on Read Only variant")
    configurable_field_sets_count: Optional[StrictInt] = Field(default=None, description="Number of Configurable Field Sets associated with the Custom Field")
    custom_field_lov_entries: Optional[List[CustomFieldLovEntry]] = None
    __properties: ClassVar[List[str]] = ["id", "label", "active", "company_id", "data_type", "variant", "description", "default_value", "configurable_field_sets_count", "custom_field_lov_entries"]

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
        """Create an instance of CustomFieldDefinition1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in custom_field_lov_entries (list)
        _items = []
        if self.custom_field_lov_entries:
            for _item_custom_field_lov_entries in self.custom_field_lov_entries:
                if _item_custom_field_lov_entries:
                    _items.append(_item_custom_field_lov_entries.to_dict())
            _dict['custom_field_lov_entries'] = _items
        # set to None if variant (nullable) is None
        # and model_fields_set contains the field
        if self.variant is None and "variant" in self.model_fields_set:
            _dict['variant'] = None

        # set to None if default_value (nullable) is None
        # and model_fields_set contains the field
        if self.default_value is None and "default_value" in self.model_fields_set:
            _dict['default_value'] = None

        # set to None if configurable_field_sets_count (nullable) is None
        # and model_fields_set contains the field
        if self.configurable_field_sets_count is None and "configurable_field_sets_count" in self.model_fields_set:
            _dict['configurable_field_sets_count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomFieldDefinition1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "active": obj.get("active"),
            "company_id": obj.get("company_id"),
            "data_type": obj.get("data_type"),
            "variant": obj.get("variant"),
            "description": obj.get("description"),
            "default_value": obj.get("default_value"),
            "configurable_field_sets_count": obj.get("configurable_field_sets_count"),
            "custom_field_lov_entries": [CustomFieldLovEntry.from_dict(_item) for _item in obj["custom_field_lov_entries"]] if obj.get("custom_field_lov_entries") is not None else None
        })
        return _obj


