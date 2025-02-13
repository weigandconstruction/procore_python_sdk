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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.links import Links
from procore_sdk.models.location7 import Location7
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from procore_sdk.models.trade2 import Trade2
from typing import Optional, Set
from typing_extensions import Self

class Image(BaseModel):
    """
    Image
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Image ID")
    url: Optional[StrictStr] = Field(default=None, description="Image url")
    size: Optional[StrictInt] = Field(default=None, description="Image size")
    filename: Optional[StrictStr] = Field(default=None, description="Image file name")
    description: Optional[StrictStr] = Field(default=None, description="Image description")
    thumbnail_url: Optional[StrictStr] = Field(default=None, description="Image thumbnail url")
    taken_at: Optional[datetime] = Field(default=None, description="Image taken at")
    created_at: Optional[datetime] = Field(default=None, description="Image created at")
    updated_at: Optional[datetime] = Field(default=None, description="Image updated at")
    location: Optional[Location7] = None
    image_category_name: Optional[StrictStr] = Field(default=None, description="Image Category Name")
    image_category_id: Optional[StrictInt] = Field(default=None, description="Image Category ID")
    permanently_deleted: Optional[StrictBool] = Field(default=None, description="Image permanent deletion status")
    private: Optional[StrictBool] = Field(default=None, description="Image private status")
    starred: Optional[StrictBool] = Field(default=None, description="Image starred status")
    width: Optional[StrictInt] = Field(default=None, description="Image width")
    height: Optional[StrictInt] = Field(default=None, description="Image height")
    image_category_private: Optional[StrictBool] = None
    origin_id: Optional[StrictInt] = None
    daily_log_header_id: Optional[StrictInt] = None
    gps_lat: Optional[StrictStr] = None
    gps_long: Optional[StrictStr] = None
    uploader: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    links: Optional[Links] = None
    trades: Optional[List[Trade2]] = None
    comments_count: Optional[StrictInt] = Field(default=None, description="the number of comments on this image")
    __properties: ClassVar[List[str]] = ["id", "url", "size", "filename", "description", "thumbnail_url", "taken_at", "created_at", "updated_at", "location", "image_category_name", "image_category_id", "permanently_deleted", "private", "starred", "width", "height", "image_category_private", "origin_id", "daily_log_header_id", "gps_lat", "gps_long", "uploader", "links", "trades", "comments_count"]

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
        """Create an instance of Image from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uploader
        if self.uploader:
            _dict['uploader'] = self.uploader.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in trades (list)
        _items = []
        if self.trades:
            for _item_trades in self.trades:
                if _item_trades:
                    _items.append(_item_trades.to_dict())
            _dict['trades'] = _items
        # set to None if thumbnail_url (nullable) is None
        # and model_fields_set contains the field
        if self.thumbnail_url is None and "thumbnail_url" in self.model_fields_set:
            _dict['thumbnail_url'] = None

        # set to None if taken_at (nullable) is None
        # and model_fields_set contains the field
        if self.taken_at is None and "taken_at" in self.model_fields_set:
            _dict['taken_at'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if width (nullable) is None
        # and model_fields_set contains the field
        if self.width is None and "width" in self.model_fields_set:
            _dict['width'] = None

        # set to None if height (nullable) is None
        # and model_fields_set contains the field
        if self.height is None and "height" in self.model_fields_set:
            _dict['height'] = None

        # set to None if origin_id (nullable) is None
        # and model_fields_set contains the field
        if self.origin_id is None and "origin_id" in self.model_fields_set:
            _dict['origin_id'] = None

        # set to None if daily_log_header_id (nullable) is None
        # and model_fields_set contains the field
        if self.daily_log_header_id is None and "daily_log_header_id" in self.model_fields_set:
            _dict['daily_log_header_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Image from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "url": obj.get("url"),
            "size": obj.get("size"),
            "filename": obj.get("filename"),
            "description": obj.get("description"),
            "thumbnail_url": obj.get("thumbnail_url"),
            "taken_at": obj.get("taken_at"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "location": Location7.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "image_category_name": obj.get("image_category_name"),
            "image_category_id": obj.get("image_category_id"),
            "permanently_deleted": obj.get("permanently_deleted"),
            "private": obj.get("private"),
            "starred": obj.get("starred"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "image_category_private": obj.get("image_category_private"),
            "origin_id": obj.get("origin_id"),
            "daily_log_header_id": obj.get("daily_log_header_id"),
            "gps_lat": obj.get("gps_lat"),
            "gps_long": obj.get("gps_long"),
            "uploader": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["uploader"]) if obj.get("uploader") is not None else None,
            "links": Links.from_dict(obj["links"]) if obj.get("links") is not None else None,
            "trades": [Trade2.from_dict(_item) for _item in obj["trades"]] if obj.get("trades") is not None else None,
            "comments_count": obj.get("comments_count")
        })
        return _obj


