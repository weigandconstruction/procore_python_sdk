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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class BudgetLineItem(BaseModel):
    """
    Budget Line Item object
    """ # noqa: E501
    wbs_code_id: StrictInt = Field(description="Work Breakdown Structure Code ID")
    original_budget_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Original Budget amount")
    uom: Optional[StrictStr] = Field(default=None, description="Unit of Measure")
    quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantity")
    unit_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Unit Cost")
    calculation_strategy: Optional[StrictStr] = Field(default=None, description="Calculation Strategy")
    __properties: ClassVar[List[str]] = ["wbs_code_id", "original_budget_amount", "uom", "quantity", "unit_cost", "calculation_strategy"]

    @field_validator('uom')
    def uom_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Any value present in the Company list of Units of Measure']):
            raise ValueError("must be one of enum values ('Any value present in the Company list of Units of Measure')")
        return value

    @field_validator('calculation_strategy')
    def calculation_strategy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['automatic', 'manual']):
            raise ValueError("must be one of enum values ('automatic', 'manual')")
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
        """Create an instance of BudgetLineItem from a JSON string"""
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
        """Create an instance of BudgetLineItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "wbs_code_id": obj.get("wbs_code_id"),
            "original_budget_amount": obj.get("original_budget_amount"),
            "uom": obj.get("uom"),
            "quantity": obj.get("quantity"),
            "unit_cost": obj.get("unit_cost"),
            "calculation_strategy": obj.get("calculation_strategy")
        })
        return _obj


