# RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittalDistributedResponsesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**distributed_attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**submittal_response** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse.md) |  | [optional] 
**submittal_response_id** | **int** |  | [optional] 
**submittal_approver_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal_distributed_responses_inner import RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittalDistributedResponsesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittalDistributedResponsesInner from a JSON string
rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal_distributed_responses_inner_instance = RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittalDistributedResponsesInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittalDistributedResponsesInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal_distributed_responses_inner_dict = rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal_distributed_responses_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittalDistributedResponsesInner from a dict
rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal_distributed_responses_inner_from_dict = RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittalDistributedResponsesInner.from_dict(rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal_distributed_responses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


