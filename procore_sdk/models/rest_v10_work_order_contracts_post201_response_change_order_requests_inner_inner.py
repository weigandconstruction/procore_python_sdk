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
from procore_sdk.models.rest_v10_work_order_contracts_get200_response_inner_currency_configuration import RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration
from typing import Optional, Set
from typing_extensions import Self

class RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner(BaseModel):
    """
    RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    deleted_at: Optional[datetime] = Field(default=None, description="Deleted at")
    due_date: Optional[date] = Field(default=None, description="Due date")
    invoiced_date: Optional[date] = Field(default=None, description="Invoiced date")
    number: Optional[StrictStr] = Field(default=None, description="Number")
    paid_date: Optional[date] = Field(default=None, description="Paid date")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    currency_configuration: Optional[RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "deleted_at", "due_date", "invoiced_date", "number", "paid_date", "status", "title", "updated_at", "currency_configuration"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['draft', 'not_pricing', 'pricing', 'pending', 'revised', 'proceeding', 'not_proceeding', 'no_charge', 'approved', 'rejected', 'void']):
            raise ValueError("must be one of enum values ('draft', 'not_pricing', 'pricing', 'pending', 'revised', 'proceeding', 'not_proceeding', 'no_charge', 'approved', 'rejected', 'void')")
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
        """Create an instance of RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of currency_configuration
        if self.currency_configuration:
            _dict['currency_configuration'] = self.currency_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "deleted_at": obj.get("deleted_at"),
            "due_date": obj.get("due_date"),
            "invoiced_date": obj.get("invoiced_date"),
            "number": obj.get("number"),
            "paid_date": obj.get("paid_date"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "updated_at": obj.get("updated_at"),
            "currency_configuration": RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.from_dict(obj["currency_configuration"]) if obj.get("currency_configuration") is not None else None
        })
        return _obj


