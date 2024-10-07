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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RequisitionBulkItemUpdateInner(BaseModel):
    """
    RequisitionBulkItemUpdateInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The id of the item to update")
    item_type: Optional[StrictStr] = Field(default=None, description="The type of the item your are updating")
    work_completed_this_period: Optional[StrictStr] = Field(default=None, description="The amount of work completed this period")
    materials_presently_stored: Optional[StrictStr] = Field(default=None, description="The amount of materials presently stored")
    work_completed_retainage_retained_this_period: Optional[StrictStr] = Field(default=None, description="Work completed retainage amount retained this period (admin user only, work_completed_this_period should be non-zero to hold a retainage)")
    materials_stored_retainage_currently_retained: Optional[StrictStr] = Field(default=None, description="Materials stored retainage amount currently retained (admin user, amount accounting only, materials_presently_stored should be non-zero to hold a retainage)")
    work_completed_retainage_released_this_period: Optional[StrictStr] = Field(default=None, description="The amount of work completed retainage released this period")
    work_completed_this_period_quantity: Optional[StrictStr] = Field(default=None, description="Work completed this period quantity (unit accounting contract only)")
    subcontractor_claimed_amount: Optional[StrictStr] = Field(default=None, description="The total amount the subcontractor original claimed for this line")
    status: Optional[StrictStr] = Field(default=None, description="Approval status of the invoice line item")
    comment: Optional[StrictStr] = Field(default=None, description="Comment about the invoice line item")
    __properties: ClassVar[List[str]] = ["id", "item_type", "work_completed_this_period", "materials_presently_stored", "work_completed_retainage_retained_this_period", "materials_stored_retainage_currently_retained", "work_completed_retainage_released_this_period", "work_completed_this_period_quantity", "subcontractor_claimed_amount", "status", "comment"]

    @field_validator('item_type')
    def item_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['contract_item', 'contract_detail_item', 'change_order_item']):
            raise ValueError("must be one of enum values ('contract_item', 'contract_detail_item', 'change_order_item')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['approved', 'rejected', 'no_action']):
            raise ValueError("must be one of enum values ('approved', 'rejected', 'no_action')")
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
        """Create an instance of RequisitionBulkItemUpdateInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RequisitionBulkItemUpdateInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "item_type": obj.get("item_type"),
            "work_completed_this_period": obj.get("work_completed_this_period"),
            "materials_presently_stored": obj.get("materials_presently_stored"),
            "work_completed_retainage_retained_this_period": obj.get("work_completed_retainage_retained_this_period"),
            "materials_stored_retainage_currently_retained": obj.get("materials_stored_retainage_currently_retained"),
            "work_completed_retainage_released_this_period": obj.get("work_completed_retainage_released_this_period"),
            "work_completed_this_period_quantity": obj.get("work_completed_this_period_quantity"),
            "subcontractor_claimed_amount": obj.get("subcontractor_claimed_amount"),
            "status": obj.get("status"),
            "comment": obj.get("comment")
        })
        return _obj


