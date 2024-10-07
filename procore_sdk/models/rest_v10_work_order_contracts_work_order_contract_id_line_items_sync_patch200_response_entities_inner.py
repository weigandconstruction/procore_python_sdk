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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.line_item_type import LineItemType
from procore_sdk.models.rest_v10_work_order_contracts_get200_response_inner_currency_configuration import RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration
from procore_sdk.models.rest_v10_work_order_contracts_get200_response_inner_project import RestV10WorkOrderContractsGet200ResponseInnerProject
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_company import RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_cost_code import RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_holder import RestV10WorkOrderContractsPost201ResponseLineItemsInnerHolder
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_wbs_code import RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_entities_inner_change_event_line_item import RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem
from typing import Optional, Set
from typing_extensions import Self

class RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInner(BaseModel):
    """
    Line Item
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Line Item id")
    amount: Optional[StrictStr] = Field(default=None, description="Line Item amount")
    company: Optional[RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany] = None
    cost_code: Optional[RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode] = None
    created_at: Optional[datetime] = Field(default=None, description="Created at date and time")
    description: Optional[StrictStr] = Field(default=None, description="Line Item description")
    extended_type: Optional[StrictStr] = Field(default=None, description="Line Item extended type")
    holder: Optional[RestV10WorkOrderContractsPost201ResponseLineItemsInnerHolder] = None
    line_item_type: Optional[LineItemType] = None
    origin_data: Optional[StrictStr] = Field(default=None, description="Line Item third party data")
    origin_id: Optional[StrictStr] = Field(default=None, description="Line Item third party id")
    position: Optional[StrictInt] = Field(default=None, description="Line Item position")
    project: Optional[RestV10WorkOrderContractsGet200ResponseInnerProject] = None
    quantity: Optional[StrictStr] = Field(default=None, description="Line Item quantity")
    tax_code_id: Optional[StrictInt] = Field(default=None, description="Tax Code ID")
    total_amount: Optional[StrictStr] = Field(default=None, description="Line Item total amount")
    extended_amount: Optional[StrictStr] = Field(default=None, description="Line Item extended amount")
    unit_cost: Optional[StrictStr] = Field(default=None, description="Line Item unit cost")
    uom: Optional[StrictStr] = Field(default=None, description="Line Item units of measure")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at date and time")
    wbs_code: Optional[RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode] = None
    change_event_line_item: Optional[RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem] = None
    currency_configuration: Optional[RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration] = None
    __properties: ClassVar[List[str]] = ["id", "amount", "company", "cost_code", "created_at", "description", "extended_type", "holder", "line_item_type", "origin_data", "origin_id", "position", "project", "quantity", "tax_code_id", "total_amount", "extended_amount", "unit_cost", "uom", "updated_at", "wbs_code", "change_event_line_item", "currency_configuration"]

    @field_validator('extended_type')
    def extended_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['manual', 'calculated']):
            raise ValueError("must be one of enum values ('manual', 'calculated')")
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
        """Create an instance of RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cost_code
        if self.cost_code:
            _dict['cost_code'] = self.cost_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of holder
        if self.holder:
            _dict['holder'] = self.holder.to_dict()
        # override the default output from pydantic by calling `to_dict()` of line_item_type
        if self.line_item_type:
            _dict['line_item_type'] = self.line_item_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wbs_code
        if self.wbs_code:
            _dict['wbs_code'] = self.wbs_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change_event_line_item
        if self.change_event_line_item:
            _dict['change_event_line_item'] = self.change_event_line_item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_configuration
        if self.currency_configuration:
            _dict['currency_configuration'] = self.currency_configuration.to_dict()
        # set to None if origin_data (nullable) is None
        # and model_fields_set contains the field
        if self.origin_data is None and "origin_data" in self.model_fields_set:
            _dict['origin_data'] = None

        # set to None if origin_id (nullable) is None
        # and model_fields_set contains the field
        if self.origin_id is None and "origin_id" in self.model_fields_set:
            _dict['origin_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "amount": obj.get("amount"),
            "company": RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany.from_dict(obj["company"]) if obj.get("company") is not None else None,
            "cost_code": RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.from_dict(obj["cost_code"]) if obj.get("cost_code") is not None else None,
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "extended_type": obj.get("extended_type"),
            "holder": RestV10WorkOrderContractsPost201ResponseLineItemsInnerHolder.from_dict(obj["holder"]) if obj.get("holder") is not None else None,
            "line_item_type": LineItemType.from_dict(obj["line_item_type"]) if obj.get("line_item_type") is not None else None,
            "origin_data": obj.get("origin_data"),
            "origin_id": obj.get("origin_id"),
            "position": obj.get("position"),
            "project": RestV10WorkOrderContractsGet200ResponseInnerProject.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "quantity": obj.get("quantity"),
            "tax_code_id": obj.get("tax_code_id"),
            "total_amount": obj.get("total_amount"),
            "extended_amount": obj.get("extended_amount"),
            "unit_cost": obj.get("unit_cost"),
            "uom": obj.get("uom"),
            "updated_at": obj.get("updated_at"),
            "wbs_code": RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode.from_dict(obj["wbs_code"]) if obj.get("wbs_code") is not None else None,
            "change_event_line_item": RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem.from_dict(obj["change_event_line_item"]) if obj.get("change_event_line_item") is not None else None,
            "currency_configuration": RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.from_dict(obj["currency_configuration"]) if obj.get("currency_configuration") is not None else None
        })
        return _obj


