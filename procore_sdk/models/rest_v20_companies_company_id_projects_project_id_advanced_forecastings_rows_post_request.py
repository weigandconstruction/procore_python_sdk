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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post_request_forecasting_rows_inner import RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequestForecastingRowsInner
from typing import Optional, Set
from typing_extensions import Self

class RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequest(BaseModel):
    """
    RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequest
    """ # noqa: E501
    forecasting_rows: Optional[List[RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequestForecastingRowsInner]] = None
    __properties: ClassVar[List[str]] = ["forecasting_rows"]

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
        """Create an instance of RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in forecasting_rows (list)
        _items = []
        if self.forecasting_rows:
            for _item_forecasting_rows in self.forecasting_rows:
                if _item_forecasting_rows:
                    _items.append(_item_forecasting_rows.to_dict())
            _dict['forecasting_rows'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "forecasting_rows": [RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequestForecastingRowsInner.from_dict(_item) for _item in obj["forecasting_rows"]] if obj.get("forecasting_rows") is not None else None
        })
        return _obj


