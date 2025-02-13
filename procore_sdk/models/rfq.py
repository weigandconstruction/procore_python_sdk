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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from procore_sdk.models.location import Location
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_cost_code import RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode
from procore_sdk.models.rfq_change_event import RFQChangeEvent
from procore_sdk.models.rfq_change_order_packages import RFQChangeOrderPackages
from procore_sdk.models.rfq_currency_configuration import RFQCurrencyConfiguration
from procore_sdk.models.rfq_potential_change_orders import RFQPotentialChangeOrders
from procore_sdk.models.rfq_quote2 import RFQQuote2
from procore_sdk.models.rfq_response2 import RFQResponse2
from procore_sdk.models.rfq_specification_section import RFQSpecificationSection
from typing import Optional, Set
from typing_extensions import Self

class RFQ(BaseModel):
    """
    RFQ
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    commitment_contract_id: Optional[StrictInt] = Field(default=None, description="Commitment Contract ID")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    deleted_at: Optional[datetime] = Field(default=None, description="Deleted at")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    due_date: Optional[date] = Field(default=None, description="Due date")
    estimated_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Estimated amount")
    estimated_schedule_impact: Optional[StrictInt] = Field(default=None, description="Estimated schedule impact in days")
    estimated_status: Optional[StrictStr] = Field(default=None, description="Estimated status")
    intent_to_quote: Optional[StrictBool] = Field(default=None, description="Intent to quote status")
    number: Optional[StrictStr] = Field(default=None, description="Number")
    original_quote: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Original quote")
    position: Optional[StrictInt] = Field(default=None, description="Position")
    private: Optional[StrictBool] = Field(default=None, description="If true, visible to admins only; otherwise visible to those with access to the parent contract.")
    prostore_file_ids: Optional[List[StrictInt]] = Field(default=None, description="Prostore File IDs")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    specification_section: Optional[RFQSpecificationSection] = None
    quotes: Optional[List[RFQQuote2]] = Field(default=None, description="Quotes")
    responses: Optional[List[RFQResponse2]] = Field(default=None, description="Responses")
    potential_change_orders: Optional[RFQPotentialChangeOrders] = None
    change_order_packages: Optional[RFQChangeOrderPackages] = None
    commitment_potential_change_orders: Optional[RFQPotentialChangeOrders] = None
    commitment_change_order_packages: Optional[RFQChangeOrderPackages] = None
    created_by: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    assigned: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    location: Optional[Location] = None
    cost_code: Optional[RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode] = None
    change_event: Optional[RFQChangeEvent] = None
    currency_configuration: Optional[RFQCurrencyConfiguration] = None
    __properties: ClassVar[List[str]] = ["id", "commitment_contract_id", "created_at", "deleted_at", "description", "due_date", "estimated_amount", "estimated_schedule_impact", "estimated_status", "intent_to_quote", "number", "original_quote", "position", "private", "prostore_file_ids", "status", "title", "updated_at", "specification_section", "quotes", "responses", "potential_change_orders", "change_order_packages", "commitment_potential_change_orders", "commitment_change_order_packages", "created_by", "assigned", "location", "cost_code", "change_event", "currency_configuration"]

    @field_validator('estimated_status')
    def estimated_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['rom', 'final']):
            raise ValueError("must be one of enum values ('rom', 'final')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['out_for_pricing', 'revise_and_resubmit', 'under_review', 'pending_final_approval', 'closed', 'withdrawn']):
            raise ValueError("must be one of enum values ('out_for_pricing', 'revise_and_resubmit', 'under_review', 'pending_final_approval', 'closed', 'withdrawn')")
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
        """Create an instance of RFQ from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of specification_section
        if self.specification_section:
            _dict['specification_section'] = self.specification_section.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in quotes (list)
        _items = []
        if self.quotes:
            for _item_quotes in self.quotes:
                if _item_quotes:
                    _items.append(_item_quotes.to_dict())
            _dict['quotes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in responses (list)
        _items = []
        if self.responses:
            for _item_responses in self.responses:
                if _item_responses:
                    _items.append(_item_responses.to_dict())
            _dict['responses'] = _items
        # override the default output from pydantic by calling `to_dict()` of potential_change_orders
        if self.potential_change_orders:
            _dict['potential_change_orders'] = self.potential_change_orders.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change_order_packages
        if self.change_order_packages:
            _dict['change_order_packages'] = self.change_order_packages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of commitment_potential_change_orders
        if self.commitment_potential_change_orders:
            _dict['commitment_potential_change_orders'] = self.commitment_potential_change_orders.to_dict()
        # override the default output from pydantic by calling `to_dict()` of commitment_change_order_packages
        if self.commitment_change_order_packages:
            _dict['commitment_change_order_packages'] = self.commitment_change_order_packages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assigned
        if self.assigned:
            _dict['assigned'] = self.assigned.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cost_code
        if self.cost_code:
            _dict['cost_code'] = self.cost_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change_event
        if self.change_event:
            _dict['change_event'] = self.change_event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_configuration
        if self.currency_configuration:
            _dict['currency_configuration'] = self.currency_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RFQ from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "commitment_contract_id": obj.get("commitment_contract_id"),
            "created_at": obj.get("created_at"),
            "deleted_at": obj.get("deleted_at"),
            "description": obj.get("description"),
            "due_date": obj.get("due_date"),
            "estimated_amount": obj.get("estimated_amount"),
            "estimated_schedule_impact": obj.get("estimated_schedule_impact"),
            "estimated_status": obj.get("estimated_status"),
            "intent_to_quote": obj.get("intent_to_quote"),
            "number": obj.get("number"),
            "original_quote": obj.get("original_quote"),
            "position": obj.get("position"),
            "private": obj.get("private"),
            "prostore_file_ids": obj.get("prostore_file_ids"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "updated_at": obj.get("updated_at"),
            "specification_section": RFQSpecificationSection.from_dict(obj["specification_section"]) if obj.get("specification_section") is not None else None,
            "quotes": [RFQQuote2.from_dict(_item) for _item in obj["quotes"]] if obj.get("quotes") is not None else None,
            "responses": [RFQResponse2.from_dict(_item) for _item in obj["responses"]] if obj.get("responses") is not None else None,
            "potential_change_orders": RFQPotentialChangeOrders.from_dict(obj["potential_change_orders"]) if obj.get("potential_change_orders") is not None else None,
            "change_order_packages": RFQChangeOrderPackages.from_dict(obj["change_order_packages"]) if obj.get("change_order_packages") is not None else None,
            "commitment_potential_change_orders": RFQPotentialChangeOrders.from_dict(obj["commitment_potential_change_orders"]) if obj.get("commitment_potential_change_orders") is not None else None,
            "commitment_change_order_packages": RFQChangeOrderPackages.from_dict(obj["commitment_change_order_packages"]) if obj.get("commitment_change_order_packages") is not None else None,
            "created_by": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "assigned": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["assigned"]) if obj.get("assigned") is not None else None,
            "location": Location.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "cost_code": RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.from_dict(obj["cost_code"]) if obj.get("cost_code") is not None else None,
            "change_event": RFQChangeEvent.from_dict(obj["change_event"]) if obj.get("change_event") is not None else None,
            "currency_configuration": RFQCurrencyConfiguration.from_dict(obj["currency_configuration"]) if obj.get("currency_configuration") is not None else None
        })
        return _obj


