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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from procore_sdk.models.work_order_contract_custom_field_custom_field_definition_id import WorkOrderContractCustomFieldCustomFieldDefinitionId
from typing import Optional, Set
from typing_extensions import Self

class IncidentPropertyDamageCreateParameters(BaseModel):
    """
    IncidentPropertyDamageCreateParameters
    """ # noqa: E501
    incident_id: StrictInt = Field(description="The ID of the Incident")
    description: Optional[StrictStr] = Field(default=None, description="Description of event in Rich Text format")
    estimated_cost_impact: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Estimated cost impact of the record")
    affected_company_id: Optional[StrictInt] = Field(default=None, description="The ID of the Affected Company")
    responsible_company_id: Optional[StrictInt] = Field(default=None, description="The ID of the Responsible Company")
    managed_equipment_id: Optional[StrictInt] = Field(default=None, description="The ID of the Managed Equipment")
    work_activity_id: Optional[StrictInt] = Field(default=None, description="The ID of the Work Activity")
    custom_field_custom_field_definition_id: Optional[WorkOrderContractCustomFieldCustomFieldDefinitionId] = Field(default=None, alias="custom_field_%{custom_field_definition_id}")
    __properties: ClassVar[List[str]] = ["incident_id", "description", "estimated_cost_impact", "affected_company_id", "responsible_company_id", "managed_equipment_id", "work_activity_id", "custom_field_%{custom_field_definition_id}"]

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
        """Create an instance of IncidentPropertyDamageCreateParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_field_custom_field_definition_id
        if self.custom_field_custom_field_definition_id:
            _dict['custom_field_%{custom_field_definition_id}'] = self.custom_field_custom_field_definition_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IncidentPropertyDamageCreateParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "incident_id": obj.get("incident_id"),
            "description": obj.get("description"),
            "estimated_cost_impact": obj.get("estimated_cost_impact"),
            "affected_company_id": obj.get("affected_company_id"),
            "responsible_company_id": obj.get("responsible_company_id"),
            "managed_equipment_id": obj.get("managed_equipment_id"),
            "work_activity_id": obj.get("work_activity_id"),
            "custom_field_%{custom_field_definition_id}": WorkOrderContractCustomFieldCustomFieldDefinitionId.from_dict(obj["custom_field_%{custom_field_definition_id}"]) if obj.get("custom_field_%{custom_field_definition_id}") is not None else None
        })
        return _obj


