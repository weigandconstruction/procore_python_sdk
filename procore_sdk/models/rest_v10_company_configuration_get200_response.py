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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_company_configuration_get200_response_projects_timecard_default_lunch_time_inner import RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultLunchTimeInner
from procore_sdk.models.rest_v10_company_configuration_get200_response_projects_timecard_default_start_time_inner import RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner
from procore_sdk.models.rest_v10_company_configuration_get200_response_projects_timecard_default_stop_time_inner import RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner
from procore_sdk.models.rest_v10_company_configuration_get200_response_projects_timecard_lunch_time_tracking_inner import RestV10CompanyConfigurationGet200ResponseProjectsTimecardLunchTimeTrackingInner
from procore_sdk.models.rest_v10_company_configuration_get200_response_rounding_configuration import RestV10CompanyConfigurationGet200ResponseRoundingConfiguration
from procore_sdk.models.rest_v10_company_configuration_get200_response_time_and_materials_company_config import RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig
from typing import Optional, Set
from typing_extensions import Self

class RestV10CompanyConfigurationGet200Response(BaseModel):
    """
    RestV10CompanyConfigurationGet200Response
    """ # noqa: E501
    strict_file_uploading: Optional[StrictBool] = Field(default=None, description="Strict File Uploading Allowed")
    enable_image_real_time_as_builts: Optional[StrictBool] = Field(default=None, description="Image Real Time As Builts Enabled")
    currency_symbol: Optional[StrictStr] = Field(default=None, description="Currency Symbol")
    currency_display: Optional[StrictStr] = Field(default=None, description="Currency Display")
    currency_iso_code: Optional[StrictStr] = Field(default=None, description="Currency ISO Code")
    timecard_employees_see_all_projects: Optional[StrictBool] = Field(default=None, description="Timecard Employees Can See All Projects")
    timesheet_enabled_cost_type: Optional[List[StrictInt]] = Field(default=None, description="Timesheet IDs With Enabled Cost Type")
    timesheet_type: Optional[List[StrictInt]] = Field(default=None, description="Timesheet IDs With Enabled Cost Type")
    enable_sd_storage: Optional[StrictBool] = Field(default=None, description="SD Storage Enabled")
    timesheets_custom_signature_text: Optional[StrictStr] = Field(default=None, description="Timesheets Custom Signature Text")
    timesheets_week_start_day: Optional[StrictInt] = Field(default=None, description="Timesheets Week Starting Day")
    use_24_hour_mode: Optional[StrictBool] = Field(default=None, description="Use 24 Hour Clock")
    timesheets_tab_enabled: Optional[StrictBool] = Field(default=None, description="Timesheets Tab Enabled")
    timecard_should_track_location: Optional[List[StrictInt]] = Field(default=None, description="Projects whose configuration has track_timecard_location equals to true")
    projects_timecard_in_out_enabled: Optional[List[StrictInt]] = Field(default=None, description="Projects Timecard In Out Enabled")
    rounding_configuration: Optional[RestV10CompanyConfigurationGet200ResponseRoundingConfiguration] = None
    time_and_materials_company_config: Optional[RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig] = None
    projects_timecard_default_lunch_time: Optional[List[RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultLunchTimeInner]] = Field(default=None, description="Project Configurations whose timecard_default_lunch_time is not nil")
    projects_timecard_default_start_time: Optional[List[RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner]] = Field(default=None, description="Project Configurations whose timecard_default_start_time is not nil")
    projects_timecard_default_stop_time: Optional[List[RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner]] = Field(default=None, description="Project Configurations whose timecard_default_stop_time is not nil")
    projects_timecard_lunch_time_tracking: Optional[List[RestV10CompanyConfigurationGet200ResponseProjectsTimecardLunchTimeTrackingInner]] = Field(default=None, description="Project Configurations whose timecard_lunch_time_tracking is not nil")
    task_codes_enabled: Optional[StrictBool] = Field(default=None, description="Task codes enabled")
    timecard_employees_can_select_non_budgeted_items: Optional[List[StrictInt]] = Field(default=None, description="Timecard Employees can select non budgeted items")
    timecards_private: Optional[StrictBool] = Field(default=None, description="Timecards private by default")
    timesheet_default_cost_type_id: Optional[StrictInt] = Field(default=None, description="Company Timesheet Budget Configuration default line item type id for non-erp integrated projects")
    timesheet_erp_default_cost_type_id: Optional[StrictInt] = Field(default=None, description="Company Timesheet Budget Configuration default line item type id for erp integrated projects")
    __properties: ClassVar[List[str]] = ["strict_file_uploading", "enable_image_real_time_as_builts", "currency_symbol", "currency_display", "currency_iso_code", "timecard_employees_see_all_projects", "timesheet_enabled_cost_type", "timesheet_type", "enable_sd_storage", "timesheets_custom_signature_text", "timesheets_week_start_day", "use_24_hour_mode", "timesheets_tab_enabled", "timecard_should_track_location", "projects_timecard_in_out_enabled", "rounding_configuration", "time_and_materials_company_config", "projects_timecard_default_lunch_time", "projects_timecard_default_start_time", "projects_timecard_default_stop_time", "projects_timecard_lunch_time_tracking", "task_codes_enabled", "timecard_employees_can_select_non_budgeted_items", "timecards_private", "timesheet_default_cost_type_id", "timesheet_erp_default_cost_type_id"]

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
        """Create an instance of RestV10CompanyConfigurationGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rounding_configuration
        if self.rounding_configuration:
            _dict['rounding_configuration'] = self.rounding_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_and_materials_company_config
        if self.time_and_materials_company_config:
            _dict['time_and_materials_company_config'] = self.time_and_materials_company_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in projects_timecard_default_lunch_time (list)
        _items = []
        if self.projects_timecard_default_lunch_time:
            for _item_projects_timecard_default_lunch_time in self.projects_timecard_default_lunch_time:
                if _item_projects_timecard_default_lunch_time:
                    _items.append(_item_projects_timecard_default_lunch_time.to_dict())
            _dict['projects_timecard_default_lunch_time'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in projects_timecard_default_start_time (list)
        _items = []
        if self.projects_timecard_default_start_time:
            for _item_projects_timecard_default_start_time in self.projects_timecard_default_start_time:
                if _item_projects_timecard_default_start_time:
                    _items.append(_item_projects_timecard_default_start_time.to_dict())
            _dict['projects_timecard_default_start_time'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in projects_timecard_default_stop_time (list)
        _items = []
        if self.projects_timecard_default_stop_time:
            for _item_projects_timecard_default_stop_time in self.projects_timecard_default_stop_time:
                if _item_projects_timecard_default_stop_time:
                    _items.append(_item_projects_timecard_default_stop_time.to_dict())
            _dict['projects_timecard_default_stop_time'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in projects_timecard_lunch_time_tracking (list)
        _items = []
        if self.projects_timecard_lunch_time_tracking:
            for _item_projects_timecard_lunch_time_tracking in self.projects_timecard_lunch_time_tracking:
                if _item_projects_timecard_lunch_time_tracking:
                    _items.append(_item_projects_timecard_lunch_time_tracking.to_dict())
            _dict['projects_timecard_lunch_time_tracking'] = _items
        # set to None if rounding_configuration (nullable) is None
        # and model_fields_set contains the field
        if self.rounding_configuration is None and "rounding_configuration" in self.model_fields_set:
            _dict['rounding_configuration'] = None

        # set to None if time_and_materials_company_config (nullable) is None
        # and model_fields_set contains the field
        if self.time_and_materials_company_config is None and "time_and_materials_company_config" in self.model_fields_set:
            _dict['time_and_materials_company_config'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10CompanyConfigurationGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "strict_file_uploading": obj.get("strict_file_uploading"),
            "enable_image_real_time_as_builts": obj.get("enable_image_real_time_as_builts"),
            "currency_symbol": obj.get("currency_symbol"),
            "currency_display": obj.get("currency_display"),
            "currency_iso_code": obj.get("currency_iso_code"),
            "timecard_employees_see_all_projects": obj.get("timecard_employees_see_all_projects"),
            "timesheet_enabled_cost_type": obj.get("timesheet_enabled_cost_type"),
            "timesheet_type": obj.get("timesheet_type"),
            "enable_sd_storage": obj.get("enable_sd_storage"),
            "timesheets_custom_signature_text": obj.get("timesheets_custom_signature_text"),
            "timesheets_week_start_day": obj.get("timesheets_week_start_day"),
            "use_24_hour_mode": obj.get("use_24_hour_mode"),
            "timesheets_tab_enabled": obj.get("timesheets_tab_enabled"),
            "timecard_should_track_location": obj.get("timecard_should_track_location"),
            "projects_timecard_in_out_enabled": obj.get("projects_timecard_in_out_enabled"),
            "rounding_configuration": RestV10CompanyConfigurationGet200ResponseRoundingConfiguration.from_dict(obj["rounding_configuration"]) if obj.get("rounding_configuration") is not None else None,
            "time_and_materials_company_config": RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig.from_dict(obj["time_and_materials_company_config"]) if obj.get("time_and_materials_company_config") is not None else None,
            "projects_timecard_default_lunch_time": [RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultLunchTimeInner.from_dict(_item) for _item in obj["projects_timecard_default_lunch_time"]] if obj.get("projects_timecard_default_lunch_time") is not None else None,
            "projects_timecard_default_start_time": [RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner.from_dict(_item) for _item in obj["projects_timecard_default_start_time"]] if obj.get("projects_timecard_default_start_time") is not None else None,
            "projects_timecard_default_stop_time": [RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner.from_dict(_item) for _item in obj["projects_timecard_default_stop_time"]] if obj.get("projects_timecard_default_stop_time") is not None else None,
            "projects_timecard_lunch_time_tracking": [RestV10CompanyConfigurationGet200ResponseProjectsTimecardLunchTimeTrackingInner.from_dict(_item) for _item in obj["projects_timecard_lunch_time_tracking"]] if obj.get("projects_timecard_lunch_time_tracking") is not None else None,
            "task_codes_enabled": obj.get("task_codes_enabled"),
            "timecard_employees_can_select_non_budgeted_items": obj.get("timecard_employees_can_select_non_budgeted_items"),
            "timecards_private": obj.get("timecards_private"),
            "timesheet_default_cost_type_id": obj.get("timesheet_default_cost_type_id"),
            "timesheet_erp_default_cost_type_id": obj.get("timesheet_erp_default_cost_type_id")
        })
        return _obj


