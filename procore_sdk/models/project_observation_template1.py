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
from procore_sdk.models.project_observation_type import ProjectObservationType
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from procore_sdk.models.trade import Trade
from typing import Optional, Set
from typing_extensions import Self

class ProjectObservationTemplate1(BaseModel):
    """
    ProjectObservationTemplate1
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Project Observation Template ID")
    active: Optional[StrictBool] = Field(default=None, description="Flag denoting if the Observation Template is available for use")
    assignee: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    updated_at: Optional[datetime] = Field(default=None, description="Date updated")
    company_observation_template_id: Optional[StrictInt] = Field(default=None, description="Company Observation Template that the Project Observation Template was created from")
    observation_title: Optional[StrictStr] = Field(default=None, description="Title to be used for Observations created from this template")
    observation_type: Optional[ProjectObservationType] = None
    trade: Optional[Trade] = None
    __properties: ClassVar[List[str]] = ["id", "active", "assignee", "updated_at", "company_observation_template_id", "observation_title", "observation_type", "trade"]

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
        """Create an instance of ProjectObservationTemplate1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of assignee
        if self.assignee:
            _dict['assignee'] = self.assignee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of observation_type
        if self.observation_type:
            _dict['observation_type'] = self.observation_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trade
        if self.trade:
            _dict['trade'] = self.trade.to_dict()
        # set to None if company_observation_template_id (nullable) is None
        # and model_fields_set contains the field
        if self.company_observation_template_id is None and "company_observation_template_id" in self.model_fields_set:
            _dict['company_observation_template_id'] = None

        # set to None if trade (nullable) is None
        # and model_fields_set contains the field
        if self.trade is None and "trade" in self.model_fields_set:
            _dict['trade'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectObservationTemplate1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "active": obj.get("active"),
            "assignee": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["assignee"]) if obj.get("assignee") is not None else None,
            "updated_at": obj.get("updated_at"),
            "company_observation_template_id": obj.get("company_observation_template_id"),
            "observation_title": obj.get("observation_title"),
            "observation_type": ProjectObservationType.from_dict(obj["observation_type"]) if obj.get("observation_type") is not None else None,
            "trade": Trade.from_dict(obj["trade"]) if obj.get("trade") is not None else None
        })
        return _obj


