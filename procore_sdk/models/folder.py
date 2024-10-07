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
from procore_sdk.models.folder_files_inner import FolderFilesInner
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_custom_fields import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields
from typing import Optional, Set
from typing_extensions import Self

class Folder(BaseModel):
    """
    Folder
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Folder id")
    name: Optional[StrictStr] = Field(default=None, description="Folder name")
    parent_id: Optional[StrictInt] = Field(default=None, description="Folder parent id")
    private: Optional[StrictBool] = Field(default=None, description="Folder private status")
    updated_at: Optional[datetime] = Field(default=None, description="Folder updated at")
    is_tracked: Optional[StrictBool] = Field(default=None, description="Folder is tracked status")
    tracked_folder: Optional[Dict[str, Any]] = Field(default=None, description="Folder watchers")
    name_with_path: Optional[StrictStr] = Field(default=None, description="Full file path with Folder name")
    folders: Optional[List[Folder]] = Field(default=None, description="Folder subfolders")
    files: Optional[List[FolderFilesInner]] = Field(default=None, description="Folder files")
    read_only: Optional[StrictBool] = Field(default=None, description="Folder read only status")
    is_deleted: Optional[StrictBool] = Field(default=None, description="File is in the recycle bin status")
    is_recycle_bin: Optional[StrictBool] = Field(default=None, description="Folder is recycle bin status")
    has_children: Optional[StrictBool] = Field(default=None, description="Folder has children status")
    has_children_files: Optional[StrictBool] = Field(default=None, description="Folder has at least one child that is a file status")
    has_children_folders: Optional[StrictBool] = Field(default=None, description="Folder has at least one child that is a folder status")
    custom_fields: Optional[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields] = None
    __properties: ClassVar[List[str]] = ["id", "name", "parent_id", "private", "updated_at", "is_tracked", "tracked_folder", "name_with_path", "folders", "files", "read_only", "is_deleted", "is_recycle_bin", "has_children", "has_children_files", "has_children_folders", "custom_fields"]

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
        """Create an instance of Folder from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in folders (list)
        _items = []
        if self.folders:
            for _item_folders in self.folders:
                if _item_folders:
                    _items.append(_item_folders.to_dict())
            _dict['folders'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item_files in self.files:
                if _item_files:
                    _items.append(_item_files.to_dict())
            _dict['files'] = _items
        # override the default output from pydantic by calling `to_dict()` of custom_fields
        if self.custom_fields:
            _dict['custom_fields'] = self.custom_fields.to_dict()
        # set to None if parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_id is None and "parent_id" in self.model_fields_set:
            _dict['parent_id'] = None

        # set to None if tracked_folder (nullable) is None
        # and model_fields_set contains the field
        if self.tracked_folder is None and "tracked_folder" in self.model_fields_set:
            _dict['tracked_folder'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Folder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "parent_id": obj.get("parent_id"),
            "private": obj.get("private"),
            "updated_at": obj.get("updated_at"),
            "is_tracked": obj.get("is_tracked"),
            "tracked_folder": obj.get("tracked_folder"),
            "name_with_path": obj.get("name_with_path"),
            "folders": [Folder.from_dict(_item) for _item in obj["folders"]] if obj.get("folders") is not None else None,
            "files": [FolderFilesInner.from_dict(_item) for _item in obj["files"]] if obj.get("files") is not None else None,
            "read_only": obj.get("read_only"),
            "is_deleted": obj.get("is_deleted"),
            "is_recycle_bin": obj.get("is_recycle_bin"),
            "has_children": obj.get("has_children"),
            "has_children_files": obj.get("has_children_files"),
            "has_children_folders": obj.get("has_children_folders"),
            "custom_fields": RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.from_dict(obj["custom_fields"]) if obj.get("custom_fields") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
Folder.model_rebuild(raise_errors=False)

