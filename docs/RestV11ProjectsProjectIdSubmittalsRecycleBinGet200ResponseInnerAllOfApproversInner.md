# RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approver_type** | **str** | Role of Approver | [optional] 
**comment** | **str** |  | [optional] 
**distributed** | **bool** |  | [optional] 
**response** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse.md) |  | [optional] 
**returned_date** | **date** | Returned Date | [optional] 
**sent_date** | **date** | Sent Date | [optional] 
**due_date** | **date** | Due Date | [optional] 
**response_required** | **bool** |  | [optional] 
**user** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | Attachments | [optional] 
**submittal_associated_attachment_ids** | **List[int]** | Submittal Associated Attachment IDs | [optional] 
**id** | **int** | ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner_all_of_approvers_inner import RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner from a JSON string
rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner_all_of_approvers_inner_instance = RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner_all_of_approvers_inner_dict = rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner_all_of_approvers_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner from a dict
rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner_all_of_approvers_inner_from_dict = RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner.from_dict(rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner_all_of_approvers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


