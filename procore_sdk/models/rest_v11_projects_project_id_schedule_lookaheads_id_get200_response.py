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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_generation_errors_inner import RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInner
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner import RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner
from typing import Optional, Set
from typing_extensions import Self

class RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response(BaseModel):
    """
    Schedule Lookahead
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Lookahead ID")
    start_date: Optional[date] = Field(default=None, description="Lookahead start date, in project time zone")
    end_date: Optional[date] = Field(default=None, description="Lookahead end date, in project time zone")
    created_at: Optional[datetime] = Field(default=None, description="Lookahead creation time")
    data_date: Optional[datetime] = Field(default=None, description="Lookahead last update time")
    created_by: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    label: Optional[StrictStr] = Field(default=None, description="Lookahead label")
    lookahead_tasks: Optional[List[RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner]] = Field(default=None, description="List of tasks in the Lookahead, given in a nested tree structure according to parent-child relationships")
    generation_errors: Optional[List[RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInner]] = Field(default=None, description="List of errors that appeared during Lookahead generation.")
    status: Optional[StrictStr] = Field(default=None, description="Lookahead processing status.")
    weeks: Optional[StrictInt] = Field(default=None, description="Number of weeks the Lookahead spans in duration")
    __properties: ClassVar[List[str]] = ["id", "start_date", "end_date", "created_at", "data_date", "created_by", "label", "lookahead_tasks", "generation_errors", "status", "weeks"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['queued', 'processing_previous_lookahead', 'processing_master_schedule', 'ready']):
            raise ValueError("must be one of enum values ('queued', 'processing_previous_lookahead', 'processing_master_schedule', 'ready')")
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
        """Create an instance of RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in lookahead_tasks (list)
        _items = []
        if self.lookahead_tasks:
            for _item_lookahead_tasks in self.lookahead_tasks:
                if _item_lookahead_tasks:
                    _items.append(_item_lookahead_tasks.to_dict())
            _dict['lookahead_tasks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in generation_errors (list)
        _items = []
        if self.generation_errors:
            for _item_generation_errors in self.generation_errors:
                if _item_generation_errors:
                    _items.append(_item_generation_errors.to_dict())
            _dict['generation_errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date"),
            "created_at": obj.get("created_at"),
            "data_date": obj.get("data_date"),
            "created_by": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "label": obj.get("label"),
            "lookahead_tasks": [RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner.from_dict(_item) for _item in obj["lookahead_tasks"]] if obj.get("lookahead_tasks") is not None else None,
            "generation_errors": [RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInner.from_dict(_item) for _item in obj["generation_errors"]] if obj.get("generation_errors") is not None else None,
            "status": obj.get("status"),
            "weeks": obj.get("weeks")
        })
        return _obj


