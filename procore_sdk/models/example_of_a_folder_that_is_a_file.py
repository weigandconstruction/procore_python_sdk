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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.example_of_a_folder_that_is_a_file_children import ExampleOfAFolderThatIsAFileChildren
from procore_sdk.models.example_of_a_folder_that_is_a_file_file import ExampleOfAFolderThatIsAFileFile
from procore_sdk.models.folder2 import Folder2
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get200_response_inner_custom_fields import RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from typing import Optional, Set
from typing_extensions import Self

class ExampleOfAFolderThatIsAFile(BaseModel):
    """
    ExampleOfAFolderThatIsAFile
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Folder id")
    name: Optional[StrictStr] = Field(default=None, description="Folder name")
    name_with_path: Optional[StrictStr] = Field(default=None, description="Full file path with folder name")
    parent_id: Optional[StrictInt] = Field(default=None, description="Folder parent id")
    created_at: Optional[datetime] = Field(default=None, description="Folder created at")
    created_by: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    updated_at: Optional[datetime] = Field(default=None, description="Folder updated at")
    read_only: Optional[StrictBool] = Field(default=None, description="File is read_only (only updatable via Schedule)")
    is_deleted: Optional[StrictBool] = Field(default=None, description="Folder is in the recycle bin status")
    is_recycle_bin: Optional[StrictBool] = Field(default=None, description="Folder is recycle bin status")
    document_type: Optional[StrictStr] = Field(default=None, description="Folder or File")
    is_tracked: Optional[StrictBool] = Field(default=None, description="Status whether Folder is explicitly tracked")
    private: Optional[StrictBool] = Field(default=None, description="Status whether Folder is explicitly private")
    private_parent: Optional[Folder2] = None
    tracked_folder: Optional[Folder2] = None
    file: Optional[ExampleOfAFolderThatIsAFileFile] = None
    children: Optional[ExampleOfAFolderThatIsAFileChildren] = None
    custom_fields: Optional[RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields] = None
    __properties: ClassVar[List[str]] = ["id", "name", "name_with_path", "parent_id", "created_at", "created_by", "updated_at", "read_only", "is_deleted", "is_recycle_bin", "document_type", "is_tracked", "private", "private_parent", "tracked_folder", "file", "children", "custom_fields"]

    @field_validator('document_type')
    def document_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['file', 'folder']):
            raise ValueError("must be one of enum values ('file', 'folder')")
        return value

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
        """Create an instance of ExampleOfAFolderThatIsAFile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of private_parent
        if self.private_parent:
            _dict['private_parent'] = self.private_parent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tracked_folder
        if self.tracked_folder:
            _dict['tracked_folder'] = self.tracked_folder.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of children
        if self.children:
            _dict['children'] = self.children.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_fields
        if self.custom_fields:
            _dict['custom_fields'] = self.custom_fields.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExampleOfAFolderThatIsAFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "name_with_path": obj.get("name_with_path"),
            "parent_id": obj.get("parent_id"),
            "created_at": obj.get("created_at"),
            "created_by": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "updated_at": obj.get("updated_at"),
            "read_only": obj.get("read_only"),
            "is_deleted": obj.get("is_deleted"),
            "is_recycle_bin": obj.get("is_recycle_bin"),
            "document_type": obj.get("document_type"),
            "is_tracked": obj.get("is_tracked"),
            "private": obj.get("private"),
            "private_parent": Folder2.from_dict(obj["private_parent"]) if obj.get("private_parent") is not None else None,
            "tracked_folder": Folder2.from_dict(obj["tracked_folder"]) if obj.get("tracked_folder") is not None else None,
            "file": ExampleOfAFolderThatIsAFileFile.from_dict(obj["file"]) if obj.get("file") is not None else None,
            "children": ExampleOfAFolderThatIsAFileChildren.from_dict(obj["children"]) if obj.get("children") is not None else None,
            "custom_fields": RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.from_dict(obj["custom_fields"]) if obj.get("custom_fields") is not None else None
        })
        return _obj


