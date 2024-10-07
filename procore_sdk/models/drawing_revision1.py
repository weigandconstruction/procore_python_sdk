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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.drawing_revision_custom_fields import DrawingRevisionCustomFields
from procore_sdk.models.drawing_revision_drawing_set import DrawingRevisionDrawingSet
from typing import Optional, Set
from typing_extensions import Self

class DrawingRevision1(BaseModel):
    """
    Drawing Revision
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Revision ID")
    drawing_date: Optional[date] = Field(default=None, description="Drawing date")
    received_date: Optional[date] = Field(default=None, description="Received date")
    revision_number: Optional[StrictStr] = Field(default=None, description="Revision number")
    floorplan: Optional[StrictBool] = Field(default=None, description="Revision floorplan status")
    current: Optional[StrictBool] = Field(default=None, description="Current Drawing Revision")
    drawing_id: Optional[StrictInt] = Field(default=None, description="Drawing ID")
    drawing_set: Optional[DrawingRevisionDrawingSet] = None
    ordered_revision_ids: Optional[List[StrictInt]] = Field(default=None, description="Ordered array of the complete list of reviewed and published Drawing Revision IDs that belong to the drawing")
    custom_fields: Optional[DrawingRevisionCustomFields] = None
    __properties: ClassVar[List[str]] = ["id", "drawing_date", "received_date", "revision_number", "floorplan", "current", "drawing_id", "drawing_set", "ordered_revision_ids", "custom_fields"]

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
        """Create an instance of DrawingRevision1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of drawing_set
        if self.drawing_set:
            _dict['drawing_set'] = self.drawing_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_fields
        if self.custom_fields:
            _dict['custom_fields'] = self.custom_fields.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DrawingRevision1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "drawing_date": obj.get("drawing_date"),
            "received_date": obj.get("received_date"),
            "revision_number": obj.get("revision_number"),
            "floorplan": obj.get("floorplan"),
            "current": obj.get("current"),
            "drawing_id": obj.get("drawing_id"),
            "drawing_set": DrawingRevisionDrawingSet.from_dict(obj["drawing_set"]) if obj.get("drawing_set") is not None else None,
            "ordered_revision_ids": obj.get("ordered_revision_ids"),
            "custom_fields": DrawingRevisionCustomFields.from_dict(obj["custom_fields"]) if obj.get("custom_fields") is not None else None
        })
        return _obj


