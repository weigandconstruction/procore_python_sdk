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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ScheduleDates(BaseModel):
    """
    ScheduleDates
    """ # noqa: E501
    substantial_completion_date: Optional[date] = Field(default=None, description="Substantial completion date")
    finish_variance: Optional[StrictStr] = Field(default=None, description="Finish variance")
    percentage_complete: Optional[StrictInt] = Field(default=None, description="Percentage complete")
    __properties: ClassVar[List[str]] = ["substantial_completion_date", "finish_variance", "percentage_complete"]

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
        """Create an instance of ScheduleDates from a JSON string"""
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
        # set to None if substantial_completion_date (nullable) is None
        # and model_fields_set contains the field
        if self.substantial_completion_date is None and "substantial_completion_date" in self.model_fields_set:
            _dict['substantial_completion_date'] = None

        # set to None if finish_variance (nullable) is None
        # and model_fields_set contains the field
        if self.finish_variance is None and "finish_variance" in self.model_fields_set:
            _dict['finish_variance'] = None

        # set to None if percentage_complete (nullable) is None
        # and model_fields_set contains the field
        if self.percentage_complete is None and "percentage_complete" in self.model_fields_set:
            _dict['percentage_complete'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScheduleDates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "substantial_completion_date": obj.get("substantial_completion_date"),
            "finish_variance": obj.get("finish_variance"),
            "percentage_complete": obj.get("percentage_complete")
        })
        return _obj


