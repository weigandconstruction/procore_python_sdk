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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request_selected_approvers_inner import RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequestSelectedApproversInner
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest(BaseModel):
    """
    RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest
    """ # noqa: E501
    submittal_log_status_id: Optional[StrictInt] = None
    submittal_description: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    prostore_file_ids: Optional[List[StrictInt]] = None
    recipient_ids: Optional[List[StrictInt]] = None
    selected_approvers: Optional[List[RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequestSelectedApproversInner]] = None
    __properties: ClassVar[List[str]] = ["submittal_log_status_id", "submittal_description", "message", "prostore_file_ids", "recipient_ids", "selected_approvers"]

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
        """Create an instance of RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in selected_approvers (list)
        _items = []
        if self.selected_approvers:
            for _item_selected_approvers in self.selected_approvers:
                if _item_selected_approvers:
                    _items.append(_item_selected_approvers.to_dict())
            _dict['selected_approvers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "submittal_log_status_id": obj.get("submittal_log_status_id"),
            "submittal_description": obj.get("submittal_description"),
            "message": obj.get("message"),
            "prostore_file_ids": obj.get("prostore_file_ids"),
            "recipient_ids": obj.get("recipient_ids"),
            "selected_approvers": [RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequestSelectedApproversInner.from_dict(_item) for _item in obj["selected_approvers"]] if obj.get("selected_approvers") is not None else None
        })
        return _obj


