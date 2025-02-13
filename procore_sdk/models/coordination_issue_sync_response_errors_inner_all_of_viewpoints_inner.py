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

class CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner(BaseModel):
    """
    CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner
    """ # noqa: E501
    snapshot_upload_uuid: StrictStr = Field(description="UUID of uploaded snapshot")
    snapshot: Optional[StrictStr] = Field(default=None, description="File to use as image data. Note that it's only possible to post a file using a multipart/form-data body (see RFC 2388). Most HTTP libraries will do the right thing when you pass in an open file or IO stream. Alternatively you can use snapshot_upload_uuid. You should not use both file and upload_uuid fields in the same request.")
    name: Optional[StrictStr] = Field(default=None, description="Viewpoint name")
    camera_data: StrictStr = Field(description="Camera data for the building model associated with the issue")
    redlines_data: Optional[StrictStr] = Field(default=None, description="Lines data for the building model associated with the issue")
    sections_data: Optional[StrictStr] = Field(default=None, description="Clipping plane data for the building model associated with the issue")
    __properties: ClassVar[List[str]] = ["snapshot_upload_uuid", "snapshot", "name", "camera_data", "redlines_data", "sections_data"]

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
        """Create an instance of CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner from a JSON string"""
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
        """Create an instance of CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "snapshot_upload_uuid": obj.get("snapshot_upload_uuid"),
            "snapshot": obj.get("snapshot"),
            "name": obj.get("name"),
            "camera_data": obj.get("camera_data"),
            "redlines_data": obj.get("redlines_data"),
            "sections_data": obj.get("sections_data")
        })
        return _obj


