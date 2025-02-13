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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.location import Location
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
from procore_sdk.models.rest_v10_submittal_logs_get200_response_inner_specification_section import RestV10SubmittalLogsGet200ResponseInnerSpecificationSection
from procore_sdk.models.rest_v10_submittal_logs_id_get200_response_approvers_inner import RestV10SubmittalLogsIdGet200ResponseApproversInner
from procore_sdk.models.rest_v10_submittal_logs_id_get200_response_created_by import RestV10SubmittalLogsIdGet200ResponseCreatedBy
from procore_sdk.models.rest_v10_submittal_logs_id_get200_response_distribution_info import RestV10SubmittalLogsIdGet200ResponseDistributionInfo
from procore_sdk.models.rest_v10_submittal_logs_id_get200_response_received_from import RestV10SubmittalLogsIdGet200ResponseReceivedFrom
from procore_sdk.models.rest_v10_submittal_logs_id_get200_response_submittal_package import RestV10SubmittalLogsIdGet200ResponseSubmittalPackage
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_attachments_inner import RestV10WorkOrderContractsPost201ResponseAttachmentsInner
from typing import Optional, Set
from typing_extensions import Self

class RestV10SubmittalLogsIdGet200Response(BaseModel):
    """
    RestV10SubmittalLogsIdGet200Response
    """ # noqa: E501
    id: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    number: Optional[StrictStr] = None
    formatted_number: Optional[StrictStr] = None
    revision: Optional[StrictStr] = None
    private: Optional[StrictBool] = None
    received_date: Optional[date] = None
    issue_date: Optional[date] = None
    submit_by: Optional[date] = None
    due_date: Optional[date] = None
    type: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    closed: Optional[StrictBool] = None
    created_by: Optional[RestV10SubmittalLogsIdGet200ResponseCreatedBy] = None
    received_from: Optional[RestV10SubmittalLogsIdGet200ResponseReceivedFrom] = None
    approvers: Optional[List[RestV10SubmittalLogsIdGet200ResponseApproversInner]] = None
    distribution_members: Optional[List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]] = None
    ball_in_court: Optional[List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]] = None
    location: Optional[Location] = None
    specification_section: Optional[RestV10SubmittalLogsGet200ResponseInnerSpecificationSection] = None
    attachments: Optional[List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]] = None
    distribution_info: Optional[RestV10SubmittalLogsIdGet200ResponseDistributionInfo] = None
    submittal_package: Optional[RestV10SubmittalLogsIdGet200ResponseSubmittalPackage] = None
    __properties: ClassVar[List[str]] = ["id", "title", "number", "formatted_number", "revision", "private", "received_date", "issue_date", "submit_by", "due_date", "type", "description", "status", "closed", "created_by", "received_from", "approvers", "distribution_members", "ball_in_court", "location", "specification_section", "attachments", "distribution_info", "submittal_package"]

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
        """Create an instance of RestV10SubmittalLogsIdGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of received_from
        if self.received_from:
            _dict['received_from'] = self.received_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in approvers (list)
        _items = []
        if self.approvers:
            for _item_approvers in self.approvers:
                if _item_approvers:
                    _items.append(_item_approvers.to_dict())
            _dict['approvers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in distribution_members (list)
        _items = []
        if self.distribution_members:
            for _item_distribution_members in self.distribution_members:
                if _item_distribution_members:
                    _items.append(_item_distribution_members.to_dict())
            _dict['distribution_members'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ball_in_court (list)
        _items = []
        if self.ball_in_court:
            for _item_ball_in_court in self.ball_in_court:
                if _item_ball_in_court:
                    _items.append(_item_ball_in_court.to_dict())
            _dict['ball_in_court'] = _items
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of specification_section
        if self.specification_section:
            _dict['specification_section'] = self.specification_section.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of distribution_info
        if self.distribution_info:
            _dict['distribution_info'] = self.distribution_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of submittal_package
        if self.submittal_package:
            _dict['submittal_package'] = self.submittal_package.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10SubmittalLogsIdGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "number": obj.get("number"),
            "formatted_number": obj.get("formatted_number"),
            "revision": obj.get("revision"),
            "private": obj.get("private"),
            "received_date": obj.get("received_date"),
            "issue_date": obj.get("issue_date"),
            "submit_by": obj.get("submit_by"),
            "due_date": obj.get("due_date"),
            "type": obj.get("type"),
            "description": obj.get("description"),
            "status": obj.get("status"),
            "closed": obj.get("closed"),
            "created_by": RestV10SubmittalLogsIdGet200ResponseCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "received_from": RestV10SubmittalLogsIdGet200ResponseReceivedFrom.from_dict(obj["received_from"]) if obj.get("received_from") is not None else None,
            "approvers": [RestV10SubmittalLogsIdGet200ResponseApproversInner.from_dict(_item) for _item in obj["approvers"]] if obj.get("approvers") is not None else None,
            "distribution_members": [RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(_item) for _item in obj["distribution_members"]] if obj.get("distribution_members") is not None else None,
            "ball_in_court": [RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.from_dict(_item) for _item in obj["ball_in_court"]] if obj.get("ball_in_court") is not None else None,
            "location": Location.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "specification_section": RestV10SubmittalLogsGet200ResponseInnerSpecificationSection.from_dict(obj["specification_section"]) if obj.get("specification_section") is not None else None,
            "attachments": [RestV10WorkOrderContractsPost201ResponseAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "distribution_info": RestV10SubmittalLogsIdGet200ResponseDistributionInfo.from_dict(obj["distribution_info"]) if obj.get("distribution_info") is not None else None,
            "submittal_package": RestV10SubmittalLogsIdGet200ResponseSubmittalPackage.from_dict(obj["submittal_package"]) if obj.get("submittal_package") is not None else None
        })
        return _obj


