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
from procore_sdk.models.default1_change_order_change_reason import Default1ChangeOrderChangeReason
from procore_sdk.models.default1_created_by import Default1CreatedBy
from procore_sdk.models.default1_designated_reviewer import Default1DesignatedReviewer
from procore_sdk.models.default1_received_from import Default1ReceivedFrom
from procore_sdk.models.default1_reviewed_by import Default1ReviewedBy
from procore_sdk.models.extended3_change_events_inner import Extended3ChangeEventsInner
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get200_response_inner_custom_fields import RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields
from procore_sdk.models.rest_v10_work_order_contracts_get200_response_inner_currency_configuration import RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration
from typing import Optional, Set
from typing_extensions import Self

class Extended3(BaseModel):
    """
    Base Prime Change Order Extended View
    """ # noqa: E501
    change_events: Optional[List[Extended3ChangeEventsInner]] = Field(default=None, description="Change Events linked")
    id: Optional[StrictInt] = Field(default=None, description="Prime Change Order ID")
    batch_id: Optional[StrictInt] = Field(default=None, description="Batch ID")
    contract_id: Optional[StrictInt] = Field(default=None, description="Contract ID")
    legacy_package_id: Optional[StrictInt] = Field(default=None, description="Legacy Package ID")
    legacy_request_id: Optional[StrictInt] = Field(default=None, description="Legacy Request ID")
    location_id: Optional[StrictInt] = Field(default=None, description="Location ID")
    description: Optional[StrictStr] = Field(default=None, description="Description of the Prime Change Order")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    invoiced_date: Optional[date] = Field(default=None, description="Invoiced date")
    paid_date: Optional[date] = Field(default=None, description="Paid date")
    due_date: Optional[date] = Field(default=None, description="Due date")
    revised_substantial_completion_date: Optional[date] = Field(default=None, description="Revised substantial completion date")
    signed_change_order_received_date: Optional[date] = Field(default=None, description="Signed change order received date")
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    reviewed_at: Optional[datetime] = Field(default=None, description="Approved date")
    executed: Optional[StrictBool] = Field(default=None, description="Whether or not the Prime Change Order is executed")
    paid: Optional[StrictBool] = Field(default=None, description="Whether or not the Prime Change Order is paid")
    signature_required: Optional[StrictBool] = Field(default=None, description="Whether or not a signature is required on the Prime Change Order")
    private: Optional[StrictBool] = Field(default=None, description="Only show this Contract to Admins and specific Accessors")
    field_change: Optional[StrictBool] = Field(default=None, description="Field change")
    grand_total: Optional[StrictStr] = Field(default=None, description="Total including markup")
    schedule_impact_amount: Optional[StrictInt] = Field(default=None, description="Schedule impact in days")
    number: Optional[StrictStr] = Field(default=None, description="Number")
    type: Optional[StrictStr] = Field(default=None, description="Type")
    revision: Optional[StrictInt] = Field(default=None, description="Revision number")
    status: Optional[StrictStr] = Field(default=None, description="The status of the Prime Change Order")
    reference: Optional[StrictStr] = Field(default=None, description="Reference")
    created_by: Optional[Default1CreatedBy] = None
    designated_reviewer: Optional[Default1DesignatedReviewer] = None
    received_from: Optional[Default1ReceivedFrom] = None
    reviewed_by: Optional[Default1ReviewedBy] = None
    change_order_change_reason: Optional[Default1ChangeOrderChangeReason] = None
    custom_fields: Optional[RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields] = None
    currency_configuration: Optional[RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration] = None
    __properties: ClassVar[List[str]] = ["change_events", "id", "batch_id", "contract_id", "legacy_package_id", "legacy_request_id", "location_id", "description", "title", "invoiced_date", "paid_date", "due_date", "revised_substantial_completion_date", "signed_change_order_received_date", "updated_at", "created_at", "reviewed_at", "executed", "paid", "signature_required", "private", "field_change", "grand_total", "schedule_impact_amount", "number", "type", "revision", "status", "reference", "created_by", "designated_reviewer", "received_from", "reviewed_by", "change_order_change_reason", "custom_fields", "currency_configuration"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PrimeChangeOrder']):
            raise ValueError("must be one of enum values ('PrimeChangeOrder')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['draft', 'pricing', 'not_pricing', 'pending', 'revised', 'proceeding', 'not_proceeding', 'pending_billable', 'no_charge', 'approved', 'rejected', 'void']):
            raise ValueError("must be one of enum values ('draft', 'pricing', 'not_pricing', 'pending', 'revised', 'proceeding', 'not_proceeding', 'pending_billable', 'no_charge', 'approved', 'rejected', 'void')")
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
        """Create an instance of Extended3 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in change_events (list)
        _items = []
        if self.change_events:
            for _item_change_events in self.change_events:
                if _item_change_events:
                    _items.append(_item_change_events.to_dict())
            _dict['change_events'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of designated_reviewer
        if self.designated_reviewer:
            _dict['designated_reviewer'] = self.designated_reviewer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of received_from
        if self.received_from:
            _dict['received_from'] = self.received_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reviewed_by
        if self.reviewed_by:
            _dict['reviewed_by'] = self.reviewed_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change_order_change_reason
        if self.change_order_change_reason:
            _dict['change_order_change_reason'] = self.change_order_change_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_fields
        if self.custom_fields:
            _dict['custom_fields'] = self.custom_fields.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_configuration
        if self.currency_configuration:
            _dict['currency_configuration'] = self.currency_configuration.to_dict()
        # set to None if batch_id (nullable) is None
        # and model_fields_set contains the field
        if self.batch_id is None and "batch_id" in self.model_fields_set:
            _dict['batch_id'] = None

        # set to None if legacy_package_id (nullable) is None
        # and model_fields_set contains the field
        if self.legacy_package_id is None and "legacy_package_id" in self.model_fields_set:
            _dict['legacy_package_id'] = None

        # set to None if legacy_request_id (nullable) is None
        # and model_fields_set contains the field
        if self.legacy_request_id is None and "legacy_request_id" in self.model_fields_set:
            _dict['legacy_request_id'] = None

        # set to None if location_id (nullable) is None
        # and model_fields_set contains the field
        if self.location_id is None and "location_id" in self.model_fields_set:
            _dict['location_id'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if invoiced_date (nullable) is None
        # and model_fields_set contains the field
        if self.invoiced_date is None and "invoiced_date" in self.model_fields_set:
            _dict['invoiced_date'] = None

        # set to None if paid_date (nullable) is None
        # and model_fields_set contains the field
        if self.paid_date is None and "paid_date" in self.model_fields_set:
            _dict['paid_date'] = None

        # set to None if due_date (nullable) is None
        # and model_fields_set contains the field
        if self.due_date is None and "due_date" in self.model_fields_set:
            _dict['due_date'] = None

        # set to None if revised_substantial_completion_date (nullable) is None
        # and model_fields_set contains the field
        if self.revised_substantial_completion_date is None and "revised_substantial_completion_date" in self.model_fields_set:
            _dict['revised_substantial_completion_date'] = None

        # set to None if signed_change_order_received_date (nullable) is None
        # and model_fields_set contains the field
        if self.signed_change_order_received_date is None and "signed_change_order_received_date" in self.model_fields_set:
            _dict['signed_change_order_received_date'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if reviewed_at (nullable) is None
        # and model_fields_set contains the field
        if self.reviewed_at is None and "reviewed_at" in self.model_fields_set:
            _dict['reviewed_at'] = None

        # set to None if schedule_impact_amount (nullable) is None
        # and model_fields_set contains the field
        if self.schedule_impact_amount is None and "schedule_impact_amount" in self.model_fields_set:
            _dict['schedule_impact_amount'] = None

        # set to None if number (nullable) is None
        # and model_fields_set contains the field
        if self.number is None and "number" in self.model_fields_set:
            _dict['number'] = None

        # set to None if revision (nullable) is None
        # and model_fields_set contains the field
        if self.revision is None and "revision" in self.model_fields_set:
            _dict['revision'] = None

        # set to None if reference (nullable) is None
        # and model_fields_set contains the field
        if self.reference is None and "reference" in self.model_fields_set:
            _dict['reference'] = None

        # set to None if designated_reviewer (nullable) is None
        # and model_fields_set contains the field
        if self.designated_reviewer is None and "designated_reviewer" in self.model_fields_set:
            _dict['designated_reviewer'] = None

        # set to None if received_from (nullable) is None
        # and model_fields_set contains the field
        if self.received_from is None and "received_from" in self.model_fields_set:
            _dict['received_from'] = None

        # set to None if reviewed_by (nullable) is None
        # and model_fields_set contains the field
        if self.reviewed_by is None and "reviewed_by" in self.model_fields_set:
            _dict['reviewed_by'] = None

        # set to None if change_order_change_reason (nullable) is None
        # and model_fields_set contains the field
        if self.change_order_change_reason is None and "change_order_change_reason" in self.model_fields_set:
            _dict['change_order_change_reason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Extended3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "change_events": [Extended3ChangeEventsInner.from_dict(_item) for _item in obj["change_events"]] if obj.get("change_events") is not None else None,
            "id": obj.get("id"),
            "batch_id": obj.get("batch_id"),
            "contract_id": obj.get("contract_id"),
            "legacy_package_id": obj.get("legacy_package_id"),
            "legacy_request_id": obj.get("legacy_request_id"),
            "location_id": obj.get("location_id"),
            "description": obj.get("description"),
            "title": obj.get("title"),
            "invoiced_date": obj.get("invoiced_date"),
            "paid_date": obj.get("paid_date"),
            "due_date": obj.get("due_date"),
            "revised_substantial_completion_date": obj.get("revised_substantial_completion_date"),
            "signed_change_order_received_date": obj.get("signed_change_order_received_date"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "reviewed_at": obj.get("reviewed_at"),
            "executed": obj.get("executed"),
            "paid": obj.get("paid"),
            "signature_required": obj.get("signature_required"),
            "private": obj.get("private"),
            "field_change": obj.get("field_change"),
            "grand_total": obj.get("grand_total"),
            "schedule_impact_amount": obj.get("schedule_impact_amount"),
            "number": obj.get("number"),
            "type": obj.get("type"),
            "revision": obj.get("revision"),
            "status": obj.get("status"),
            "reference": obj.get("reference"),
            "created_by": Default1CreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "designated_reviewer": Default1DesignatedReviewer.from_dict(obj["designated_reviewer"]) if obj.get("designated_reviewer") is not None else None,
            "received_from": Default1ReceivedFrom.from_dict(obj["received_from"]) if obj.get("received_from") is not None else None,
            "reviewed_by": Default1ReviewedBy.from_dict(obj["reviewed_by"]) if obj.get("reviewed_by") is not None else None,
            "change_order_change_reason": Default1ChangeOrderChangeReason.from_dict(obj["change_order_change_reason"]) if obj.get("change_order_change_reason") is not None else None,
            "custom_fields": RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.from_dict(obj["custom_fields"]) if obj.get("custom_fields") is not None else None,
            "currency_configuration": RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.from_dict(obj["currency_configuration"]) if obj.get("currency_configuration") is not None else None
        })
        return _obj


