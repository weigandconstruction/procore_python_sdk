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
from procore_sdk.models.drawing_area1_drawing_disciplines_inner import DrawingArea1DrawingDisciplinesInner
from procore_sdk.models.drawing_set1 import DrawingSet1
from typing import Optional, Set
from typing_extensions import Self

class DrawingArea1(BaseModel):
    """
    Drawing Area
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Drawing Area ID")
    name: Optional[StrictStr] = Field(default=None, description="Drawing Area name")
    drawings_count: Optional[StrictInt] = Field(default=None, description="Amount of Drawings")
    description: Optional[StrictStr] = Field(default=None, description="Drawing Area Description")
    drawing_sets: Optional[List[DrawingSet1]] = Field(default=None, description="Array of Drawing Sets")
    drawing_disciplines: Optional[List[DrawingArea1DrawingDisciplinesInner]] = Field(default=None, description="Array of Drawing Disciplines")
    __properties: ClassVar[List[str]] = ["id", "name", "drawings_count", "description", "drawing_sets", "drawing_disciplines"]

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
        """Create an instance of DrawingArea1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in drawing_sets (list)
        _items = []
        if self.drawing_sets:
            for _item_drawing_sets in self.drawing_sets:
                if _item_drawing_sets:
                    _items.append(_item_drawing_sets.to_dict())
            _dict['drawing_sets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in drawing_disciplines (list)
        _items = []
        if self.drawing_disciplines:
            for _item_drawing_disciplines in self.drawing_disciplines:
                if _item_drawing_disciplines:
                    _items.append(_item_drawing_disciplines.to_dict())
            _dict['drawing_disciplines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DrawingArea1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "drawings_count": obj.get("drawings_count"),
            "description": obj.get("description"),
            "drawing_sets": [DrawingSet1.from_dict(_item) for _item in obj["drawing_sets"]] if obj.get("drawing_sets") is not None else None,
            "drawing_disciplines": [DrawingArea1DrawingDisciplinesInner.from_dict(_item) for _item in obj["drawing_disciplines"]] if obj.get("drawing_disciplines") is not None else None
        })
        return _obj


