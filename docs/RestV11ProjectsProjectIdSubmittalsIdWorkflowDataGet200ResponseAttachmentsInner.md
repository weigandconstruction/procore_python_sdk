# RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**approver_id** | **int** |  | [optional] 
**approver_marked_up_at** | **str** |  | [optional] 
**can_carry_forward** | **bool** |  | [optional] 
**download_url** | **str** |  | [optional] 
**has_failed** | **bool** |  | [optional] 
**is_originating_attachment** | **bool** |  | [optional] 
**is_processing** | **bool** |  | [optional] 
**last_marked_up_at** | **str** |  | [optional] 
**last_marked_up_by** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**viewer_type** | **str** |  | [optional] 
**viewer_url** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_attachments_inner import RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner from a JSON string
rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_attachments_inner_instance = RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_attachments_inner_dict = rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_attachments_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner from a dict
rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_attachments_inner_from_dict = RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner.from_dict(rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


