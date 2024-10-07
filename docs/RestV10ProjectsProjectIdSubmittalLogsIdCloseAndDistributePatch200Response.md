# RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**submittal_description** | **str** |  | [optional] 
**sent_at** | **datetime** |  | [optional] 
**distributed_by** | [**RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner**](RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner.md) |  | [optional] 
**distributed_to** | [**List[RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner]**](RestV10ProjectsProjectIdDistributionGroupsPost200ResponseUsersInner.md) |  | [optional] 
**distributed_attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**download_all_attachments_url** | **str** |  | [optional] 
**submittal_distributed_attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**download_all_submittal_distributed_attachments_url** | **str** |  | [optional] 
**message_distributed_attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**download_all_message_distributed_attachments_url** | **str** |  | [optional] 
**distributed_responses** | [**List[RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200ResponseDistributedResponsesInner]**](RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200ResponseDistributedResponsesInner.md) | List of submittal responses selected to be distributed | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response import RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200Response from a JSON string
rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response_instance = RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response_dict = rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200Response from a dict
rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response_from_dict = RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200Response.from_dict(rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


