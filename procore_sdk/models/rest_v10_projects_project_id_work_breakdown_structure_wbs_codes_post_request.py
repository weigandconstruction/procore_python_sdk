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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request_segment_items_inner import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequestSegmentItemsInner
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest(BaseModel):
    """
    RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description of the wbs code.")
    segment_items: List[RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequestSegmentItemsInner]
    __properties: ClassVar[List[str]] = ["description", "segment_items"]

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
        """Create an instance of RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in segment_items (list)
        _items = []
        if self.segment_items:
            for _item_segment_items in self.segment_items:
                if _item_segment_items:
                    _items.append(_item_segment_items.to_dict())
            _dict['segment_items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "segment_items": [RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequestSegmentItemsInner.from_dict(_item) for _item in obj["segment_items"]] if obj.get("segment_items") is not None else None
        })
        return _obj


