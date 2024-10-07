# RestV11ProjectsProjectIdSubmittalsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**approvers** | [**List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInner]**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInner.md) |  | [optional] 
**associated_attachments** | [**List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerAssociatedAttachmentsInner]**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerAssociatedAttachmentsInner.md) |  | [optional] 
**ball_in_court** | [**List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerBallInCourtInner]**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerBallInCourtInner.md) |  | [optional] 
**cost_code_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser.md) |  | [optional] 
**current_revision** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**distributed_at** | **datetime** |  | [optional] 
**distribution_members** | [**List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser]**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser.md) |  | [optional] 
**drawing_ids** | **List[int]** |  | [optional] 
**due_date** | **date** |  | [optional] 
**formatted_number** | **str** |  | [optional] 
**issue_date** | **date** |  | [optional] 
**last_distributed_submittal** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittal**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerLastDistributedSubmittal.md) |  | [optional] 
**linked_drawing_ids** | **List[int]** |  | [optional] 
**location_id** | **int** |  | [optional] 
**number** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**received_date** | **date** |  | [optional] 
**received_from** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser.md) |  | [optional] 
**responsible_contractor** | [**RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.md) |  | [optional] 
**revision** | **str** |  | [optional] 
**specification_section** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection.md) |  | [optional] 
**status** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerStatus**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerStatus.md) |  | [optional] 
**sub_job_id** | **int** |  | [optional] 
**submit_by** | **date** |  | [optional] 
**submittal_manager** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser.md) |  | [optional] 
**submittal_package** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSubmittalPackage**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSubmittalPackage.md) |  | [optional] 
**title** | **str** |  | [optional] 
**type** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerType**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerType.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_get200_response_inner import RestV11ProjectsProjectIdSubmittalsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsGet200ResponseInner from a JSON string
rest_v11_projects_project_id_submittals_get200_response_inner_instance = RestV11ProjectsProjectIdSubmittalsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_get200_response_inner_dict = rest_v11_projects_project_id_submittals_get200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsGet200ResponseInner from a dict
rest_v11_projects_project_id_submittals_get200_response_inner_from_dict = RestV11ProjectsProjectIdSubmittalsGet200ResponseInner.from_dict(rest_v11_projects_project_id_submittals_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


