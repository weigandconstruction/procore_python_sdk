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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequestInvoiceConfiguration(BaseModel):
    """
    Invoice Configuration for the Contract
    """ # noqa: E501
    separate_billing_for_stored_materials: Optional[StrictBool] = Field(default=None, description="Whether billing for materials separately from the work complete is allowed")
    stored_materials_billing_method: Optional[StrictStr] = Field(default=None, description="Billing method for stored materials")
    __properties: ClassVar[List[str]] = ["separate_billing_for_stored_materials", "stored_materials_billing_method"]

    @field_validator('stored_materials_billing_method')
    def stored_materials_billing_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['move_new_materials']):
            raise ValueError("must be one of enum values ('move_new_materials')")
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
        """Create an instance of RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequestInvoiceConfiguration from a JSON string"""
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
        """Create an instance of RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequestInvoiceConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "separate_billing_for_stored_materials": obj.get("separate_billing_for_stored_materials"),
            "stored_materials_billing_method": obj.get("stored_materials_billing_method")
        })
        return _obj


