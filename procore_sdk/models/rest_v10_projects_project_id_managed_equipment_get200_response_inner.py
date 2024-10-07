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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.managed_equipment_category import ManagedEquipmentCategory
from procore_sdk.models.managed_equipment_make import ManagedEquipmentMake
from procore_sdk.models.managed_equipment_model import ManagedEquipmentModel
from procore_sdk.models.managed_equipment_type import ManagedEquipmentType
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner(BaseModel):
    """
    Managed Equipment
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID")
    name: Optional[StrictStr] = Field(default=None, description="The name of the install managed equipment")
    company_id: Optional[StrictInt] = Field(default=None, description="The Comapny ID the Managed Equipment was created with")
    current_project_id: Optional[StrictInt] = Field(default=None, description="Project ids the equipment is involved in")
    company_visible: Optional[StrictBool] = Field(default=None, description="Is the equipment visible as a company equipment")
    updated_at: Optional[datetime] = Field(default=None, description="Date the managed equipment was updated")
    created_at: Optional[datetime] = Field(default=None, description="Date the managed equipment was created")
    deleted_at: Optional[datetime] = Field(default=None, description="Date the managed equipment was deleted")
    serial_number: Optional[StrictStr] = Field(default=None, description="Serial number of the equipment")
    identification_number: Optional[StrictStr] = Field(default=None, description="Identification number of the equipment")
    description: Optional[StrictStr] = Field(default=None, description="description of the equipment")
    managed_equipment_make_id: Optional[StrictInt] = Field(default=None, description="ID of the equipment make")
    managed_equipment_model_id: Optional[StrictInt] = Field(default=None, description="ID of the equipment model")
    managed_equipment_type_id: Optional[StrictInt] = Field(default=None, description="ID of the equipment type")
    managed_equipment_category_id: Optional[StrictInt] = Field(default=None, description="ID of the equipment category")
    year: Optional[StrictInt] = Field(default=None, description="Year the equipment was manufactured in")
    status: Optional[StrictStr] = Field(default=None, description="Status")
    ownership: Optional[StrictStr] = Field(default=None, description="The type of ownership")
    created_by: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    managed_equipment_make: Optional[ManagedEquipmentMake] = None
    managed_equipment_model: Optional[ManagedEquipmentModel] = None
    managed_equipment_category: Optional[ManagedEquipmentCategory] = None
    managed_equipment_type: Optional[ManagedEquipmentType] = None
    __properties: ClassVar[List[str]] = ["id", "name", "company_id", "current_project_id", "company_visible", "updated_at", "created_at", "deleted_at", "serial_number", "identification_number", "description", "managed_equipment_make_id", "managed_equipment_model_id", "managed_equipment_type_id", "managed_equipment_category_id", "year", "status", "ownership", "created_by", "managed_equipment_make", "managed_equipment_model", "managed_equipment_category", "managed_equipment_type"]

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
        """Create an instance of RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of managed_equipment_make
        if self.managed_equipment_make:
            _dict['managed_equipment_make'] = self.managed_equipment_make.to_dict()
        # override the default output from pydantic by calling `to_dict()` of managed_equipment_model
        if self.managed_equipment_model:
            _dict['managed_equipment_model'] = self.managed_equipment_model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of managed_equipment_category
        if self.managed_equipment_category:
            _dict['managed_equipment_category'] = self.managed_equipment_category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of managed_equipment_type
        if self.managed_equipment_type:
            _dict['managed_equipment_type'] = self.managed_equipment_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "company_id": obj.get("company_id"),
            "current_project_id": obj.get("current_project_id"),
            "company_visible": obj.get("company_visible"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "deleted_at": obj.get("deleted_at"),
            "serial_number": obj.get("serial_number"),
            "identification_number": obj.get("identification_number"),
            "description": obj.get("description"),
            "managed_equipment_make_id": obj.get("managed_equipment_make_id"),
            "managed_equipment_model_id": obj.get("managed_equipment_model_id"),
            "managed_equipment_type_id": obj.get("managed_equipment_type_id"),
            "managed_equipment_category_id": obj.get("managed_equipment_category_id"),
            "year": obj.get("year"),
            "status": obj.get("status"),
            "ownership": obj.get("ownership"),
            "created_by": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "managed_equipment_make": ManagedEquipmentMake.from_dict(obj["managed_equipment_make"]) if obj.get("managed_equipment_make") is not None else None,
            "managed_equipment_model": ManagedEquipmentModel.from_dict(obj["managed_equipment_model"]) if obj.get("managed_equipment_model") is not None else None,
            "managed_equipment_category": ManagedEquipmentCategory.from_dict(obj["managed_equipment_category"]) if obj.get("managed_equipment_category") is not None else None,
            "managed_equipment_type": ManagedEquipmentType.from_dict(obj["managed_equipment_type"]) if obj.get("managed_equipment_type") is not None else None
        })
        return _obj


