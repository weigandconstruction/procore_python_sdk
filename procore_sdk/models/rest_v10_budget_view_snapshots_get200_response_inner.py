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
from procore_sdk.models.rest_v10_budget_view_snapshots_get200_response_inner_budget_view import RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView
from procore_sdk.models.rest_v10_budget_view_snapshots_get200_response_inner_links import RestV10BudgetViewSnapshotsGet200ResponseInnerLinks
from procore_sdk.models.rest_v10_budget_views_get200_response_inner_created_by import RestV10BudgetViewsGet200ResponseInnerCreatedBy
from typing import Optional, Set
from typing_extensions import Self

class RestV10BudgetViewSnapshotsGet200ResponseInner(BaseModel):
    """
    Budget View Snapshot
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    name: Optional[StrictStr] = Field(default=None, description="Name")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    created_at: Optional[StrictStr] = Field(default=None, description="Created At timestamp")
    created_by: Optional[RestV10BudgetViewsGet200ResponseInnerCreatedBy] = None
    budget_view: Optional[RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView] = None
    links: Optional[RestV10BudgetViewSnapshotsGet200ResponseInnerLinks] = None
    __properties: ClassVar[List[str]] = ["id", "name", "description", "created_at", "created_by", "budget_view", "links"]

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
        """Create an instance of RestV10BudgetViewSnapshotsGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of budget_view
        if self.budget_view:
            _dict['budget_view'] = self.budget_view.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10BudgetViewSnapshotsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "created_at": obj.get("created_at"),
            "created_by": RestV10BudgetViewsGet200ResponseInnerCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "budget_view": RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView.from_dict(obj["budget_view"]) if obj.get("budget_view") is not None else None,
            "links": RestV10BudgetViewSnapshotsGet200ResponseInnerLinks.from_dict(obj["links"]) if obj.get("links") is not None else None
        })
        return _obj


