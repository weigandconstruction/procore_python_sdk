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
from procore_sdk.models.rest_v10_payment_applications_get200_response_inner_all_of_currency_configuration import RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration
from procore_sdk.models.rest_v11_projects_project_id_direct_costs_get200_response_inner_employee import RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee
from typing import Optional, Set
from typing_extensions import Self

class RestV11ProjectsProjectIdDirectCostsGet200ResponseInner(BaseModel):
    """
    RestV11ProjectsProjectIdDirectCostsGet200ResponseInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    amount: Optional[StrictStr] = Field(default=None, description="Grand total")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    deleted_at: Optional[datetime] = Field(default=None, description="Deleted at")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    direct_cost_type: Optional[StrictStr] = Field(default=None, description="Type")
    direct_cost_date: Optional[date] = Field(default=None, description="Date")
    grand_total: Optional[StrictStr] = Field(default=None, description="Grand total")
    invoice_number: Optional[StrictStr] = Field(default=None, description="Unique identifier for a Direct Cost Item of type invoice")
    origin_data: Optional[StrictStr] = Field(default=None, description="Origin Data")
    origin_id: Optional[StrictStr] = Field(default=None, description="Origin ID")
    payment_date: Optional[date] = Field(default=None, description="Payment Date")
    received_date: Optional[date] = Field(default=None, description="Received Date")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    terms: Optional[StrictStr] = Field(default=None, description="The agreed upon Terms for the date of payment")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    vendor: Optional[StrictStr] = Field(default=None, description="Vendor name")
    vendor_id: Optional[StrictInt] = Field(default=None, description="Vendor ID")
    vendor_name: Optional[StrictStr] = Field(default=None, description="Vendor name")
    currency_configuration: Optional[RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration] = None
    employee: Optional[RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee] = None
    __properties: ClassVar[List[str]] = ["id", "amount", "created_at", "deleted_at", "description", "direct_cost_type", "direct_cost_date", "grand_total", "invoice_number", "origin_data", "origin_id", "payment_date", "received_date", "status", "terms", "updated_at", "vendor", "vendor_id", "vendor_name", "currency_configuration", "employee"]

    @field_validator('direct_cost_type')
    def direct_cost_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['invoice', 'expense', 'payroll']):
            raise ValueError("must be one of enum values ('invoice', 'expense', 'payroll')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['draft', 'pending', 'revise_and_resubmit', 'approved']):
            raise ValueError("must be one of enum values ('draft', 'pending', 'revise_and_resubmit', 'approved')")
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
        """Create an instance of RestV11ProjectsProjectIdDirectCostsGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of employee
        if self.employee:
            _dict['employee'] = self.employee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV11ProjectsProjectIdDirectCostsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "amount": obj.get("amount"),
            "created_at": obj.get("created_at"),
            "deleted_at": obj.get("deleted_at"),
            "description": obj.get("description"),
            "direct_cost_type": obj.get("direct_cost_type"),
            "direct_cost_date": obj.get("direct_cost_date"),
            "grand_total": obj.get("grand_total"),
            "invoice_number": obj.get("invoice_number"),
            "origin_data": obj.get("origin_data"),
            "origin_id": obj.get("origin_id"),
            "payment_date": obj.get("payment_date"),
            "received_date": obj.get("received_date"),
            "status": obj.get("status"),
            "terms": obj.get("terms"),
            "updated_at": obj.get("updated_at"),
            "vendor": obj.get("vendor"),
            "vendor_id": obj.get("vendor_id"),
            "vendor_name": obj.get("vendor_name"),
            "currency_configuration": RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration.from_dict(obj["currency_configuration"]) if obj.get("currency_configuration") is not None else None,
            "employee": RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee.from_dict(obj["employee"]) if obj.get("employee") is not None else None
        })
        return _obj


