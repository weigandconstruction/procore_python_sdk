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
from procore_sdk.models.rest_v10_purchase_order_contracts_get200_response_inner_assignee import RestV10PurchaseOrderContractsGet200ResponseInnerAssignee
from procore_sdk.models.rest_v10_purchase_order_contracts_post201_response_change_order_packages_inner import RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner
from procore_sdk.models.rest_v10_purchase_order_contracts_post201_response_potential_change_orders_inner_inner import RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner
from procore_sdk.models.rest_v10_work_order_contracts_get200_response_inner_currency_configuration import RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration
from procore_sdk.models.rest_v10_work_order_contracts_get200_response_inner_project import RestV10WorkOrderContractsGet200ResponseInnerProject
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_attachments_inner import RestV10WorkOrderContractsPost201ResponseAttachmentsInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_change_order_requests_inner_inner import RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_invoice_contacts_inner import RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner import RestV10WorkOrderContractsPost201ResponseLineItemsInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_payments_issued_inner import RestV10WorkOrderContractsPost201ResponsePaymentsIssuedInner
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_vendor import RestV10WorkOrderContractsPost201ResponseVendor
from typing import Optional, Set
from typing_extensions import Self

class RestV10PurchaseOrderContractsPost201Response(BaseModel):
    """
    Purchase Order Contract
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    accounting_method: Optional[StrictStr] = Field(default=None, description="Accounting method")
    approval_letter_date: Optional[StrictStr] = Field(default=None, description="Approval letter date")
    approved_change_orders: Optional[StrictStr] = Field(default=None, description="Approved Change Orders Amount")
    assignee: Optional[RestV10PurchaseOrderContractsGet200ResponseInnerAssignee] = None
    attachments: Optional[RestV10WorkOrderContractsPost201ResponseAttachmentsInner] = None
    bill_to_address: Optional[StrictStr] = Field(default=None, description="Bill to Address")
    change_order_packages: Optional[List[RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner]] = None
    change_order_requests: Optional[List[RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner]] = None
    contract_date: Optional[date] = Field(default=None, description="Contract date")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    created_by_id: Optional[StrictInt] = Field(default=None, description="ID of the user who created the Contract")
    deleted_at: Optional[datetime] = Field(default=None, description="Deleted at")
    delivery_date: Optional[date] = Field(default=None, description="Delivery date")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    draft_change_orders_amount: Optional[StrictStr] = Field(default=None, description="Total of all draft change orders")
    executed: Optional[StrictBool] = Field(default=None, description="Executed status")
    execution_date: Optional[date] = Field(default=None, description="Execution date")
    grand_total: Optional[StrictStr] = Field(default=None, description="Grand total")
    invoice_contacts: Optional[List[RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner]] = Field(default=None, description="Invoice Contacts")
    issued_on_date: Optional[date] = Field(default=None, description="Issued on")
    letter_of_intent_date: Optional[date] = Field(default=None, description="Letter of intent date")
    line_items: Optional[List[RestV10WorkOrderContractsPost201ResponseLineItemsInner]] = Field(default=None, description="Line items")
    number: Optional[StrictStr] = Field(default=None, description="Number")
    origin_code: Optional[StrictStr] = Field(default=None, description="Origin code")
    origin_data: Optional[StrictStr] = Field(default=None, description="Origin data")
    origin_id: Optional[StrictStr] = Field(default=None, description="Origin ID")
    payment_terms: Optional[StrictStr] = Field(default=None, description="Payment terms")
    payments_issued: Optional[List[RestV10WorkOrderContractsPost201ResponsePaymentsIssuedInner]] = Field(default=None, description="Payments issued")
    pending_change_orders: Optional[StrictStr] = Field(default=None, description="Pending Change Orders amount")
    pending_revised_contract: Optional[StrictStr] = Field(default=None, description="Pending Revised Contract amount")
    percentage_paid: Optional[StrictStr] = Field(default=None, description="Percentage paid amount")
    potential_change_orders: Optional[List[List[RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner]]] = Field(default=None, description="Potential Change Orders")
    private: Optional[StrictBool] = Field(default=None, description="Enable/Disable Pivate status")
    project: Optional[RestV10WorkOrderContractsGet200ResponseInnerProject] = None
    remaining_balance_outstanding: Optional[StrictStr] = Field(default=None, description="Remaining Balance Outstanding amount")
    requisitions_are_enabled: Optional[StrictBool] = Field(default=None, description="If true, Requisitions (Subcontractor Invoices) are enabled on the Commitment Contract")
    retainage_percent: Optional[StrictStr] = Field(default=None, description="Retainage Percent")
    returned_date: Optional[date] = Field(default=None, description="Returned date")
    revised_contract: Optional[StrictStr] = Field(default=None, description="Revised contracts amount")
    ship_to_address: Optional[StrictStr] = Field(default=None, description="Ship to address")
    ship_via: Optional[StrictStr] = Field(default=None, description="Ship via")
    show_line_items_to_non_admins: Optional[StrictBool] = Field(default=None, description="If true and the contract is private, non admins with access to the contract will be able to view the SOV items")
    signed_contract_received_date: Optional[date] = Field(default=None, description="Signed contract received date")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    total_draw_requests_amount: Optional[StrictStr] = Field(default=None, description="Total Draw Requests amount")
    total_payments: Optional[StrictStr] = Field(default=None, description="Total Payments amount")
    total_requisitions_amount: Optional[StrictStr] = Field(default=None, description="Total Requisitions (Subcontractor Invoices) amount")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    vendor: Optional[RestV10WorkOrderContractsPost201ResponseVendor] = None
    currency_configuration: Optional[RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration] = None
    __properties: ClassVar[List[str]] = ["id", "accounting_method", "approval_letter_date", "approved_change_orders", "assignee", "attachments", "bill_to_address", "change_order_packages", "change_order_requests", "contract_date", "created_at", "created_by_id", "deleted_at", "delivery_date", "description", "draft_change_orders_amount", "executed", "execution_date", "grand_total", "invoice_contacts", "issued_on_date", "letter_of_intent_date", "line_items", "number", "origin_code", "origin_data", "origin_id", "payment_terms", "payments_issued", "pending_change_orders", "pending_revised_contract", "percentage_paid", "potential_change_orders", "private", "project", "remaining_balance_outstanding", "requisitions_are_enabled", "retainage_percent", "returned_date", "revised_contract", "ship_to_address", "ship_via", "show_line_items_to_non_admins", "signed_contract_received_date", "status", "title", "total_draw_requests_amount", "total_payments", "total_requisitions_amount", "updated_at", "vendor", "currency_configuration"]

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

        if value not in set(['Draft', 'Processing', 'Submitted', 'Partially Received', 'Received', 'Approved', 'Closed']):
            raise ValueError("must be one of enum values ('Draft', 'Processing', 'Submitted', 'Partially Received', 'Received', 'Approved', 'Closed')")
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
        """Create an instance of RestV10PurchaseOrderContractsPost201Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of assignee
        if self.assignee:
            _dict['assignee'] = self.assignee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attachments
        if self.attachments:
            _dict['attachments'] = self.attachments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in change_order_packages (list)
        _items = []
        if self.change_order_packages:
            for _item_change_order_packages in self.change_order_packages:
                if _item_change_order_packages:
                    _items.append(_item_change_order_packages.to_dict())
            _dict['change_order_packages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in change_order_requests (list)
        _items = []
        if self.change_order_requests:
            for _item_change_order_requests in self.change_order_requests:
                if _item_change_order_requests:
                    _items.append(_item_change_order_requests.to_dict())
            _dict['change_order_requests'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in invoice_contacts (list)
        _items = []
        if self.invoice_contacts:
            for _item_invoice_contacts in self.invoice_contacts:
                if _item_invoice_contacts:
                    _items.append(_item_invoice_contacts.to_dict())
            _dict['invoice_contacts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['line_items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payments_issued (list)
        _items = []
        if self.payments_issued:
            for _item_payments_issued in self.payments_issued:
                if _item_payments_issued:
                    _items.append(_item_payments_issued.to_dict())
            _dict['payments_issued'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in potential_change_orders (list of list)
        _items = []
        if self.potential_change_orders:
            for _item_potential_change_orders in self.potential_change_orders:
                if _item_potential_change_orders:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item_potential_change_orders if _inner_item is not None]
                    )
            _dict['potential_change_orders'] = _items
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vendor
        if self.vendor:
            _dict['vendor'] = self.vendor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_configuration
        if self.currency_configuration:
            _dict['currency_configuration'] = self.currency_configuration.to_dict()
        # set to None if origin_id (nullable) is None
        # and model_fields_set contains the field
        if self.origin_id is None and "origin_id" in self.model_fields_set:
            _dict['origin_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10PurchaseOrderContractsPost201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "accounting_method": obj.get("accounting_method"),
            "approval_letter_date": obj.get("approval_letter_date"),
            "approved_change_orders": obj.get("approved_change_orders"),
            "assignee": RestV10PurchaseOrderContractsGet200ResponseInnerAssignee.from_dict(obj["assignee"]) if obj.get("assignee") is not None else None,
            "attachments": RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(obj["attachments"]) if obj.get("attachments") is not None else None,
            "bill_to_address": obj.get("bill_to_address"),
            "change_order_packages": [RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner.from_dict(_item) for _item in obj["change_order_packages"]] if obj.get("change_order_packages") is not None else None,
            "change_order_requests": [RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner.from_dict(_item) for _item in obj["change_order_requests"]] if obj.get("change_order_requests") is not None else None,
            "contract_date": obj.get("contract_date"),
            "created_at": obj.get("created_at"),
            "created_by_id": obj.get("created_by_id"),
            "deleted_at": obj.get("deleted_at"),
            "delivery_date": obj.get("delivery_date"),
            "description": obj.get("description"),
            "draft_change_orders_amount": obj.get("draft_change_orders_amount"),
            "executed": obj.get("executed"),
            "execution_date": obj.get("execution_date"),
            "grand_total": obj.get("grand_total"),
            "invoice_contacts": [RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner.from_dict(_item) for _item in obj["invoice_contacts"]] if obj.get("invoice_contacts") is not None else None,
            "issued_on_date": obj.get("issued_on_date"),
            "letter_of_intent_date": obj.get("letter_of_intent_date"),
            "line_items": [RestV10WorkOrderContractsPost201ResponseLineItemsInner.from_dict(_item) for _item in obj["line_items"]] if obj.get("line_items") is not None else None,
            "number": obj.get("number"),
            "origin_code": obj.get("origin_code"),
            "origin_data": obj.get("origin_data"),
            "origin_id": obj.get("origin_id"),
            "payment_terms": obj.get("payment_terms"),
            "payments_issued": [RestV10WorkOrderContractsPost201ResponsePaymentsIssuedInner.from_dict(_item) for _item in obj["payments_issued"]] if obj.get("payments_issued") is not None else None,
            "pending_change_orders": obj.get("pending_change_orders"),
            "pending_revised_contract": obj.get("pending_revised_contract"),
            "percentage_paid": obj.get("percentage_paid"),
            "potential_change_orders": [
                    [RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["potential_change_orders"]
                ] if obj.get("potential_change_orders") is not None else None,
            "private": obj.get("private"),
            "project": RestV10WorkOrderContractsGet200ResponseInnerProject.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "remaining_balance_outstanding": obj.get("remaining_balance_outstanding"),
            "requisitions_are_enabled": obj.get("requisitions_are_enabled"),
            "retainage_percent": obj.get("retainage_percent"),
            "returned_date": obj.get("returned_date"),
            "revised_contract": obj.get("revised_contract"),
            "ship_to_address": obj.get("ship_to_address"),
            "ship_via": obj.get("ship_via"),
            "show_line_items_to_non_admins": obj.get("show_line_items_to_non_admins"),
            "signed_contract_received_date": obj.get("signed_contract_received_date"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "total_draw_requests_amount": obj.get("total_draw_requests_amount"),
            "total_payments": obj.get("total_payments"),
            "total_requisitions_amount": obj.get("total_requisitions_amount"),
            "updated_at": obj.get("updated_at"),
            "vendor": RestV10WorkOrderContractsPost201ResponseVendor.from_dict(obj["vendor"]) if obj.get("vendor") is not None else None,
            "currency_configuration": RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.from_dict(obj["currency_configuration"]) if obj.get("currency_configuration") is not None else None
        })
        return _obj


