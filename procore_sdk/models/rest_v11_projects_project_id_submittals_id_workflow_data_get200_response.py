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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_approvers_inner import RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseApproversInner
from procore_sdk.models.rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_attachments_inner import RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner
from procore_sdk.models.rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_steps_inner import RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseStepsInner
from typing import Optional, Set
from typing_extensions import Self

class RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200Response(BaseModel):
    """
    RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200Response
    """ # noqa: E501
    steps: Optional[List[RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseStepsInner]] = None
    approvers: Optional[List[RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseApproversInner]] = None
    attachments: Optional[List[RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner]] = None
    __properties: ClassVar[List[str]] = ["steps", "approvers", "attachments"]

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
        """Create an instance of RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item_steps in self.steps:
                if _item_steps:
                    _items.append(_item_steps.to_dict())
            _dict['steps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in approvers (list)
        _items = []
        if self.approvers:
            for _item_approvers in self.approvers:
                if _item_approvers:
                    _items.append(_item_approvers.to_dict())
            _dict['approvers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "steps": [RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseStepsInner.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "approvers": [RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseApproversInner.from_dict(_item) for _item in obj["approvers"]] if obj.get("approvers") is not None else None,
            "attachments": [RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None
        })
        return _obj


