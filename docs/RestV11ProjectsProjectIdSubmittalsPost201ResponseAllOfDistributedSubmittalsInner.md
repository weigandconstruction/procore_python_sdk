# RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfDistributedSubmittalsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**sent_at** | **datetime** |  | [optional] 
**distributed_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**distributed_to** | [**List[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee]**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**final_attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**selected_approver_ids** | **List[int]** | List of Submittal Approver IDs for approvers selected to be distributed | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_post201_response_all_of_distributed_submittals_inner import RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfDistributedSubmittalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfDistributedSubmittalsInner from a JSON string
rest_v11_projects_project_id_submittals_post201_response_all_of_distributed_submittals_inner_instance = RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfDistributedSubmittalsInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfDistributedSubmittalsInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_post201_response_all_of_distributed_submittals_inner_dict = rest_v11_projects_project_id_submittals_post201_response_all_of_distributed_submittals_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfDistributedSubmittalsInner from a dict
rest_v11_projects_project_id_submittals_post201_response_all_of_distributed_submittals_inner_from_dict = RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfDistributedSubmittalsInner.from_dict(rest_v11_projects_project_id_submittals_post201_response_all_of_distributed_submittals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


