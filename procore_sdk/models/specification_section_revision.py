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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_custom_fields import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields
from typing import Optional, Set
from typing_extensions import Self

class SpecificationSectionRevision(BaseModel):
    """
    A version of a Specification Section. Each time a Specification Section is revised, the newly uploaded version is a new revision of that section.
    """ # noqa: E501
    id: Optional[StrictInt] = None
    specification_section_id: Optional[StrictInt] = None
    specification_section_division_id: Optional[StrictInt] = Field(default=None, description="Id of the Section Division")
    specification_set_id: Optional[StrictInt] = Field(default=None, description="Id of the Set")
    number: Optional[StrictStr] = Field(default=None, description="The number of this revision's SpecificationSection")
    description: Optional[StrictStr] = Field(default=None, description="The description of this revision's SpecificationSection")
    url: Optional[StrictStr] = Field(default=None, description="Address of SpecificationRevision PDF. This can be blank if the Specification Section was created manually without an upload, and no revisions have been uploaded yet.")
    revision: Optional[StrictStr] = Field(default=None, description="The revision number")
    issued_date: Optional[date] = Field(default=None, description="The date when the SpecificationRevision was issued by the architect")
    received_date: Optional[date] = Field(default=None, description="The date when the SpecificationRevision was received by the project")
    updated_at: Optional[StrictStr] = Field(default=None, description="Updated at")
    custom_fields: Optional[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields] = None
    __properties: ClassVar[List[str]] = ["id", "specification_section_id", "specification_section_division_id", "specification_set_id", "number", "description", "url", "revision", "issued_date", "received_date", "updated_at", "custom_fields"]

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
        """Create an instance of SpecificationSectionRevision from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_fields
        if self.custom_fields:
            _dict['custom_fields'] = self.custom_fields.to_dict()
        # set to None if specification_set_id (nullable) is None
        # and model_fields_set contains the field
        if self.specification_set_id is None and "specification_set_id" in self.model_fields_set:
            _dict['specification_set_id'] = None

        # set to None if issued_date (nullable) is None
        # and model_fields_set contains the field
        if self.issued_date is None and "issued_date" in self.model_fields_set:
            _dict['issued_date'] = None

        # set to None if received_date (nullable) is None
        # and model_fields_set contains the field
        if self.received_date is None and "received_date" in self.model_fields_set:
            _dict['received_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpecificationSectionRevision from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "specification_section_id": obj.get("specification_section_id"),
            "specification_section_division_id": obj.get("specification_section_division_id"),
            "specification_set_id": obj.get("specification_set_id"),
            "number": obj.get("number"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "revision": obj.get("revision"),
            "issued_date": obj.get("issued_date"),
            "received_date": obj.get("received_date"),
            "updated_at": obj.get("updated_at"),
            "custom_fields": RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.from_dict(obj["custom_fields"]) if obj.get("custom_fields") is not None else None
        })
        return _obj


