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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.body104_coordination_issue_origin import Body104CoordinationIssueOrigin
from procore_sdk.models.coordination_issue_sync_response_errors_inner_all_of_viewpoints_inner import CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_errors_inner_all_of_errors import RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors
from typing import Optional, Set
from typing_extensions import Self

class CoordinationIssueSyncResponseErrorsInner(BaseModel):
    """
    CoordinationIssueSyncResponseErrorsInner
    """ # noqa: E501
    uuid: Optional[StrictStr] = Field(default=None, description="Coordination Issue UUID. This is an optional parameter, and is set automatically on server if not present in the payload")
    title: StrictStr = Field(description="Coordination Issue title. The title can have a maximum of 80 characters")
    description: Optional[StrictStr] = Field(default=None, description="Coordination Issue description.")
    status: Optional[StrictStr] = Field(default=None, description="Status of the issue. Should be either open or closed")
    creation_source: Optional[StrictStr] = Field(default=None, description="Source of issue creation. This attribute is ignored when issue is create by third party developers.")
    location_id: Optional[StrictInt] = Field(default=None, description="Location where the issue is present. The location must be in the same project as the project_id")
    assignee_id: Optional[StrictInt] = Field(default=None, description="ID of Procore user that should be assigned the issue")
    coordination_issue_file_id: Optional[StrictInt] = Field(default=None, description="ID of the BIM File to be set as origin source")
    drawing_revision_id: Optional[StrictInt] = Field(default=None, description="ID of the drawing revision to be set as origin source. Only one of drawing_revision_id or coordination_issue_file_id can be present")
    bim_model_id: Optional[StrictInt] = Field(default=None, description="ID of the model to be associated")
    due_date: Optional[StrictStr] = Field(default=None, description="Due date of the Coordination Issue")
    origin: Optional[Body104CoordinationIssueOrigin] = None
    attachment_upload_uuids: Optional[List[StrictStr]] = None
    attachments: Optional[List[StrictStr]] = None
    viewpoints: Optional[List[CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner]] = Field(default=None, description="An array of issue viewpoints. Only one viewpoint is allowed at this time.")
    errors: Optional[RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors] = None
    __properties: ClassVar[List[str]] = ["uuid", "title", "description", "status", "creation_source", "location_id", "assignee_id", "coordination_issue_file_id", "drawing_revision_id", "bim_model_id", "due_date", "origin", "attachment_upload_uuids", "attachments", "viewpoints", "errors"]

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
        """Create an instance of CoordinationIssueSyncResponseErrorsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of origin
        if self.origin:
            _dict['origin'] = self.origin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in viewpoints (list)
        _items = []
        if self.viewpoints:
            for _item_viewpoints in self.viewpoints:
                if _item_viewpoints:
                    _items.append(_item_viewpoints.to_dict())
            _dict['viewpoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of errors
        if self.errors:
            _dict['errors'] = self.errors.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CoordinationIssueSyncResponseErrorsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "status": obj.get("status"),
            "creation_source": obj.get("creation_source"),
            "location_id": obj.get("location_id"),
            "assignee_id": obj.get("assignee_id"),
            "coordination_issue_file_id": obj.get("coordination_issue_file_id"),
            "drawing_revision_id": obj.get("drawing_revision_id"),
            "bim_model_id": obj.get("bim_model_id"),
            "due_date": obj.get("due_date"),
            "origin": Body104CoordinationIssueOrigin.from_dict(obj["origin"]) if obj.get("origin") is not None else None,
            "attachment_upload_uuids": obj.get("attachment_upload_uuids"),
            "attachments": obj.get("attachments"),
            "viewpoints": [CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner.from_dict(_item) for _item in obj["viewpoints"]] if obj.get("viewpoints") is not None else None,
            "errors": RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.from_dict(obj["errors"]) if obj.get("errors") is not None else None
        })
        return _obj


