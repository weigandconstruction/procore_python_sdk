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
from procore_sdk.models.rest_v10_requisitions_requisition_id_add_change_order_package_post201_response_inner_currency_configuration import RestV10RequisitionsRequisitionIdAddChangeOrderPackagePost201ResponseInnerCurrencyConfiguration
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_wbs_code import RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode
from typing import Optional, Set
from typing_extensions import Self

class RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response(BaseModel):
    """
    Requisition (Subcontractor Invoice) Whole Change Order Item
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID of the Whole Change Order Item")
    cost_code_id: Optional[StrictInt] = Field(default=None, description="Cost Code ID")
    item_type: Optional[StrictStr] = Field(default=None, description="Item type")
    line_item_id: Optional[StrictInt] = Field(default=None, description="Line Item ID")
    description_of_work: Optional[StrictStr] = Field(default=None, description="Description of work")
    scheduled_value: Optional[StrictStr] = Field(default=None, description="Scheduled value amount")
    work_completed_from_previous_application: Optional[StrictStr] = Field(default=None, description="Work completed from previous application amount")
    work_completed_this_period: Optional[StrictStr] = Field(default=None, description="Work completed this period amount")
    materials_presently_stored: Optional[StrictStr] = Field(default=None, description="Materials presently stored amount")
    total_completed_and_stored_to_date: Optional[StrictStr] = Field(default=None, description="Total completed and stored to date amount")
    total_completed_and_stored_to_date_percent: Optional[StrictStr] = Field(default=None, description="Total completed and stored to date percent")
    work_completed_retainage_from_previous_application: Optional[StrictStr] = Field(default=None, description="Work completed retainage amount from previous application")
    work_completed_retainage_retained_this_period: Optional[StrictStr] = Field(default=None, description="Work completed retainage amount retained this period")
    work_completed_retainage_percent_this_period: Optional[StrictStr] = Field(default=None, description="Work completed retainage percent this period")
    ssr_manual_override: Optional[StrictBool] = Field(default=None, description="SSR manual override")
    materials_stored_retainage_currently_retained: Optional[StrictStr] = Field(default=None, description="Materials stored retainage amount currently retained")
    materials_stored_retainage_percent_this_period: Optional[StrictStr] = Field(default=None, description="Materials stored retainage percent this period")
    work_completed_retainage_released_this_period: Optional[StrictStr] = Field(default=None, description="Work completed retainage amount released this period")
    materials_stored_retainage_released_this_period: Optional[StrictStr] = Field(default=None, description="Materials stored retainage amount released this period")
    scheduled_quantity: Optional[StrictStr] = Field(default=None, description="Scheduled quantity")
    scheduled_unit_price: Optional[StrictStr] = Field(default=None, description="Scheduled unit price")
    work_completed_this_period_quantity: Optional[StrictStr] = Field(default=None, description="Work completed this period quantity")
    work_completed_from_previous_application_quantity: Optional[StrictStr] = Field(default=None, description="Work completed from previous application quantity")
    change_order_package_id: Optional[StrictInt] = Field(default=None, description="ID for Change Order Package")
    subcontractor_claimed_amount: Optional[StrictStr] = Field(default=None, description="Amount claimed by the subcontractor")
    comment: Optional[StrictStr] = Field(default=None, description="Comment for the Whole Change Order Item")
    status: Optional[StrictStr] = Field(default=None, description="Status of the Whole Change Order Item")
    wbs_code: Optional[RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode] = None
    position: Optional[StrictInt] = Field(default=None, description="Position")
    currency_configuration: Optional[RestV10RequisitionsRequisitionIdAddChangeOrderPackagePost201ResponseInnerCurrencyConfiguration] = None
    materials_moved: Optional[StrictStr] = Field(default=None, description="Materials automatically moved from previous line item into previous work completed. This will be non-zero only if move_materials_to_previous_work_completed is true on the payment application.")
    materials_retainage_retained_moved: Optional[StrictStr] = Field(default=None, description="Retainage on materials automatically moved from previous line item into work completed retainage amount accrued previously. This will be non-zero only if move_materials_to_previous_work_completed is true on the payment application.")
    __properties: ClassVar[List[str]] = ["id", "cost_code_id", "item_type", "line_item_id", "description_of_work", "scheduled_value", "work_completed_from_previous_application", "work_completed_this_period", "materials_presently_stored", "total_completed_and_stored_to_date", "total_completed_and_stored_to_date_percent", "work_completed_retainage_from_previous_application", "work_completed_retainage_retained_this_period", "work_completed_retainage_percent_this_period", "ssr_manual_override", "materials_stored_retainage_currently_retained", "materials_stored_retainage_percent_this_period", "work_completed_retainage_released_this_period", "materials_stored_retainage_released_this_period", "scheduled_quantity", "scheduled_unit_price", "work_completed_this_period_quantity", "work_completed_from_previous_application_quantity", "change_order_package_id", "subcontractor_claimed_amount", "comment", "status", "wbs_code", "position", "currency_configuration", "materials_moved", "materials_retainage_retained_moved"]

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
        """Create an instance of RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of wbs_code
        if self.wbs_code:
            _dict['wbs_code'] = self.wbs_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_configuration
        if self.currency_configuration:
            _dict['currency_configuration'] = self.currency_configuration.to_dict()
        # set to None if cost_code_id (nullable) is None
        # and model_fields_set contains the field
        if self.cost_code_id is None and "cost_code_id" in self.model_fields_set:
            _dict['cost_code_id'] = None

        # set to None if description_of_work (nullable) is None
        # and model_fields_set contains the field
        if self.description_of_work is None and "description_of_work" in self.model_fields_set:
            _dict['description_of_work'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "cost_code_id": obj.get("cost_code_id"),
            "item_type": obj.get("item_type"),
            "line_item_id": obj.get("line_item_id"),
            "description_of_work": obj.get("description_of_work"),
            "scheduled_value": obj.get("scheduled_value"),
            "work_completed_from_previous_application": obj.get("work_completed_from_previous_application"),
            "work_completed_this_period": obj.get("work_completed_this_period"),
            "materials_presently_stored": obj.get("materials_presently_stored"),
            "total_completed_and_stored_to_date": obj.get("total_completed_and_stored_to_date"),
            "total_completed_and_stored_to_date_percent": obj.get("total_completed_and_stored_to_date_percent"),
            "work_completed_retainage_from_previous_application": obj.get("work_completed_retainage_from_previous_application"),
            "work_completed_retainage_retained_this_period": obj.get("work_completed_retainage_retained_this_period"),
            "work_completed_retainage_percent_this_period": obj.get("work_completed_retainage_percent_this_period"),
            "ssr_manual_override": obj.get("ssr_manual_override"),
            "materials_stored_retainage_currently_retained": obj.get("materials_stored_retainage_currently_retained"),
            "materials_stored_retainage_percent_this_period": obj.get("materials_stored_retainage_percent_this_period"),
            "work_completed_retainage_released_this_period": obj.get("work_completed_retainage_released_this_period"),
            "materials_stored_retainage_released_this_period": obj.get("materials_stored_retainage_released_this_period"),
            "scheduled_quantity": obj.get("scheduled_quantity"),
            "scheduled_unit_price": obj.get("scheduled_unit_price"),
            "work_completed_this_period_quantity": obj.get("work_completed_this_period_quantity"),
            "work_completed_from_previous_application_quantity": obj.get("work_completed_from_previous_application_quantity"),
            "change_order_package_id": obj.get("change_order_package_id"),
            "subcontractor_claimed_amount": obj.get("subcontractor_claimed_amount"),
            "comment": obj.get("comment"),
            "status": obj.get("status"),
            "wbs_code": RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode.from_dict(obj["wbs_code"]) if obj.get("wbs_code") is not None else None,
            "position": obj.get("position"),
            "currency_configuration": RestV10RequisitionsRequisitionIdAddChangeOrderPackagePost201ResponseInnerCurrencyConfiguration.from_dict(obj["currency_configuration"]) if obj.get("currency_configuration") is not None else None,
            "materials_moved": obj.get("materials_moved"),
            "materials_retainage_retained_moved": obj.get("materials_retainage_retained_moved")
        })
        return _obj


