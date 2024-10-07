# RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200ResponseDistributedResponsesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**distributed_attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**response_name** | **str** |  | [optional] 
**submittal_response** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse.md) |  | [optional] 
**submittal_response_id** | **int** |  | [optional] 
**submittal_approver_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**user** | [**RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner**](RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response_distributed_responses_inner import RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200ResponseDistributedResponsesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200ResponseDistributedResponsesInner from a JSON string
rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response_distributed_responses_inner_instance = RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200ResponseDistributedResponsesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200ResponseDistributedResponsesInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response_distributed_responses_inner_dict = rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response_distributed_responses_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200ResponseDistributedResponsesInner from a dict
rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response_distributed_responses_inner_from_dict = RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200ResponseDistributedResponsesInner.from_dict(rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response_distributed_responses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


