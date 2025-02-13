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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v11_projects_project_id_submittals_post_request1_submittal_workflow_data_inner_inner import RestV11ProjectsProjectIdSubmittalsPostRequest1SubmittalWorkflowDataInnerInner
from procore_sdk.models.work_order_contract_custom_field_custom_field_definition_id import WorkOrderContractCustomFieldCustomFieldDefinitionId
from typing import Optional, Set
from typing_extensions import Self

class RestV11ProjectsProjectIdSubmittalsPostRequest1Submittal(BaseModel):
    """
    RestV11ProjectsProjectIdSubmittalsPostRequest1Submittal
    """ # noqa: E501
    actual_delivery_date: Optional[date] = Field(default=None, description="The Actual Delivery Date of the Submittal *This field can only be set if the project has submittal delivery information enabled")
    attachments: Optional[List[StrictStr]] = Field(default=None, description="Submittal attachments. To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.")
    confirmed_delivery_date: Optional[date] = Field(default=None, description="The Confirmed Delivery Date of the Submittal *This field can only be set if the project has submittal delivery information enabled")
    cost_code_id: Optional[StrictInt] = Field(default=None, description="The ID of the Cost Code of the Submittal *This field can only be set by admins")
    custom_textarea_1: Optional[StrictStr] = Field(default=None, description="*This field can only be set by admins ")
    custom_textfield_1: Optional[StrictStr] = Field(default=None, description="*This field can only be set by admins ")
    description: Optional[StrictStr] = Field(default=None, description="The Description of the Submittal")
    design_team_review_time: Optional[StrictInt] = Field(default=None, description="The Design Team Review Time of the Submittal (in days) *This field can only be set if the project has schedule calculations enabled")
    distribution_member_ids: Optional[List[StrictInt]] = Field(default=None, description="The IDs of the Distribution Members of the Submittal")
    due_date: Optional[date] = Field(default=None, description="The Due Date of the Submittal *This field is not available to be set if sequential approvers is enabled")
    internal_review_time: Optional[StrictInt] = Field(default=None, description="The Internal Review Time of the Submtital (in days) *This field can only be set if the project has schedule calculations enabled")
    issue_date: Optional[date] = Field(default=None, description="The Issue Date of the Submittal *This field can only be set by admins")
    lead_time: Optional[StrictInt] = Field(default=None, description="The Lead Time of the Submittal (in days) *This field can only be set by admins or if the project has schedule calculations enabled")
    location_id: Optional[StrictInt] = Field(default=None, description="The Location of the Submittal")
    number: StrictStr = Field(description="The Number of the Submittal")
    private: Optional[StrictBool] = Field(default=None, description="Whether the Submittal is Private or not")
    prostore_file_ids: Optional[List[StrictInt]] = Field(default=None, description="An array of Prostore File IDs. The Prostore Files will be associated with the Submittal as attachments.")
    received_date: Optional[date] = Field(default=None, description="The Received Date of the Submittal *This field can only be set by admins")
    received_from_id: Optional[StrictInt] = Field(default=None, description="The Received From of the Submittal")
    required_on_site_date: Optional[date] = Field(default=None, description="The Required On Site Date of the Submittal *This field can only be set by admins or if the project has schedule calculations enabled")
    responsible_contractor_id: Optional[StrictInt] = Field(default=None, description="The Responsible Contractor of the Submittal")
    revision: Optional[StrictStr] = Field(default=None, description="The Revision of the Submittal")
    scheduled_task_key: Optional[StrictStr] = Field(default=None, description="The key of the Scheduled Task of the Submittal. Note that use of this parameter is deprecated. Please use `scheduled_task_id` instead. *This field can only be set if the project has submittal delivery information enabled and the user has permissions to view the calendar tool")
    scheduled_task_id: Optional[StrictInt] = Field(default=None, description="The ID of the Scheduled Task of the Submittal *This field can only be set if the project has submittal delivery information enabled and the user has permissions to view the calendar tool")
    source_submittal_log_id: Optional[StrictInt] = Field(default=None, description="The ID of the Source Submittal. *By setting this field, the submittal will be created as a revision of source submittal.")
    specification_section_id: Optional[StrictInt] = Field(default=None, description="The ID of the Specification Section of the Submittal")
    status_id: Optional[StrictInt] = Field(default=None, description="The ID of the Submittal Status of the Submittal *This field can only be set by admins")
    sub_job_id: Optional[StrictInt] = Field(default=None, description="The ID of the Sub Job of the Submittal")
    submit_by: Optional[date] = Field(default=None, description="The Submit By Date of the Submittal *This field can only be set by admins")
    submittal_manager_id: Optional[StrictInt] = Field(default=None, description="The ID of the Submittal Manager of the Submittal *This field can only be set by admins")
    submittal_package_id: Optional[StrictInt] = Field(default=None, description="The ID of the Submittal Package of the Submittal *This field can only be set by admins")
    title: Optional[StrictStr] = Field(default=None, description="The Title of the Submittal")
    type: Optional[StrictStr] = Field(default=None, description="The Submittal Type of the Submittal")
    workflow_data: Optional[List[List[RestV11ProjectsProjectIdSubmittalsPostRequest1SubmittalWorkflowDataInnerInner]]] = None
    custom_field_custom_field_definition_id: Optional[WorkOrderContractCustomFieldCustomFieldDefinitionId] = Field(default=None, alias="custom_field_%{custom_field_definition_id}")
    __properties: ClassVar[List[str]] = ["actual_delivery_date", "attachments", "confirmed_delivery_date", "cost_code_id", "custom_textarea_1", "custom_textfield_1", "description", "design_team_review_time", "distribution_member_ids", "due_date", "internal_review_time", "issue_date", "lead_time", "location_id", "number", "private", "prostore_file_ids", "received_date", "received_from_id", "required_on_site_date", "responsible_contractor_id", "revision", "scheduled_task_key", "scheduled_task_id", "source_submittal_log_id", "specification_section_id", "status_id", "sub_job_id", "submit_by", "submittal_manager_id", "submittal_package_id", "title", "type", "workflow_data", "custom_field_%{custom_field_definition_id}"]

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
        """Create an instance of RestV11ProjectsProjectIdSubmittalsPostRequest1Submittal from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in workflow_data (list of list)
        _items = []
        if self.workflow_data:
            for _item_workflow_data in self.workflow_data:
                if _item_workflow_data:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item_workflow_data if _inner_item is not None]
                    )
            _dict['workflow_data'] = _items
        # override the default output from pydantic by calling `to_dict()` of custom_field_custom_field_definition_id
        if self.custom_field_custom_field_definition_id:
            _dict['custom_field_%{custom_field_definition_id}'] = self.custom_field_custom_field_definition_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV11ProjectsProjectIdSubmittalsPostRequest1Submittal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actual_delivery_date": obj.get("actual_delivery_date"),
            "attachments": obj.get("attachments"),
            "confirmed_delivery_date": obj.get("confirmed_delivery_date"),
            "cost_code_id": obj.get("cost_code_id"),
            "custom_textarea_1": obj.get("custom_textarea_1"),
            "custom_textfield_1": obj.get("custom_textfield_1"),
            "description": obj.get("description"),
            "design_team_review_time": obj.get("design_team_review_time"),
            "distribution_member_ids": obj.get("distribution_member_ids"),
            "due_date": obj.get("due_date"),
            "internal_review_time": obj.get("internal_review_time"),
            "issue_date": obj.get("issue_date"),
            "lead_time": obj.get("lead_time"),
            "location_id": obj.get("location_id"),
            "number": obj.get("number"),
            "private": obj.get("private"),
            "prostore_file_ids": obj.get("prostore_file_ids"),
            "received_date": obj.get("received_date"),
            "received_from_id": obj.get("received_from_id"),
            "required_on_site_date": obj.get("required_on_site_date"),
            "responsible_contractor_id": obj.get("responsible_contractor_id"),
            "revision": obj.get("revision"),
            "scheduled_task_key": obj.get("scheduled_task_key"),
            "scheduled_task_id": obj.get("scheduled_task_id"),
            "source_submittal_log_id": obj.get("source_submittal_log_id"),
            "specification_section_id": obj.get("specification_section_id"),
            "status_id": obj.get("status_id"),
            "sub_job_id": obj.get("sub_job_id"),
            "submit_by": obj.get("submit_by"),
            "submittal_manager_id": obj.get("submittal_manager_id"),
            "submittal_package_id": obj.get("submittal_package_id"),
            "title": obj.get("title"),
            "type": obj.get("type"),
            "workflow_data": [
                    [RestV11ProjectsProjectIdSubmittalsPostRequest1SubmittalWorkflowDataInnerInner.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["workflow_data"]
                ] if obj.get("workflow_data") is not None else None,
            "custom_field_%{custom_field_definition_id}": WorkOrderContractCustomFieldCustomFieldDefinitionId.from_dict(obj["custom_field_%{custom_field_definition_id}"]) if obj.get("custom_field_%{custom_field_definition_id}") is not None else None
        })
        return _obj


