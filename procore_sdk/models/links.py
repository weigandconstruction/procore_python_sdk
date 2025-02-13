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

class Links(BaseModel):
    """
    Links
    """ # noqa: E501
    var_self: Optional[StrictStr] = Field(default=None, description="A link back to the current resource", alias="self")
    update: Optional[StrictStr] = Field(default=None, description="A link to the update endpoint for the resource")
    delete: Optional[StrictStr] = Field(default=None, description="A link to the delete endpoint for the resource")
    permanently_delete: Optional[StrictStr] = Field(default=None, description="A link to the permanent delete endpoint for the resource", alias="permanentlyDelete")
    retrieve: Optional[StrictStr] = Field(default=None, description="A link to the retrive endpoint for the resource")
    __properties: ClassVar[List[str]] = ["self", "update", "delete", "permanentlyDelete", "retrieve"]

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
        """Create an instance of Links from a JSON string"""
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
        """Create an instance of Links from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "self": obj.get("self"),
            "update": obj.get("update"),
            "delete": obj.get("delete"),
            "permanentlyDelete": obj.get("permanentlyDelete"),
            "retrieve": obj.get("retrieve")
        })
        return _obj


