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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates_accident_log_inner import RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdates(BaseModel):
    """
    RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdates
    """ # noqa: E501
    accident_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    call_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    delay_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    delivery_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    dumpster_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    equipment_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    inspection_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    manpower_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    daily_construction_report_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    notes_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    plan_revision_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    productivity_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    quantity_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    safety_violation_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    timecard_entry: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    visitor_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    waste_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    work_log: Optional[List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]] = Field(default=None, description="Array of Update Data for Log Type")
    __properties: ClassVar[List[str]] = ["accident_log", "call_log", "delay_log", "delivery_log", "dumpster_log", "equipment_log", "inspection_log", "manpower_log", "daily_construction_report_log", "notes_log", "plan_revision_log", "productivity_log", "quantity_log", "safety_violation_log", "timecard_entry", "visitor_log", "waste_log", "work_log"]

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
        """Create an instance of RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdates from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in accident_log (list)
        _items = []
        if self.accident_log:
            for _item_accident_log in self.accident_log:
                if _item_accident_log:
                    _items.append(_item_accident_log.to_dict())
            _dict['accident_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in call_log (list)
        _items = []
        if self.call_log:
            for _item_call_log in self.call_log:
                if _item_call_log:
                    _items.append(_item_call_log.to_dict())
            _dict['call_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in delay_log (list)
        _items = []
        if self.delay_log:
            for _item_delay_log in self.delay_log:
                if _item_delay_log:
                    _items.append(_item_delay_log.to_dict())
            _dict['delay_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in delivery_log (list)
        _items = []
        if self.delivery_log:
            for _item_delivery_log in self.delivery_log:
                if _item_delivery_log:
                    _items.append(_item_delivery_log.to_dict())
            _dict['delivery_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dumpster_log (list)
        _items = []
        if self.dumpster_log:
            for _item_dumpster_log in self.dumpster_log:
                if _item_dumpster_log:
                    _items.append(_item_dumpster_log.to_dict())
            _dict['dumpster_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in equipment_log (list)
        _items = []
        if self.equipment_log:
            for _item_equipment_log in self.equipment_log:
                if _item_equipment_log:
                    _items.append(_item_equipment_log.to_dict())
            _dict['equipment_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in inspection_log (list)
        _items = []
        if self.inspection_log:
            for _item_inspection_log in self.inspection_log:
                if _item_inspection_log:
                    _items.append(_item_inspection_log.to_dict())
            _dict['inspection_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in manpower_log (list)
        _items = []
        if self.manpower_log:
            for _item_manpower_log in self.manpower_log:
                if _item_manpower_log:
                    _items.append(_item_manpower_log.to_dict())
            _dict['manpower_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in daily_construction_report_log (list)
        _items = []
        if self.daily_construction_report_log:
            for _item_daily_construction_report_log in self.daily_construction_report_log:
                if _item_daily_construction_report_log:
                    _items.append(_item_daily_construction_report_log.to_dict())
            _dict['daily_construction_report_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notes_log (list)
        _items = []
        if self.notes_log:
            for _item_notes_log in self.notes_log:
                if _item_notes_log:
                    _items.append(_item_notes_log.to_dict())
            _dict['notes_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in plan_revision_log (list)
        _items = []
        if self.plan_revision_log:
            for _item_plan_revision_log in self.plan_revision_log:
                if _item_plan_revision_log:
                    _items.append(_item_plan_revision_log.to_dict())
            _dict['plan_revision_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in productivity_log (list)
        _items = []
        if self.productivity_log:
            for _item_productivity_log in self.productivity_log:
                if _item_productivity_log:
                    _items.append(_item_productivity_log.to_dict())
            _dict['productivity_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in quantity_log (list)
        _items = []
        if self.quantity_log:
            for _item_quantity_log in self.quantity_log:
                if _item_quantity_log:
                    _items.append(_item_quantity_log.to_dict())
            _dict['quantity_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in safety_violation_log (list)
        _items = []
        if self.safety_violation_log:
            for _item_safety_violation_log in self.safety_violation_log:
                if _item_safety_violation_log:
                    _items.append(_item_safety_violation_log.to_dict())
            _dict['safety_violation_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in timecard_entry (list)
        _items = []
        if self.timecard_entry:
            for _item_timecard_entry in self.timecard_entry:
                if _item_timecard_entry:
                    _items.append(_item_timecard_entry.to_dict())
            _dict['timecard_entry'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in visitor_log (list)
        _items = []
        if self.visitor_log:
            for _item_visitor_log in self.visitor_log:
                if _item_visitor_log:
                    _items.append(_item_visitor_log.to_dict())
            _dict['visitor_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in waste_log (list)
        _items = []
        if self.waste_log:
            for _item_waste_log in self.waste_log:
                if _item_waste_log:
                    _items.append(_item_waste_log.to_dict())
            _dict['waste_log'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in work_log (list)
        _items = []
        if self.work_log:
            for _item_work_log in self.work_log:
                if _item_work_log:
                    _items.append(_item_work_log.to_dict())
            _dict['work_log'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accident_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["accident_log"]] if obj.get("accident_log") is not None else None,
            "call_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["call_log"]] if obj.get("call_log") is not None else None,
            "delay_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["delay_log"]] if obj.get("delay_log") is not None else None,
            "delivery_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["delivery_log"]] if obj.get("delivery_log") is not None else None,
            "dumpster_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["dumpster_log"]] if obj.get("dumpster_log") is not None else None,
            "equipment_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["equipment_log"]] if obj.get("equipment_log") is not None else None,
            "inspection_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["inspection_log"]] if obj.get("inspection_log") is not None else None,
            "manpower_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["manpower_log"]] if obj.get("manpower_log") is not None else None,
            "daily_construction_report_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["daily_construction_report_log"]] if obj.get("daily_construction_report_log") is not None else None,
            "notes_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["notes_log"]] if obj.get("notes_log") is not None else None,
            "plan_revision_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["plan_revision_log"]] if obj.get("plan_revision_log") is not None else None,
            "productivity_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["productivity_log"]] if obj.get("productivity_log") is not None else None,
            "quantity_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["quantity_log"]] if obj.get("quantity_log") is not None else None,
            "safety_violation_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["safety_violation_log"]] if obj.get("safety_violation_log") is not None else None,
            "timecard_entry": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["timecard_entry"]] if obj.get("timecard_entry") is not None else None,
            "visitor_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["visitor_log"]] if obj.get("visitor_log") is not None else None,
            "waste_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["waste_log"]] if obj.get("waste_log") is not None else None,
            "work_log": [RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.from_dict(_item) for _item in obj["work_log"]] if obj.get("work_log") is not None else None
        })
        return _obj


