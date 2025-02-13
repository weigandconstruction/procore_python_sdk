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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.nested_bim_view_folder_batch_create_response_errors_inner import NestedBIMViewFolderBatchCreateResponseErrorsInner
from procore_sdk.models.rest_v10_nested_bim_view_folders_post200_response import RestV10NestedBimViewFoldersPost200Response
from typing import Optional, Set
from typing_extensions import Self

class NestedBIMViewFolderBatchCreateResponse(BaseModel):
    """
    NestedBIMViewFolderBatchCreateResponse
    """ # noqa: E501
    bim_view_folders: Optional[List[RestV10NestedBimViewFoldersPost200Response]] = None
    errors: Optional[List[NestedBIMViewFolderBatchCreateResponseErrorsInner]] = None
    __properties: ClassVar[List[str]] = ["bim_view_folders", "errors"]

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
        """Create an instance of NestedBIMViewFolderBatchCreateResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NestedBIMViewFolderBatchCreateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bim_view_folders": [RestV10NestedBimViewFoldersPost200Response.from_dict(_item) for _item in obj["bim_view_folders"]] if obj.get("bim_view_folders") is not None else None,
            "errors": [NestedBIMViewFolderBatchCreateResponseErrorsInner.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None
        })
        return _obj


