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
from procore_sdk.models.line_item_type import LineItemType
from procore_sdk.models.rest_v10_projects_project_id_waste_logs_get200_response_inner_vendor import RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_cost_code import RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode
from procore_sdk.models.rfq_change_event_change_event_line_items_inner_budget_mod import RFQChangeEventChangeEventLineItemsInnerBudgetMod
from procore_sdk.models.rfq_change_event_change_event_line_items_inner_contract import RFQChangeEventChangeEventLineItemsInnerContract
from procore_sdk.models.rfq_change_event_change_event_line_items_inner_links import RFQChangeEventChangeEventLineItemsInnerLinks
from procore_sdk.models.rfq_change_event_change_event_line_items_inner_statuses import RFQChangeEventChangeEventLineItemsInnerStatuses
from typing import Optional, Set
from typing_extensions import Self

class RFQChangeEventChangeEventLineItemsInner(BaseModel):
    """
    RFQChangeEventChangeEventLineItemsInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    cost_code_biller_name: Optional[StrictStr] = Field(default=None, description="Cost Code biller name")
    cost_code: Optional[RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode] = None
    cost_code_is_budgeted: Optional[StrictBool] = Field(default=None, description="Cost Code budgeted status")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    event_id: Optional[StrictInt] = Field(default=None, description="Event ID")
    line_item_type: Optional[LineItemType] = None
    rom: Optional[StrictInt] = Field(default=None, description="Rough order of magnitude (ROM)")
    contract: Optional[RFQChangeEventChangeEventLineItemsInnerContract] = None
    links: Optional[RFQChangeEventChangeEventLineItemsInnerLinks] = None
    statuses: Optional[RFQChangeEventChangeEventLineItemsInnerStatuses] = None
    number: Optional[StrictStr] = Field(default=None, description="Number")
    status: Optional[StrictStr] = Field(default=None, description="Change Event Status name")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    vendor: Optional[RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor] = None
    commitment_contract_cost: Optional[StrictStr] = Field(default=None, description="Commitment contract cost")
    commitment_pco_cost: Optional[StrictStr] = Field(default=None, description="Commitment Potential Change Order cost")
    budget_mod_amount: Optional[StrictStr] = Field(default=None, description="Budget Modification transfer amount")
    budget_mod: Optional[RFQChangeEventChangeEventLineItemsInnerBudgetMod] = None
    prime_pco_cost: Optional[StrictStr] = Field(default=None, description="Prime Potential Change Order cost")
    rfq_amount: Optional[StrictStr] = Field(default=None, description="RFQ amount")
    rfq_status: Optional[StrictStr] = Field(default=None, description="RFQ status")
    __properties: ClassVar[List[str]] = ["id", "cost_code_biller_name", "cost_code", "cost_code_is_budgeted", "description", "event_id", "line_item_type", "rom", "contract", "links", "statuses", "number", "status", "title", "vendor", "commitment_contract_cost", "commitment_pco_cost", "budget_mod_amount", "budget_mod", "prime_pco_cost", "rfq_amount", "rfq_status"]

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
        """Create an instance of RFQChangeEventChangeEventLineItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of budget_mod
        if self.budget_mod:
            _dict['budget_mod'] = self.budget_mod.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RFQChangeEventChangeEventLineItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "cost_code_biller_name": obj.get("cost_code_biller_name"),
            "cost_code": RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.from_dict(obj["cost_code"]) if obj.get("cost_code") is not None else None,
            "cost_code_is_budgeted": obj.get("cost_code_is_budgeted"),
            "description": obj.get("description"),
            "event_id": obj.get("event_id"),
            "line_item_type": LineItemType.from_dict(obj["line_item_type"]) if obj.get("line_item_type") is not None else None,
            "rom": obj.get("rom"),
            "contract": RFQChangeEventChangeEventLineItemsInnerContract.from_dict(obj["contract"]) if obj.get("contract") is not None else None,
            "links": RFQChangeEventChangeEventLineItemsInnerLinks.from_dict(obj["links"]) if obj.get("links") is not None else None,
            "statuses": RFQChangeEventChangeEventLineItemsInnerStatuses.from_dict(obj["statuses"]) if obj.get("statuses") is not None else None,
            "number": obj.get("number"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "vendor": RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.from_dict(obj["vendor"]) if obj.get("vendor") is not None else None,
            "commitment_contract_cost": obj.get("commitment_contract_cost"),
            "commitment_pco_cost": obj.get("commitment_pco_cost"),
            "budget_mod_amount": obj.get("budget_mod_amount"),
            "budget_mod": RFQChangeEventChangeEventLineItemsInnerBudgetMod.from_dict(obj["budget_mod"]) if obj.get("budget_mod") is not None else None,
            "prime_pco_cost": obj.get("prime_pco_cost"),
            "rfq_amount": obj.get("rfq_amount"),
            "rfq_status": obj.get("rfq_status")
        })
        return _obj


