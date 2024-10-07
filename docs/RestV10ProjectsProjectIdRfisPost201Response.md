# RestV10ProjectsProjectIdRfisPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** | RFI Acceptance status, true means the RFI is accepted and closed | [optional] 
**ball_in_court_role** | **str** | Ball in Court Role (can be Assignees, Creator, or RFI Manager) | [optional] 
**custom_textfield_1** | [**RestV10ProjectsProjectIdRfisPost201ResponseAllOfCustomTextfield1**](RestV10ProjectsProjectIdRfisPost201ResponseAllOfCustomTextfield1.md) |  | [optional] 
**custom_textfield_2** | [**RestV10ProjectsProjectIdRfisPost201ResponseAllOfCustomTextfield2**](RestV10ProjectsProjectIdRfisPost201ResponseAllOfCustomTextfield2.md) |  | [optional] 
**distribution_list** | [**List[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee]**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) | RFI Distribution List of Users | [optional] 
**draft** | **bool** | Draft status, true if draft | [optional] 
**drawing_ids** | **List[int]** | Array of IDs for associated Drawings | [optional] 
**drawing_number** | **str** | Drawing Number | [optional] 
**questions** | [**List[RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner]**](RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInner.md) | List of questions | [optional] 
**specification_section** | [**RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection**](RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection.md) |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**id** | **int** | ID | [optional] 
**assignee** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**assignees** | [**List[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee]**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) | RFI Assignees | [optional] 
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
**received_from** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**reference** | **str** | Reference | [optional] 
**responsible_contractor** | [**RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.md) |  | [optional] 
**rfi_manager** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**schedule_impact** | [**RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfScheduleImpact**](RestV10ProjectsProjectIdRfisGet200ResponseInnerAllOfScheduleImpact.md) |  | [optional] 
**status** | **str** | Status | [optional] 
**translated_status** | **str** | Translated RFI status | [optional] 
**subject** | **str** | Subject | [optional] 
**time_resolved** | **datetime** | Time RFI was closed | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response import RestV10ProjectsProjectIdRfisPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRfisPost201Response from a JSON string
rest_v10_projects_project_id_rfis_post201_response_instance = RestV10ProjectsProjectIdRfisPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRfisPost201Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_rfis_post201_response_dict = rest_v10_projects_project_id_rfis_post201_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRfisPost201Response from a dict
rest_v10_projects_project_id_rfis_post201_response_from_dict = RestV10ProjectsProjectIdRfisPost201Response.from_dict(rest_v10_projects_project_id_rfis_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


