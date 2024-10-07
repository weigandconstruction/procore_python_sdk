# RestV10WorkflowActivityHistoriesGet200ResponseInner

Workflow Activity History

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**attachments** | **List[str]** | List of Attachment URLs | [optional] 
**bic_duration** | **str** | Ball In Court duration in days | [optional] 
**bic_start** | **datetime** | Ball In Court started at | [optional] 
**bic_end** | **datetime** | Ball In Court ended at | [optional] 
**comments** | **str** | Comments | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**performed_by_id** | **int** | Login Information ID of a Workflow User Role Login Information. | [optional] 
**performed_by_name** | **str** | Full Name of Contact for Workflow User Role Login Information | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**workflow_activity_id** | **int** | Workflow Activity ID | [optional] 
**workflow_activity_name** | **str** | Workflow Activity Name | [optional] 
**workflow_instance_id** | **int** | Workflow Instance ID | [optional] 
**workflow_user_role_id** | **int** | Workflow User Role ID | [optional] 
**workflow_user_role_name** | **str** | Workflow User Role Name | [optional] 
**workflow_state_id** | **int** | Workflow State ID | [optional] 
**workflow_state_name** | **str** | Workflow State Name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_workflow_activity_histories_get200_response_inner import RestV10WorkflowActivityHistoriesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkflowActivityHistoriesGet200ResponseInner from a JSON string
rest_v10_workflow_activity_histories_get200_response_inner_instance = RestV10WorkflowActivityHistoriesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkflowActivityHistoriesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_workflow_activity_histories_get200_response_inner_dict = rest_v10_workflow_activity_histories_get200_response_inner_instance.to_dict()
# create an instance of RestV10WorkflowActivityHistoriesGet200ResponseInner from a dict
rest_v10_workflow_activity_histories_get200_response_inner_from_dict = RestV10WorkflowActivityHistoriesGet200ResponseInner.from_dict(rest_v10_workflow_activity_histories_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


