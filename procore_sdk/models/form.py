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
from typing import Optional, Set
from typing_extensions import Self

class Form(BaseModel):
    """
    Form
    """ # noqa: E501
    name: StrictStr = Field(description="The Name of the Form")
    description: StrictStr = Field(description="The Description of the Form")
    form_template_id: StrictInt = Field(description="ID of the Form Template that the Form is made from")
    private: Optional[StrictBool] = Field(default=False, description="The Private status of the Form")
    fillable_pdf_prostore_file_id: StrictInt = Field(description="Form's Fillable PDF")
    prostore_file_ids: Optional[List[StrictInt]] = Field(default=None, description="An array of Prostore File IDs. The Prostore Files will be associated with the Form as attachments")
    __properties: ClassVar[List[str]] = ["name", "description", "form_template_id", "private", "fillable_pdf_prostore_file_id", "prostore_file_ids"]

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
        """Create an instance of Form from a JSON string"""
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
        """Create an instance of Form from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "form_template_id": obj.get("form_template_id"),
            "private": obj.get("private") if obj.get("private") is not None else False,
            "fillable_pdf_prostore_file_id": obj.get("fillable_pdf_prostore_file_id"),
            "prostore_file_ids": obj.get("prostore_file_ids")
        })
        return _obj


