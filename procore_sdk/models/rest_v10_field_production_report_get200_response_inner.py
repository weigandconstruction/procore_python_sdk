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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class RestV10FieldProductionReportGet200ResponseInner(BaseModel):
    """
    Field Production Report
    """ # noqa: E501
    cost_code_id: Optional[StrictInt] = Field(default=None, description="ID of associated cost code")
    cost_code: Optional[StrictStr] = Field(default=None, description="Code and description of associated cost code")
    budgeted_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Number of labor hours budgeted for the given cost code")
    actual_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Number of labor hours logged for the given cost code to date")
    remaining_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Budgeted Hours - Actual Hours")
    hours_utilization: Optional[StrictStr] = Field(default=None, description="(Actual Hours / Budgeted Hours) * 100")
    projected_hours_at_completion: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="(Actual Hours / Actual Quantities) * Remaining Quantities")
    earned_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="(Budgeted Hours * Actual Quantities) / Budgeted Quantities")
    budgeted_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Budgeted amount of a unit to install for the given cost code")
    actual_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Actual amount of a unit installed for the given cost code to date")
    remaining_quantities: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Budgeted Quantity - Actual Quantity")
    unit_of_measure: Optional[StrictStr] = Field(default=None, description="One of the following (ea, ls, lf, sf, sy, cy, mm, m, m^2, m^3, lbs, t, kg, ton)")
    percent_complete: Optional[StrictStr] = Field(default=None, description="(Actual Quantity / Budgeted Quantity) * 100")
    budgeted_production_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Budgeted Quantity / Budgeted Hours")
    actual_production_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Actual Quantity / Actual Hours")
    production_rate_variance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Actual Production Rate - Budgeted Production Rate")
    is_budgeted: Optional[StrictStr] = Field(default=None, description="Cost code budgeted (yes/no)")
    sub_job_name: Optional[StrictStr] = Field(default=None, description="Name of the associated sub job")
    sub_job_id: Optional[StrictInt] = Field(default=None, description="ID of the associated sub job")
    __properties: ClassVar[List[str]] = ["cost_code_id", "cost_code", "budgeted_hours", "actual_hours", "remaining_hours", "hours_utilization", "projected_hours_at_completion", "earned_hours", "budgeted_quantity", "actual_quantity", "remaining_quantities", "unit_of_measure", "percent_complete", "budgeted_production_rate", "actual_production_rate", "production_rate_variance", "is_budgeted", "sub_job_name", "sub_job_id"]

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
        """Create an instance of RestV10FieldProductionReportGet200ResponseInner from a JSON string"""
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
        """Create an instance of RestV10FieldProductionReportGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cost_code_id": obj.get("cost_code_id"),
            "cost_code": obj.get("cost_code"),
            "budgeted_hours": obj.get("budgeted_hours"),
            "actual_hours": obj.get("actual_hours"),
            "remaining_hours": obj.get("remaining_hours"),
            "hours_utilization": obj.get("hours_utilization"),
            "projected_hours_at_completion": obj.get("projected_hours_at_completion"),
            "earned_hours": obj.get("earned_hours"),
            "budgeted_quantity": obj.get("budgeted_quantity"),
            "actual_quantity": obj.get("actual_quantity"),
            "remaining_quantities": obj.get("remaining_quantities"),
            "unit_of_measure": obj.get("unit_of_measure"),
            "percent_complete": obj.get("percent_complete"),
            "budgeted_production_rate": obj.get("budgeted_production_rate"),
            "actual_production_rate": obj.get("actual_production_rate"),
            "production_rate_variance": obj.get("production_rate_variance"),
            "is_budgeted": obj.get("is_budgeted"),
            "sub_job_name": obj.get("sub_job_name"),
            "sub_job_id": obj.get("sub_job_id")
        })
        return _obj


