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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_projects_project_id_schedule_imports_processing_status_get200_response_import_file import RestV10ProjectsProjectIdScheduleImportsProcessingStatusGet200ResponseImportFile
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdScheduleImportsProcessingStatusGet200Response(BaseModel):
    """
    Schedule Import Processing State
    """ # noqa: E501
    schedule_processing_status: Optional[StrictStr] = Field(default=None, description="The status of a Schedule Import")
    import_file: Optional[RestV10ProjectsProjectIdScheduleImportsProcessingStatusGet200ResponseImportFile] = None
    schedule_uploaded: Optional[StrictBool] = Field(default=None, description="The upload status of the Schedule Import")
    __properties: ClassVar[List[str]] = ["schedule_processing_status", "import_file", "schedule_uploaded"]

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
        """Create an instance of RestV10ProjectsProjectIdScheduleImportsProcessingStatusGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of import_file
        if self.import_file:
            _dict['import_file'] = self.import_file.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdScheduleImportsProcessingStatusGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schedule_processing_status": obj.get("schedule_processing_status"),
            "import_file": RestV10ProjectsProjectIdScheduleImportsProcessingStatusGet200ResponseImportFile.from_dict(obj["import_file"]) if obj.get("import_file") is not None else None,
            "schedule_uploaded": obj.get("schedule_uploaded")
        })
        return _obj


