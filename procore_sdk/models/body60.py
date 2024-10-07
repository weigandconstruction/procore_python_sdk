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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.body59_bim_view_folder import Body59BimViewFolder
from typing import Optional, Set
from typing_extensions import Self

class Body60(BaseModel):
    """
    Body60
    """ # noqa: E501
    project_id: StrictInt = Field(description="Unique identifier for the project.")
    view: Optional[StrictStr] = Field(default=None, description="Specify response schema view")
    bim_view_folders: List[Body59BimViewFolder] = Field(description="An array of nested BIM View Folder payload")
    __properties: ClassVar[List[str]] = ["project_id", "view", "bim_view_folders"]

    @field_validator('view')
    def view_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['compact', 'normal', 'extended']):
            raise ValueError("must be one of enum values ('compact', 'normal', 'extended')")
        return value

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
        """Create an instance of Body60 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bim_view_folders (list)
        _items = []
        if self.bim_view_folders:
            for _item_bim_view_folders in self.bim_view_folders:
                if _item_bim_view_folders:
                    _items.append(_item_bim_view_folders.to_dict())
            _dict['bim_view_folders'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Body60 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "project_id": obj.get("project_id"),
            "view": obj.get("view"),
            "bim_view_folders": [Body59BimViewFolder.from_dict(_item) for _item in obj["bim_view_folders"]] if obj.get("bim_view_folders") is not None else None
        })
        return _obj


