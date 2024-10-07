# RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInnerPayload

Contains specific attributes depending on the type of Reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | [**RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment**](RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment.md) |  | [optional] 
**drawing_id** | **int** | ID of the Drawing the Drawing Revision belongs to | [optional] 
**drawing_revision_id** | **int** | ID of the latest Drawing Revision of the Drawing | [optional] 
**file_version_id** | **int** | ID of the latest File Version of the Folder File | [optional] 
**folder_id** | **int** | ID of the Folder File the File Version belongs to | [optional] 
**specification_section_id** | **int** | Specification Section ID | [optional] 
**specification_section_current_revision_id** | **int** | Current Revision ID of a Specification Section | [optional] 
**generic_tool_item_id** | **int** | Generic Tool Item (Correspondence) ID | [optional] 
**form_id** | **int** | Form ID | [optional] 
**meeting_id** | **int** | Meeting ID | [optional] 
**observation_item_id** | **int** | Observation Item ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_references_get200_response_inner_payload import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInnerPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInnerPayload from a JSON string
rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_references_get200_response_inner_payload_instance = RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInnerPayload.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInnerPayload.to_json())

# convert the object into a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_references_get200_response_inner_payload_dict = rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_references_get200_response_inner_payload_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInnerPayload from a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_references_get200_response_inner_payload_from_dict = RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInnerPayload.from_dict(rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_references_get200_response_inner_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


