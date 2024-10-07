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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_change_order_packages_post201_response_line_items_inner_markup_line_items_inner_markup import RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkup
from procore_sdk.models.rest_v10_work_order_contracts_get200_response_inner_currency_configuration import RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration
from typing import Optional, Set
from typing_extensions import Self

class RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInner(BaseModel):
    """
    RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Markup Line Item ID")
    amount: Optional[StrictStr] = Field(default=None, description="Markup Line Item amount")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    markup: Optional[RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkup] = None
    currency_configuration: Optional[RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration] = None
    __properties: ClassVar[List[str]] = ["id", "amount", "created_at", "updated_at", "markup", "currency_configuration"]

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
        """Create an instance of RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of markup
        if self.markup:
            _dict['markup'] = self.markup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_configuration
        if self.currency_configuration:
            _dict['currency_configuration'] = self.currency_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "amount": obj.get("amount"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "markup": RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkup.from_dict(obj["markup"]) if obj.get("markup") is not None else None,
            "currency_configuration": RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.from_dict(obj["currency_configuration"]) if obj.get("currency_configuration") is not None else None
        })
        return _obj


