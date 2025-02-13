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
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks(BaseModel):
    """
    Links that can be used by Frontend
    """ # noqa: E501
    add_vendor: Optional[StrictStr] = None
    analytics_events_path: Optional[StrictStr] = Field(default=None, alias="analyticsEventsPath")
    attach_documents: Optional[StrictStr] = None
    bid_list: Optional[StrictStr] = None
    bid_packages: Optional[StrictStr] = None
    bid_packages_by_project: Optional[StrictStr] = None
    bulk_create_bids: Optional[StrictStr] = None
    cost_codes: Optional[StrictStr] = None
    overview: Optional[StrictStr] = None
    permission_templates: Optional[StrictStr] = None
    submit: Optional[StrictStr] = None
    trades: Optional[StrictStr] = None
    vendors: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["add_vendor", "analyticsEventsPath", "attach_documents", "bid_list", "bid_packages", "bid_packages_by_project", "bulk_create_bids", "cost_codes", "overview", "permission_templates", "submit", "trades", "vendors"]

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
        """Create an instance of RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "add_vendor": obj.get("add_vendor"),
            "analyticsEventsPath": obj.get("analyticsEventsPath"),
            "attach_documents": obj.get("attach_documents"),
            "bid_list": obj.get("bid_list"),
            "bid_packages": obj.get("bid_packages"),
            "bid_packages_by_project": obj.get("bid_packages_by_project"),
            "bulk_create_bids": obj.get("bulk_create_bids"),
            "cost_codes": obj.get("cost_codes"),
            "overview": obj.get("overview"),
            "permission_templates": obj.get("permission_templates"),
            "submit": obj.get("submit"),
            "trades": obj.get("trades"),
            "vendors": obj.get("vendors")
        })
        return _obj


