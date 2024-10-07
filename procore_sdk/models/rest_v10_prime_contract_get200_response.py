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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_prime_contracts_get200_response_inner_contractor import RestV10PrimeContractsGet200ResponseInnerContractor
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from procore_sdk.models.rest_v10_work_order_contracts_get200_response_inner_currency_configuration import RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_attachments_inner import RestV10WorkOrderContractsPost201ResponseAttachmentsInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_change_order_packages_inner import RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_change_order_requests_inner_inner import RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner import RestV10WorkOrderContractsPost201ResponseLineItemsInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_cost_code import RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_payments_issued_inner import RestV10WorkOrderContractsPost201ResponsePaymentsIssuedInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_potential_change_orders_inner import RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner
from typing import Optional, Set
from typing_extensions import Self

class RestV10PrimeContractGet200Response(BaseModel):
    """
    Prime Contract
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Prime Contract ID")
    accounting_method: Optional[StrictStr] = Field(default=None, description="Accounting method")
    actual_completion_date: Optional[date] = Field(default=None, description="Actual completion date")
    allow_comments: Optional[StrictBool] = Field(default=None, description="Allow comments status")
    allow_markups: Optional[StrictBool] = Field(default=None, description="Allow markups status")
    allow_payment_applications: Optional[StrictBool] = Field(default=None, description="Enable/Disable Payment Applications (Owner Invoices)")
    allow_payments: Optional[StrictBool] = Field(default=None, description="Enable/Disable payments")
    allow_redistributions: Optional[StrictBool] = Field(default=None, description="Deprecated - always false")
    approval_letter_date: Optional[date] = Field(default=None, description="Approval letter date")
    approved_change_orders: Optional[StrictStr] = Field(default=None, description="Approved change orders amount")
    bill_to: Optional[StrictStr] = Field(default=None, description="Bill to address")
    budget_line_item_id: Optional[StrictInt] = Field(default=None, description="Budget line item ID")
    contract_date: Optional[date] = Field(default=None, description="Contract date")
    contract_estimated_completion_date: Optional[date] = Field(default=None, description="Contract estimated completion date")
    contract_start_date: Optional[date] = Field(default=None, description="Contract start date")
    contract_termination_date: Optional[date] = Field(default=None, description="Contract termination date")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    deleted_at: Optional[datetime] = Field(default=None, description="Deleted at")
    delivery_date: Optional[date] = Field(default=None, description="Delivery date")
    description: Optional[StrictStr] = Field(default=None, description="Description of the Prime Contract")
    display_materials_retainage: Optional[StrictBool] = Field(default=None, description="Display materials retainage status")
    display_stored_materials: Optional[StrictBool] = Field(default=None, description="Enable/Disable stored materials")
    display_work_retainage: Optional[StrictBool] = Field(default=None, description="Display work retainage")
    draft_change_orders_amount: Optional[StrictStr] = Field(default=None, description="Total of all draft change orders")
    exclusions: Optional[StrictStr] = Field(default=None, description="Exclusions")
    executed: Optional[StrictBool] = Field(default=None, description="Executed status")
    execution_date: Optional[date] = Field(default=None, description="Execution date")
    grand_total: Optional[StrictStr] = Field(default=None, description="Total of Line items including markup, plus project level (vertical) markup, if any")
    inclusions: Optional[StrictStr] = Field(default=None, description="Inclusions")
    issued_on_date: Optional[date] = Field(default=None, description="Issued on date")
    letter_of_intent_date: Optional[date] = Field(default=None, description="Letter of intent date")
    line_items_extended_total: Optional[StrictStr] = Field(default=None, description="Total of Line items including markup")
    line_items_total: Optional[StrictStr] = Field(default=None, description="Total of Line items without markup")
    number: Optional[StrictStr] = Field(default=None, description="Number")
    origin_data: Optional[StrictStr] = Field(default=None, description="Prime Contract third party data")
    origin_id: Optional[StrictStr] = Field(default=None, description="Prime Contract third party ID")
    outstanding_balance: Optional[StrictStr] = Field(default=None, description="Revised contract amount minus total payments")
    owner_invoices_amount: Optional[StrictStr] = Field(default=None, description="Total of owner invoices")
    payment_terms: Optional[StrictStr] = Field(default=None, description="Payment terms")
    pending_change_orders_amount: Optional[StrictStr] = Field(default=None, description="Total of all pending and revised change orders")
    pending_revised_contract_amount: Optional[StrictStr] = Field(default=None, description="Revised contract amount, plus pending and revised change orders")
    percentage_paid: Optional[StrictStr] = Field(default=None, description="Percentage paid")
    position: Optional[StrictInt] = Field(default=None, description="Position")
    private: Optional[StrictBool] = Field(default=None, description="If true, visible to admins only; otherwise visible to those with access to the parent contract.")
    requisition_number: Optional[StrictStr] = Field(default=None, description="Requisition (Subcontractor Invoice) number")
    retainage_percent: Optional[StrictStr] = Field(default=None, description="Retainage percent")
    returned_date: Optional[date] = Field(default=None, description="Returned date")
    revised_contract_amount: Optional[StrictStr] = Field(default=None, description="Grand total, plus approved change orders")
    ship_to: Optional[StrictStr] = Field(default=None, description="Ship to address")
    ship_via: Optional[StrictStr] = Field(default=None, description="Ship via")
    signed_contract_received_date: Optional[date] = Field(default=None, description="Signed contract received date")
    show_line_items_to_non_admins: Optional[StrictBool] = Field(default=None, description="If true and the contract is private, non admins with access to the contract will be able to view the SOV items")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    total_payments: Optional[StrictStr] = Field(default=None, description="Total payments")
    type: Optional[StrictStr] = Field(default=None, description="Type")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    original_substantial_completion_date: Optional[date] = Field(default=None, description="Original substantial completion date")
    substantial_completion_date: Optional[date] = Field(default=None, description="Substantial completion date")
    architect: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    assigned_to: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    attachments: Optional[List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]] = Field(default=None, description="Attachments")
    change_order_packages: Optional[List[RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner]] = Field(default=None, description="Change order packages")
    change_order_requests: Optional[List[List[RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner]]] = Field(default=None, description="Change order requests")
    contractor: Optional[RestV10PrimeContractsGet200ResponseInnerContractor] = None
    cost_code: Optional[RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode] = None
    created_by: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    line_items: Optional[List[RestV10WorkOrderContractsPost201ResponseLineItemsInner]] = Field(default=None, description="Line items")
    potential_change_orders: Optional[List[RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner]] = Field(default=None, description="Potential change orders")
    payments_received: Optional[List[RestV10WorkOrderContractsPost201ResponsePaymentsIssuedInner]] = Field(default=None, description="Payments received")
    received_from: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    vendor: Optional[RestV10PrimeContractsGet200ResponseInnerContractor] = None
    currency_configuration: Optional[RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration] = None
    __properties: ClassVar[List[str]] = ["id", "accounting_method", "actual_completion_date", "allow_comments", "allow_markups", "allow_payment_applications", "allow_payments", "allow_redistributions", "approval_letter_date", "approved_change_orders", "bill_to", "budget_line_item_id", "contract_date", "contract_estimated_completion_date", "contract_start_date", "contract_termination_date", "created_at", "deleted_at", "delivery_date", "description", "display_materials_retainage", "display_stored_materials", "display_work_retainage", "draft_change_orders_amount", "exclusions", "executed", "execution_date", "grand_total", "inclusions", "issued_on_date", "letter_of_intent_date", "line_items_extended_total", "line_items_total", "number", "origin_data", "origin_id", "outstanding_balance", "owner_invoices_amount", "payment_terms", "pending_change_orders_amount", "pending_revised_contract_amount", "percentage_paid", "position", "private", "requisition_number", "retainage_percent", "returned_date", "revised_contract_amount", "ship_to", "ship_via", "signed_contract_received_date", "show_line_items_to_non_admins", "status", "title", "total_payments", "type", "updated_at", "original_substantial_completion_date", "substantial_completion_date", "architect", "assigned_to", "attachments", "change_order_packages", "change_order_requests", "contractor", "cost_code", "created_by", "line_items", "potential_change_orders", "payments_received", "received_from", "vendor", "currency_configuration"]

    @field_validator('accounting_method')
    def accounting_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['amount', 'unit']):
            raise ValueError("must be one of enum values ('amount', 'unit')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Draft', 'Out For Bid', 'Out For Signature', 'Approved', 'Complete', 'Terminated']):
            raise ValueError("must be one of enum values ('Draft', 'Out For Bid', 'Out For Signature', 'Approved', 'Complete', 'Terminated')")
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
        """Create an instance of RestV10PrimeContractGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of architect
        if self.architect:
            _dict['architect'] = self.architect.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assigned_to
        if self.assigned_to:
            _dict['assigned_to'] = self.assigned_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in change_order_packages (list)
        _items = []
        if self.change_order_packages:
            for _item_change_order_packages in self.change_order_packages:
                if _item_change_order_packages:
                    _items.append(_item_change_order_packages.to_dict())
            _dict['change_order_packages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in change_order_requests (list of list)
        _items = []
        if self.change_order_requests:
            for _item_change_order_requests in self.change_order_requests:
                if _item_change_order_requests:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item_change_order_requests if _inner_item is not None]
                    )
            _dict['change_order_requests'] = _items
        # override the default output from pydantic by calling `to_dict()` of contractor
        if self.contractor:
            _dict['contractor'] = self.contractor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cost_code
        if self.cost_code:
            _dict['cost_code'] = self.cost_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['line_items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in potential_change_orders (list)
        _items = []
        if self.potential_change_orders:
            for _item_potential_change_orders in self.potential_change_orders:
                if _item_potential_change_orders:
                    _items.append(_item_potential_change_orders.to_dict())
            _dict['potential_change_orders'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payments_received (list)
        _items = []
        if self.payments_received:
            for _item_payments_received in self.payments_received:
                if _item_payments_received:
                    _items.append(_item_payments_received.to_dict())
            _dict['payments_received'] = _items
        # override the default output from pydantic by calling `to_dict()` of received_from
        if self.received_from:
            _dict['received_from'] = self.received_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vendor
        if self.vendor:
            _dict['vendor'] = self.vendor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_configuration
        if self.currency_configuration:
            _dict['currency_configuration'] = self.currency_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10PrimeContractGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "accounting_method": obj.get("accounting_method"),
            "actual_completion_date": obj.get("actual_completion_date"),
            "allow_comments": obj.get("allow_comments"),
            "allow_markups": obj.get("allow_markups"),
            "allow_payment_applications": obj.get("allow_payment_applications"),
            "allow_payments": obj.get("allow_payments"),
            "allow_redistributions": obj.get("allow_redistributions"),
            "approval_letter_date": obj.get("approval_letter_date"),
            "approved_change_orders": obj.get("approved_change_orders"),
            "bill_to": obj.get("bill_to"),
            "budget_line_item_id": obj.get("budget_line_item_id"),
            "contract_date": obj.get("contract_date"),
            "contract_estimated_completion_date": obj.get("contract_estimated_completion_date"),
            "contract_start_date": obj.get("contract_start_date"),
            "contract_termination_date": obj.get("contract_termination_date"),
            "created_at": obj.get("created_at"),
            "deleted_at": obj.get("deleted_at"),
            "delivery_date": obj.get("delivery_date"),
            "description": obj.get("description"),
            "display_materials_retainage": obj.get("display_materials_retainage"),
            "display_stored_materials": obj.get("display_stored_materials"),
            "display_work_retainage": obj.get("display_work_retainage"),
            "draft_change_orders_amount": obj.get("draft_change_orders_amount"),
            "exclusions": obj.get("exclusions"),
            "executed": obj.get("executed"),
            "execution_date": obj.get("execution_date"),
            "grand_total": obj.get("grand_total"),
            "inclusions": obj.get("inclusions"),
            "issued_on_date": obj.get("issued_on_date"),
            "letter_of_intent_date": obj.get("letter_of_intent_date"),
            "line_items_extended_total": obj.get("line_items_extended_total"),
            "line_items_total": obj.get("line_items_total"),
            "number": obj.get("number"),
            "origin_data": obj.get("origin_data"),
            "origin_id": obj.get("origin_id"),
            "outstanding_balance": obj.get("outstanding_balance"),
            "owner_invoices_amount": obj.get("owner_invoices_amount"),
            "payment_terms": obj.get("payment_terms"),
            "pending_change_orders_amount": obj.get("pending_change_orders_amount"),
            "pending_revised_contract_amount": obj.get("pending_revised_contract_amount"),
            "percentage_paid": obj.get("percentage_paid"),
            "position": obj.get("position"),
            "private": obj.get("private"),
            "requisition_number": obj.get("requisition_number"),
            "retainage_percent": obj.get("retainage_percent"),
            "returned_date": obj.get("returned_date"),
            "revised_contract_amount": obj.get("revised_contract_amount"),
            "ship_to": obj.get("ship_to"),
            "ship_via": obj.get("ship_via"),
            "signed_contract_received_date": obj.get("signed_contract_received_date"),
            "show_line_items_to_non_admins": obj.get("show_line_items_to_non_admins"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "total_payments": obj.get("total_payments"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "original_substantial_completion_date": obj.get("original_substantial_completion_date"),
            "substantial_completion_date": obj.get("substantial_completion_date"),
            "architect": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["architect"]) if obj.get("architect") is not None else None,
            "assigned_to": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["assigned_to"]) if obj.get("assigned_to") is not None else None,
            "attachments": [RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "change_order_packages": [RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner.from_dict(_item) for _item in obj["change_order_packages"]] if obj.get("change_order_packages") is not None else None,
            "change_order_requests": [
                    [RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["change_order_requests"]
                ] if obj.get("change_order_requests") is not None else None,
            "contractor": RestV10PrimeContractsGet200ResponseInnerContractor.from_dict(obj["contractor"]) if obj.get("contractor") is not None else None,
            "cost_code": RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.from_dict(obj["cost_code"]) if obj.get("cost_code") is not None else None,
            "created_by": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "line_items": [RestV10WorkOrderContractsPost201ResponseLineItemsInner.from_dict(_item) for _item in obj["line_items"]] if obj.get("line_items") is not None else None,
            "potential_change_orders": [RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner.from_dict(_item) for _item in obj["potential_change_orders"]] if obj.get("potential_change_orders") is not None else None,
            "payments_received": [RestV10WorkOrderContractsPost201ResponsePaymentsIssuedInner.from_dict(_item) for _item in obj["payments_received"]] if obj.get("payments_received") is not None else None,
            "received_from": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["received_from"]) if obj.get("received_from") is not None else None,
            "vendor": RestV10PrimeContractsGet200ResponseInnerContractor.from_dict(obj["vendor"]) if obj.get("vendor") is not None else None,
            "currency_configuration": RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.from_dict(obj["currency_configuration"]) if obj.get("currency_configuration") is not None else None
        })
        return _obj


