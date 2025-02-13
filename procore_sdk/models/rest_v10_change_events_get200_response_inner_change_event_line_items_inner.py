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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from procore_sdk.models.line_item_type import LineItemType
from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner_biller import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBiller
from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_code import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode
from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_mod import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod
from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner_contract import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract
from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner_links import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks
from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner_statuses import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses
from procore_sdk.models.rest_v10_projects_project_id_waste_logs_get200_response_inner_vendor import RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_cost_code import RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode
from procore_sdk.models.rfq_currency_configuration import RFQCurrencyConfiguration
from typing import Optional, Set
from typing_extensions import Self

class RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner(BaseModel):
    """
    RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    budget_code: Optional[RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode] = None
    cost_code_biller_name: Optional[StrictStr] = Field(default=None, description="Cost Code Biller name")
    cost_code: Optional[RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode] = None
    cost_code_is_budgeted: Optional[StrictBool] = Field(default=None, description="Cost Code is budgeted")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    event_id: Optional[StrictInt] = Field(default=None, description="Change Event ID")
    line_item_type: Optional[LineItemType] = None
    rom: Optional[StrictInt] = Field(default=None, description="Rough order of magnitude (ROM)")
    contract: Optional[RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract] = None
    links: Optional[RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks] = None
    statuses: Optional[RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses] = None
    number: Optional[StrictStr] = Field(default=None, description="Number")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    vendor: Optional[RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor] = None
    biller: Optional[RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBiller] = None
    proposed_vendor_id: Optional[StrictInt] = Field(default=None, description="Proposed Vendor ID")
    proposed_contract_id: Optional[StrictInt] = Field(default=None, description="Proposed Contract ID")
    uom: Optional[StrictStr] = Field(default=None, description="Unit of Measure")
    estimated_cost_amount: Optional[StrictStr] = Field(default=None, description="Estimated Cost Amount")
    estimated_cost_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Estimated Cost Quantity")
    estimated_cost_unit_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Estimated Cost Unit Cost")
    estimated_cost_calculation_strategy: Optional[StrictStr] = Field(default=None, description="Estimated Cost Calculation Strategy controls whether estimated_cost_amount is calculated by multiplying the quantity and unit_cost attributes or set manually to a provided value.")
    line_item_type_id: Optional[StrictInt] = Field(default=None, description="Line Item Type ID")
    cost_code_id: Optional[StrictInt] = Field(default=None, description="Cost Code ID")
    editable: Optional[StrictBool] = Field(default=None, description="Editable status")
    deletable: Optional[StrictBool] = Field(default=None, description="Deletable status")
    request_for_quote_id: Optional[StrictInt] = Field(default=None, description="Request For Quote ID")
    biller_guid: Optional[StrictStr] = Field(default=None, description="Biller GUID")
    commitment_contract_cost: Optional[StrictStr] = Field(default=None, description="Commitment Contract Cost")
    commitment_pco_cost: Optional[StrictStr] = Field(default=None, description="Commitment PCO Cost")
    budget_mod_amount: Optional[StrictStr] = Field(default=None, description="Budget Modification Amount")
    budget_mod: Optional[RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod] = None
    prime_pco_cost: Optional[StrictStr] = Field(default=None, description="Prime PCO Cost")
    rfq_amount: Optional[StrictStr] = Field(default=None, description="Request RFQ Amount")
    rfq_sent: Optional[StrictStr] = Field(default=None, description="RFQ status")
    currency_configuration: Optional[RFQCurrencyConfiguration] = None
    __properties: ClassVar[List[str]] = ["id", "budget_code", "cost_code_biller_name", "cost_code", "cost_code_is_budgeted", "description", "event_id", "line_item_type", "rom", "contract", "links", "statuses", "number", "status", "title", "vendor", "biller", "proposed_vendor_id", "proposed_contract_id", "uom", "estimated_cost_amount", "estimated_cost_quantity", "estimated_cost_unit_cost", "estimated_cost_calculation_strategy", "line_item_type_id", "cost_code_id", "editable", "deletable", "request_for_quote_id", "biller_guid", "commitment_contract_cost", "commitment_pco_cost", "budget_mod_amount", "budget_mod", "prime_pco_cost", "rfq_amount", "rfq_sent", "currency_configuration"]

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
        """Create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of budget_code
        if self.budget_code:
            _dict['budget_code'] = self.budget_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cost_code
        if self.cost_code:
            _dict['cost_code'] = self.cost_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of line_item_type
        if self.line_item_type:
            _dict['line_item_type'] = self.line_item_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contract
        if self.contract:
            _dict['contract'] = self.contract.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statuses
        if self.statuses:
            _dict['statuses'] = self.statuses.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vendor
        if self.vendor:
            _dict['vendor'] = self.vendor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of biller
        if self.biller:
            _dict['biller'] = self.biller.to_dict()
        # override the default output from pydantic by calling `to_dict()` of budget_mod
        if self.budget_mod:
            _dict['budget_mod'] = self.budget_mod.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_configuration
        if self.currency_configuration:
            _dict['currency_configuration'] = self.currency_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "budget_code": RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode.from_dict(obj["budget_code"]) if obj.get("budget_code") is not None else None,
            "cost_code_biller_name": obj.get("cost_code_biller_name"),
            "cost_code": RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.from_dict(obj["cost_code"]) if obj.get("cost_code") is not None else None,
            "cost_code_is_budgeted": obj.get("cost_code_is_budgeted"),
            "description": obj.get("description"),
            "event_id": obj.get("event_id"),
            "line_item_type": LineItemType.from_dict(obj["line_item_type"]) if obj.get("line_item_type") is not None else None,
            "rom": obj.get("rom"),
            "contract": RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract.from_dict(obj["contract"]) if obj.get("contract") is not None else None,
            "links": RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks.from_dict(obj["links"]) if obj.get("links") is not None else None,
            "statuses": RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses.from_dict(obj["statuses"]) if obj.get("statuses") is not None else None,
            "number": obj.get("number"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "vendor": RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.from_dict(obj["vendor"]) if obj.get("vendor") is not None else None,
            "biller": RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBiller.from_dict(obj["biller"]) if obj.get("biller") is not None else None,
            "proposed_vendor_id": obj.get("proposed_vendor_id"),
            "proposed_contract_id": obj.get("proposed_contract_id"),
            "uom": obj.get("uom"),
            "estimated_cost_amount": obj.get("estimated_cost_amount"),
            "estimated_cost_quantity": obj.get("estimated_cost_quantity"),
            "estimated_cost_unit_cost": obj.get("estimated_cost_unit_cost"),
            "estimated_cost_calculation_strategy": obj.get("estimated_cost_calculation_strategy"),
            "line_item_type_id": obj.get("line_item_type_id"),
            "cost_code_id": obj.get("cost_code_id"),
            "editable": obj.get("editable"),
            "deletable": obj.get("deletable"),
            "request_for_quote_id": obj.get("request_for_quote_id"),
            "biller_guid": obj.get("biller_guid"),
            "commitment_contract_cost": obj.get("commitment_contract_cost"),
            "commitment_pco_cost": obj.get("commitment_pco_cost"),
            "budget_mod_amount": obj.get("budget_mod_amount"),
            "budget_mod": RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod.from_dict(obj["budget_mod"]) if obj.get("budget_mod") is not None else None,
            "prime_pco_cost": obj.get("prime_pco_cost"),
            "rfq_amount": obj.get("rfq_amount"),
            "rfq_sent": obj.get("rfq_sent"),
            "currency_configuration": RFQCurrencyConfiguration.from_dict(obj["currency_configuration"]) if obj.get("currency_configuration") is not None else None
        })
        return _obj


