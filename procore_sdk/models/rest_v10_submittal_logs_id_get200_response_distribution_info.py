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
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_attachments_inner import RestV10WorkOrderContractsPost201ResponseAttachmentsInner
from typing import Optional, Set
from typing_extensions import Self

class RestV10SubmittalLogsIdGet200ResponseDistributionInfo(BaseModel):
    """
    RestV10SubmittalLogsIdGet200ResponseDistributionInfo
    """ # noqa: E501
    id: Optional[StrictInt] = None
    message: Optional[StrictStr] = None
    distributed_date: Optional[datetime] = None
    distributed_by: Optional[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] = None
    distributed_to: Optional[List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]] = None
    final_attachments: Optional[List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]] = None
    __properties: ClassVar[List[str]] = ["id", "message", "distributed_date", "distributed_by", "distributed_to", "final_attachments"]

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
        """Create an instance of RestV10SubmittalLogsIdGet200ResponseDistributionInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of distributed_by
        if self.distributed_by:
            _dict['distributed_by'] = self.distributed_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in distributed_to (list)
        _items = []
        if self.distributed_to:
            for _item_distributed_to in self.distributed_to:
                if _item_distributed_to:
                    _items.append(_item_distributed_to.to_dict())
            _dict['distributed_to'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in final_attachments (list)
        _items = []
        if self.final_attachments:
            for _item_final_attachments in self.final_attachments:
                if _item_final_attachments:
                    _items.append(_item_final_attachments.to_dict())
            _dict['final_attachments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10SubmittalLogsIdGet200ResponseDistributionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "message": obj.get("message"),
            "distributed_date": obj.get("distributed_date"),
            "distributed_by": RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(obj["distributed_by"]) if obj.get("distributed_by") is not None else None,
            "distributed_to": [RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(_item) for _item in obj["distributed_to"]] if obj.get("distributed_to") is not None else None,
            "final_attachments": [RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(_item) for _item in obj["final_attachments"]] if obj.get("final_attachments") is not None else None
        })
        return _obj


