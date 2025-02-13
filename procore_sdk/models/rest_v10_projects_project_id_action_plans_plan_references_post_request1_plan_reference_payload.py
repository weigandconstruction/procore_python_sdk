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

from pydantic import BaseModel, ConfigDict, Field, StrictBytes, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest1PlanReferencePayload(BaseModel):
    """
    One of attachment, drawing_revision_id, file_version_id, specification_section_id, submittal_log_id, generic_tool_item_id, form_id, meeting_id, or observation_item_id is accepted depending on the type provided
    """ # noqa: E501
    drawing_revision_id: Optional[StrictInt] = Field(default=None, description="Drawing Revision ID")
    file_version_id: Optional[StrictInt] = Field(default=None, description="File Version ID")
    specification_section_id: Optional[StrictInt] = Field(default=None, description="Specification Section ID")
    submittal_log_id: Optional[StrictInt] = Field(default=None, description="Submittal Log ID")
    attachment: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="Reference Attachment. To upload an attachment you must upload the entire payload as `multipart/form-data` content-type with the `attachment` file.")
    generic_tool_item_id: Optional[StrictInt] = Field(default=None, description="Generic Tool Item (Correspondence) ID")
    form_id: Optional[StrictInt] = Field(default=None, description="Form ID")
    meeting_id: Optional[StrictInt] = Field(default=None, description="Meeting ID")
    observation_item_id: Optional[StrictInt] = Field(default=None, description="Observation Item ID")
    __properties: ClassVar[List[str]] = ["drawing_revision_id", "file_version_id", "specification_section_id", "submittal_log_id", "attachment", "generic_tool_item_id", "form_id", "meeting_id", "observation_item_id"]

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
        """Create an instance of RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest1PlanReferencePayload from a JSON string"""
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
        """Create an instance of RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest1PlanReferencePayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "drawing_revision_id": obj.get("drawing_revision_id"),
            "file_version_id": obj.get("file_version_id"),
            "specification_section_id": obj.get("specification_section_id"),
            "submittal_log_id": obj.get("submittal_log_id"),
            "attachment": obj.get("attachment"),
            "generic_tool_item_id": obj.get("generic_tool_item_id"),
            "form_id": obj.get("form_id"),
            "meeting_id": obj.get("meeting_id"),
            "observation_item_id": obj.get("observation_item_id")
        })
        return _obj


