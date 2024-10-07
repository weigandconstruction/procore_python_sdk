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
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.incident_filing_type import IncidentFilingType
from procore_sdk.models.rest_v10_projects_project_id_incidents_alerts_get200_response_inner_injury import RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury
from procore_sdk.models.rest_v10_projects_project_id_rfis_default_distribution_get200_response_inner import RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner
from procore_sdk.models.severity_level import SeverityLevel
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInner(BaseModel):
    """
    RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Incident Alert ID")
    event_id: Optional[StrictInt] = Field(default=None, description="Incident Alert Event ID")
    emailed_at: Optional[datetime] = Field(default=None, description="Timestamp of email delivery")
    filing_type: Optional[IncidentFilingType] = None
    injury: Optional[RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury] = None
    pushed_at: Optional[datetime] = Field(default=None, description="Timestamp of when the push notification delivery")
    recipient: Optional[RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner] = None
    severity_level: Optional[SeverityLevel] = None
    triggered_at: Optional[datetime] = Field(default=None, description="Timestamp of when the alert was triggered")
    triggered_by: Optional[RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner] = None
    __properties: ClassVar[List[str]] = ["id", "event_id", "emailed_at", "filing_type", "injury", "pushed_at", "recipient", "severity_level", "triggered_at", "triggered_by"]

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
        """Create an instance of RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filing_type
        if self.filing_type:
            _dict['filing_type'] = self.filing_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of injury
        if self.injury:
            _dict['injury'] = self.injury.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['recipient'] = self.recipient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of severity_level
        if self.severity_level:
            _dict['severity_level'] = self.severity_level.to_dict()
        # override the default output from pydantic by calling `to_dict()` of triggered_by
        if self.triggered_by:
            _dict['triggered_by'] = self.triggered_by.to_dict()
        # set to None if injury (nullable) is None
        # and model_fields_set contains the field
        if self.injury is None and "injury" in self.model_fields_set:
            _dict['injury'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "event_id": obj.get("event_id"),
            "emailed_at": obj.get("emailed_at"),
            "filing_type": IncidentFilingType.from_dict(obj["filing_type"]) if obj.get("filing_type") is not None else None,
            "injury": RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury.from_dict(obj["injury"]) if obj.get("injury") is not None else None,
            "pushed_at": obj.get("pushed_at"),
            "recipient": RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner.from_dict(obj["recipient"]) if obj.get("recipient") is not None else None,
            "severity_level": SeverityLevel.from_dict(obj["severity_level"]) if obj.get("severity_level") is not None else None,
            "triggered_at": obj.get("triggered_at"),
            "triggered_by": RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner.from_dict(obj["triggered_by"]) if obj.get("triggered_by") is not None else None
        })
        return _obj


