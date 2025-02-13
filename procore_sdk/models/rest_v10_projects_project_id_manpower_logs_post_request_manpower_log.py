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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.work_order_contract_custom_field_custom_field_definition_id import WorkOrderContractCustomFieldCustomFieldDefinitionId
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdManpowerLogsPostRequestManpowerLog(BaseModel):
    """
    RestV10ProjectsProjectIdManpowerLogsPostRequestManpowerLog
    """ # noqa: E501
    var_date: Optional[date] = Field(default=None, description="Date of record. Mutually exclusive with the datetime property.", alias="date")
    datetime: Optional[datetime] = Field(default=None, description="Datetime of record. Mutually exclusive with the date property.")
    notes: Optional[StrictStr] = Field(default=None, description="Notes")
    num_workers: Optional[StrictInt] = Field(default=None, description="Number of workers")
    num_hours: Optional[StrictStr] = Field(default=None, description="Number of hours for each worker")
    contact_id: Optional[StrictInt] = Field(default=None, description="ID of the Vendor that is performing work")
    user_id: Optional[StrictInt] = Field(default=None, description="ID of the user that is performing work. Use this instead of contact_id when tracking hours for a specific user.")
    cost_code_id: Optional[StrictInt] = Field(default=None, description="Cost Code ID")
    location_id: Optional[StrictInt] = Field(default=None, description="The ID of the Location of the Manpower Log. `location_id` takes precedence over `mt_location`")
    trade_id: Optional[StrictInt] = Field(default=None, description="ID of the Trade associated to the Manpower Log")
    mt_location: Optional[List[StrictStr]] = Field(default=None, description="Use this for creating a new multi-tier or single-tier Location. This will be ignored if `location_id` is provided.")
    custom_field_custom_field_definition_id: Optional[WorkOrderContractCustomFieldCustomFieldDefinitionId] = Field(default=None, alias="custom_field_%{custom_field_definition_id}")
    __properties: ClassVar[List[str]] = ["date", "datetime", "notes", "num_workers", "num_hours", "contact_id", "user_id", "cost_code_id", "location_id", "trade_id", "mt_location", "custom_field_%{custom_field_definition_id}"]

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
        """Create an instance of RestV10ProjectsProjectIdManpowerLogsPostRequestManpowerLog from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_field_custom_field_definition_id
        if self.custom_field_custom_field_definition_id:
            _dict['custom_field_%{custom_field_definition_id}'] = self.custom_field_custom_field_definition_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdManpowerLogsPostRequestManpowerLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "datetime": obj.get("datetime"),
            "notes": obj.get("notes"),
            "num_workers": obj.get("num_workers"),
            "num_hours": obj.get("num_hours"),
            "contact_id": obj.get("contact_id"),
            "user_id": obj.get("user_id"),
            "cost_code_id": obj.get("cost_code_id"),
            "location_id": obj.get("location_id"),
            "trade_id": obj.get("trade_id"),
            "mt_location": obj.get("mt_location"),
            "custom_field_%{custom_field_definition_id}": WorkOrderContractCustomFieldCustomFieldDefinitionId.from_dict(obj["custom_field_%{custom_field_definition_id}"]) if obj.get("custom_field_%{custom_field_definition_id}") is not None else None
        })
        return _obj


