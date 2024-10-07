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
from procore_sdk.models.action_type import ActionType
from procore_sdk.models.incident_attachment import IncidentAttachment
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_custom_fields import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields
from typing import Optional, Set
from typing_extensions import Self

class RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner(BaseModel):
    """
    RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Action ID")
    incident_id: Optional[StrictInt] = Field(default=None, description="Incident ID")
    action_type: Optional[ActionType] = None
    attachments: Optional[List[IncidentAttachment]] = None
    description: Optional[StrictStr] = Field(default=None, description="The account of the action in rich text form.")
    description_plain_text: Optional[StrictStr] = Field(default=None, description="The account of the action plain text form.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp of creation")
    deleted_at: Optional[datetime] = Field(default=None, description="Timestamp of deletion")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp of last update")
    observation_id: Optional[StrictInt] = Field(default=None, description="Observation ID")
    custom_fields: Optional[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields] = None
    __properties: ClassVar[List[str]] = ["id", "incident_id", "action_type", "attachments", "description", "description_plain_text", "created_at", "deleted_at", "updated_at", "observation_id", "custom_fields"]

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
        """Create an instance of RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of action_type
        if self.action_type:
            _dict['action_type'] = self.action_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of custom_fields
        if self.custom_fields:
            _dict['custom_fields'] = self.custom_fields.to_dict()
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deleted_at'] = None

        # set to None if observation_id (nullable) is None
        # and model_fields_set contains the field
        if self.observation_id is None and "observation_id" in self.model_fields_set:
            _dict['observation_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "incident_id": obj.get("incident_id"),
            "action_type": ActionType.from_dict(obj["action_type"]) if obj.get("action_type") is not None else None,
            "attachments": [IncidentAttachment.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "description": obj.get("description"),
            "description_plain_text": obj.get("description_plain_text"),
            "created_at": obj.get("created_at"),
            "deleted_at": obj.get("deleted_at"),
            "updated_at": obj.get("updated_at"),
            "observation_id": obj.get("observation_id"),
            "custom_fields": RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.from_dict(obj["custom_fields"]) if obj.get("custom_fields") is not None else None
        })
        return _obj


