# RestV10ProjectsProjectIdRfisGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**link** | **str** | Web link to resource | [optional] 
**location_id** | **int** | ID of the associated Location | [optional] 
**questions** | [**List[RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfQuestionsInner]**](RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfQuestionsInner.md) | RFI Questions | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**id** | **int** | ID | [optional] 
**assignee** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**assignees** | [**List[RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfAssigneesInner]**](RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfAssigneesInner.md) | RFI Assignees | [optional] 
**ball_in_court** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**ball_in_courts** | [**List[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee]**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) | Ball In Courts | [optional] 
**cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**cost_impact** | [**RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfCostImpact**](RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfCostImpact.md) |  | [optional] 
**created_at** | **datetime** | Date created | [optional] 
**deleted** | **bool** | Deleted status (this is only shown on deleted records) | [optional] 
**deleted_at** | **datetime** | Time deleted (this is only shown on deleted records) | [optional] 
**due_date** | **date** | Due Date | [optional] 
**initiated_at** | **datetime** | Date initiated | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**full_number** | **str** | Full Number | [optional] 
**number** | **str** | Number | [optional] 
**prefix** | **str** | Prefix | [optional] 
**private** | **bool** | Private Status | [optional] 
**project_stage** | [**RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfProjectStage**](RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfProjectStage.md) |  | [optional] 
**received_from** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**reference** | **str** | Reference | [optional] 
**responsible_contractor** | [**RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.md) |  | [optional] 
**rfi_manager** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**schedule_impact** | [**RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfScheduleImpact**](RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfScheduleImpact.md) |  | [optional] 
**status** | **str** | Status | [optional] 
**translated_status** | **str** | Translated RFI status | [optional] 
**sub_job** | [**TimecardEntry3SubJob**](TimecardEntry3SubJob.md) |  | [optional] 
**subject** | **str** | Subject | [optional] 
**time_resolved** | **datetime** | Time RFI was closed | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_rfis_get200_response_inner import RestV10ProjectsProjectIdRfisGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRfisGet200ResponseInner from a JSON string
rest_v10_projects_project_id_rfis_get200_response_inner_instance = RestV10ProjectsProjectIdRfisGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRfisGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_rfis_get200_response_inner_dict = rest_v10_projects_project_id_rfis_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRfisGet200ResponseInner from a dict
rest_v10_projects_project_id_rfis_get200_response_inner_from_dict = RestV10ProjectsProjectIdRfisGet200ResponseInner.from_dict(rest_v10_projects_project_id_rfis_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


