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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from procore_sdk.models.office import Office
from procore_sdk.models.project import Project
from procore_sdk.models.rest_v10_projects_project_id_schedule_get200_response_active_features import RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures
from procore_sdk.models.rest_v10_projects_project_id_schedule_get200_response_schedule_crud_beta_agreement import RestV10ProjectsProjectIdScheduleGet200ResponseScheduleCrudBetaAgreement
from procore_sdk.models.rest_v10_projects_project_id_schedule_get200_response_type import RestV10ProjectsProjectIdScheduleGet200ResponseType
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdScheduleGet200Response(BaseModel):
    """
    RestV10ProjectsProjectIdScheduleGet200Response
    """ # noqa: E501
    active_features: Optional[RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures] = None
    last_calendar_view: Optional[StrictStr] = None
    schedule_present: Optional[StrictBool] = None
    schedule_processing: Optional[StrictBool] = None
    schedule_crud_beta_agreement: Optional[RestV10ProjectsProjectIdScheduleGet200ResponseScheduleCrudBetaAgreement] = None
    schedule_tasks_last_updated_at: Optional[datetime] = Field(default=None, description="Timestamp of the most recent change to any task in the Schedule.")
    schedule_tasks_edited_manually: Optional[StrictBool] = None
    type: Optional[RestV10ProjectsProjectIdScheduleGet200ResponseType] = None
    data_date: Optional[datetime] = Field(default=None, description="The data datetime of the last imported schedule.")
    lookahead_data_date: Optional[datetime] = Field(default=None, description="The Lookahead's data datetime.")
    number_of_pending_requested_changes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of pending Requested Changes for the given user.")
    uploaded_at: Optional[datetime] = Field(default=None, description="The upload datetime of the last imported schedule.")
    office: Optional[Office] = None
    project: Optional[Project] = None
    __properties: ClassVar[List[str]] = ["active_features", "last_calendar_view", "schedule_present", "schedule_processing", "schedule_crud_beta_agreement", "schedule_tasks_last_updated_at", "schedule_tasks_edited_manually", "type", "data_date", "lookahead_data_date", "number_of_pending_requested_changes", "uploaded_at", "office", "project"]

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
        """Create an instance of RestV10ProjectsProjectIdScheduleGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of active_features
        if self.active_features:
            _dict['active_features'] = self.active_features.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule_crud_beta_agreement
        if self.schedule_crud_beta_agreement:
            _dict['schedule_crud_beta_agreement'] = self.schedule_crud_beta_agreement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of office
        if self.office:
            _dict['office'] = self.office.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # set to None if schedule_tasks_last_updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.schedule_tasks_last_updated_at is None and "schedule_tasks_last_updated_at" in self.model_fields_set:
            _dict['schedule_tasks_last_updated_at'] = None

        # set to None if data_date (nullable) is None
        # and model_fields_set contains the field
        if self.data_date is None and "data_date" in self.model_fields_set:
            _dict['data_date'] = None

        # set to None if lookahead_data_date (nullable) is None
        # and model_fields_set contains the field
        if self.lookahead_data_date is None and "lookahead_data_date" in self.model_fields_set:
            _dict['lookahead_data_date'] = None

        # set to None if uploaded_at (nullable) is None
        # and model_fields_set contains the field
        if self.uploaded_at is None and "uploaded_at" in self.model_fields_set:
            _dict['uploaded_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdScheduleGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active_features": RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures.from_dict(obj["active_features"]) if obj.get("active_features") is not None else None,
            "last_calendar_view": obj.get("last_calendar_view"),
            "schedule_present": obj.get("schedule_present"),
            "schedule_processing": obj.get("schedule_processing"),
            "schedule_crud_beta_agreement": RestV10ProjectsProjectIdScheduleGet200ResponseScheduleCrudBetaAgreement.from_dict(obj["schedule_crud_beta_agreement"]) if obj.get("schedule_crud_beta_agreement") is not None else None,
            "schedule_tasks_last_updated_at": obj.get("schedule_tasks_last_updated_at"),
            "schedule_tasks_edited_manually": obj.get("schedule_tasks_edited_manually"),
            "type": RestV10ProjectsProjectIdScheduleGet200ResponseType.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "data_date": obj.get("data_date"),
            "lookahead_data_date": obj.get("lookahead_data_date"),
            "number_of_pending_requested_changes": obj.get("number_of_pending_requested_changes"),
            "uploaded_at": obj.get("uploaded_at"),
            "office": Office.from_dict(obj["office"]) if obj.get("office") is not None else None,
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None
        })
        return _obj


