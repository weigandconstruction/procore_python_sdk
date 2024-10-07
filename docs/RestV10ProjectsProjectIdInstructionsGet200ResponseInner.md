# RestV10ProjectsProjectIdInstructionsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**number** | **str** | Number | [optional] 
**title** | **str** | Number | [optional] 
**rich_text_description** | **str** | Rich Text Description | [optional] 
**plain_text_description** | **str** | Plain Text Description | [optional] 
**created_at** | **datetime** | Date created | [optional] 
**date_received** | **date** | Date created | [optional] 
**date_issued** | **datetime** | Date created | [optional] 
**status** | **str** | Status | [optional] 
**private** | **bool** | private | [optional] 
**schedule_impact** | [**RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfScheduleImpact**](RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfScheduleImpact.md) |  | [optional] 
**cost_impact** | [**RestV10ProjectsProjectIdInstructionsGet200ResponseInnerCostImpact**](RestV10ProjectsProjectIdInstructionsGet200ResponseInnerCostImpact.md) |  | [optional] 
**instruction_type** | [**RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType**](RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**instruction_from** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**distribution_members** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) | Instruction Distribution List of Users | [optional] 
**attentions** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) | Instruction Attentions | [optional] 
**attachments** | [**List[RestV10SubmittalApproversIdPatch200ResponseInnerAttachmentsInner]**](RestV10SubmittalApproversIdPatch200ResponseInnerAttachmentsInner.md) |  | [optional] 
**trades** | [**List[Trade2]**](Trade2.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_instructions_get200_response_inner import RestV10ProjectsProjectIdInstructionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdInstructionsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_instructions_get200_response_inner_instance = RestV10ProjectsProjectIdInstructionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdInstructionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_instructions_get200_response_inner_dict = rest_v10_projects_project_id_instructions_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdInstructionsGet200ResponseInner from a dict
rest_v10_projects_project_id_instructions_get200_response_inner_from_dict = RestV10ProjectsProjectIdInstructionsGet200ResponseInner.from_dict(rest_v10_projects_project_id_instructions_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


