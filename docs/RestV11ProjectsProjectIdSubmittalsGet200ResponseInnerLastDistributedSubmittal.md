# RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**distributed_attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**distributed_responses** | [**List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittalDistributedResponsesInner]**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittalDistributedResponsesInner.md) |  | [optional] 
**distributed_by** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser.md) |  | [optional] 
**distributed_to** | [**List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser]**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser.md) |  | [optional] 
**message** | **str** |  | [optional] 
**sent_at** | **datetime** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal import RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittal

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittal from a JSON string
rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal_instance = RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittal.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittal.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal_dict = rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittal from a dict
rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal_from_dict = RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittal.from_dict(rest_v11_projects_project_id_submittals_get200_response_inner_last_distributed_submittal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


