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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdSafetyViolationLogsPostRequestSafetyViolationLog(BaseModel):
    """
    RestV10ProjectsProjectIdSafetyViolationLogsPostRequestSafetyViolationLog
    """ # noqa: E501
    comments: Optional[StrictStr] = Field(default=None, description="Comments")
    compliance_due: Optional[date] = Field(default=None, description="The date the compliance for the safety violation is due by")
    issued_to: Optional[StrictStr] = Field(default=None, description="Person who the safety violation was issued to")
    safety_notice: Optional[StrictStr] = Field(default=None, description="Name/number of the safety notice issued")
    subject: Optional[StrictStr] = Field(default=None, description="Reason for the safety violation")
    time_hour: Annotated[int, Field(le=23, strict=True, ge=0)] = Field(description="Time of safety violation - hour")
    time_minute: Annotated[int, Field(le=59, strict=True, ge=0)] = Field(description="Time of safety violation - minute")
    var_date: Optional[date] = Field(default=None, description="Format: YYYY-MM-DD Example: 2016-04-19", alias="date")
    datetime: Optional[datetime] = Field(default=None, description="Datetime of record. Mutually exclusive with the date property.")
    __properties: ClassVar[List[str]] = ["comments", "compliance_due", "issued_to", "safety_notice", "subject", "time_hour", "time_minute", "date", "datetime"]

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
        """Create an instance of RestV10ProjectsProjectIdSafetyViolationLogsPostRequestSafetyViolationLog from a JSON string"""
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
        """Create an instance of RestV10ProjectsProjectIdSafetyViolationLogsPostRequestSafetyViolationLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comments": obj.get("comments"),
            "compliance_due": obj.get("compliance_due"),
            "issued_to": obj.get("issued_to"),
            "safety_notice": obj.get("safety_notice"),
            "subject": obj.get("subject"),
            "time_hour": obj.get("time_hour"),
            "time_minute": obj.get("time_minute"),
            "date": obj.get("date"),
            "datetime": obj.get("datetime")
        })
        return _obj


