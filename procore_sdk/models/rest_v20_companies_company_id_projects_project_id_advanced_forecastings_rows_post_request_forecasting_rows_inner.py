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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post_request_forecasting_rows_inner_periods_inner import RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequestForecastingRowsInnerPeriodsInner
from typing import Optional, Set
from typing_extensions import Self

class RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequestForecastingRowsInner(BaseModel):
    """
    RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequestForecastingRowsInner
    """ # noqa: E501
    budget_line_item_id: Optional[StrictStr] = Field(default=None, description="ID of the line item.")
    wbs_code_id: StrictStr = Field(description="ID of the WBS code")
    start_date: Optional[StrictStr] = Field(default=None, description="The start date of the line item")
    end_date: Optional[StrictStr] = Field(default=None, description="The end date of the line item")
    curve: Optional[StrictStr] = Field(default=None, description="The curve of the line item. For more information about the curve distribution visit https://support.procore.com/faq/how-do-procores-advanced-forecasting-curves-distribute-projected-cost-to-complete-amounts")
    forecast_to_complete: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The forecast to complete of the line item")
    periods: Optional[List[RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequestForecastingRowsInnerPeriodsInner]] = Field(default=None, description="The periods of the line item")
    __properties: ClassVar[List[str]] = ["budget_line_item_id", "wbs_code_id", "start_date", "end_date", "curve", "forecast_to_complete", "periods"]

    @field_validator('curve')
    def curve_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['bell', 'back_loaded', 'front_loaded', 'linear', 'manual']):
            raise ValueError("must be one of enum values ('bell', 'back_loaded', 'front_loaded', 'linear', 'manual')")
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
        """Create an instance of RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequestForecastingRowsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in periods (list)
        _items = []
        if self.periods:
            for _item_periods in self.periods:
                if _item_periods:
                    _items.append(_item_periods.to_dict())
            _dict['periods'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequestForecastingRowsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "budget_line_item_id": obj.get("budget_line_item_id"),
            "wbs_code_id": obj.get("wbs_code_id"),
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date"),
            "curve": obj.get("curve"),
            "forecast_to_complete": obj.get("forecast_to_complete"),
            "periods": [RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequestForecastingRowsInnerPeriodsInner.from_dict(_item) for _item in obj["periods"]] if obj.get("periods") is not None else None
        })
        return _obj


