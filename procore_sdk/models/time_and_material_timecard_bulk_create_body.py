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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from procore_sdk.models.time_and_material_timecard_properties import TimeAndMaterialTimecardProperties
from typing import Optional, Set
from typing_extensions import Self

class TimeAndMaterialTimecardBulkCreateBody(BaseModel):
    """
    TimeAndMaterialTimecardBulkCreateBody
    """ # noqa: E501
    time_and_material_timecards: List[TimeAndMaterialTimecardProperties] = Field(description="Array of Time and material timecard objects")
    __properties: ClassVar[List[str]] = ["time_and_material_timecards"]

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
        """Create an instance of TimeAndMaterialTimecardBulkCreateBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in time_and_material_timecards (list)
        _items = []
        if self.time_and_material_timecards:
            for _item_time_and_material_timecards in self.time_and_material_timecards:
                if _item_time_and_material_timecards:
                    _items.append(_item_time_and_material_timecards.to_dict())
            _dict['time_and_material_timecards'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimeAndMaterialTimecardBulkCreateBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "time_and_material_timecards": [TimeAndMaterialTimecardProperties.from_dict(_item) for _item in obj["time_and_material_timecards"]] if obj.get("time_and_material_timecards") is not None else None
        })
        return _obj


