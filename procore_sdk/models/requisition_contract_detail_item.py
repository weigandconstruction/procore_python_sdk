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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RequisitionContractDetailItem(BaseModel):
    """
    Requisition (Subcontractor Invoice) Contract Detail Item
    """ # noqa: E501
    work_completed_this_period: Optional[StrictStr] = Field(default=None, description="The amount of work completed this period")
    materials_presently_stored: Optional[StrictStr] = Field(default=None, description="The amount of materials presently stored")
    work_completed_retainage_retained_this_period: Optional[StrictStr] = Field(default=None, description="Work completed retainage amount retained this period (admin user only, work_completed_this_period should be non-zero to hold a retainage)")
    materials_stored_retainage_currently_retained: Optional[StrictStr] = Field(default=None, description="Materials stored retainage amount currently retained (admin user, amount accounting only, materials_presently_stored should be non-zero to hold a retainage)")
    work_completed_retainage_released_this_period: Optional[StrictStr] = Field(default=None, description="The amount of work completed retainage released this period")
    work_completed_this_period_quantity: Optional[StrictStr] = Field(default=None, description="Work completed this period quantity (unit accounting contract only)")
    __properties: ClassVar[List[str]] = ["work_completed_this_period", "materials_presently_stored", "work_completed_retainage_retained_this_period", "materials_stored_retainage_currently_retained", "work_completed_retainage_released_this_period", "work_completed_this_period_quantity"]

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
        """Create an instance of RequisitionContractDetailItem from a JSON string"""
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
        """Create an instance of RequisitionContractDetailItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "work_completed_this_period": obj.get("work_completed_this_period"),
            "materials_presently_stored": obj.get("materials_presently_stored"),
            "work_completed_retainage_retained_this_period": obj.get("work_completed_retainage_retained_this_period"),
            "materials_stored_retainage_currently_retained": obj.get("materials_stored_retainage_currently_retained"),
            "work_completed_retainage_released_this_period": obj.get("work_completed_retainage_released_this_period"),
            "work_completed_this_period_quantity": obj.get("work_completed_this_period_quantity")
        })
        return _obj


