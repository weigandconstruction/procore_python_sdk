# RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest1PlanReferencePayload

One of attachment, drawing_revision_id, file_version_id, specification_section_id, submittal_log_id, generic_tool_item_id, form_id, meeting_id, or observation_item_id is accepted depending on the type provided

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drawing_revision_id** | **int** | Drawing Revision ID | [optional] 
**file_version_id** | **int** | File Version ID | [optional] 
**specification_section_id** | **int** | Specification Section ID | [optional] 
**submittal_log_id** | **int** | Submittal Log ID | [optional] 
**attachment** | **bytearray** | Reference Attachment. To upload an attachment you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type with the &#x60;attachment&#x60; file. | [optional] 
**generic_tool_item_id** | **int** | Generic Tool Item (Correspondence) ID | [optional] 
**form_id** | **int** | Form ID | [optional] 
**meeting_id** | **int** | Meeting ID | [optional] 
**observation_item_id** | **int** | Observation Item ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_references_post_request1_plan_reference_payload import RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest1PlanReferencePayload

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest1PlanReferencePayload from a JSON string
rest_v10_projects_project_id_action_plans_plan_references_post_request1_plan_reference_payload_instance = RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest1PlanReferencePayload.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest1PlanReferencePayload.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_references_post_request1_plan_reference_payload_dict = rest_v10_projects_project_id_action_plans_plan_references_post_request1_plan_reference_payload_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest1PlanReferencePayload from a dict
rest_v10_projects_project_id_action_plans_plan_references_post_request1_plan_reference_payload_from_dict = RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest1PlanReferencePayload.from_dict(rest_v10_projects_project_id_action_plans_plan_references_post_request1_plan_reference_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


