# RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvers** | [**List[RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner]**](RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInnerAllOfApproversInner.md) |  | [optional] 
**attachments_count** | **int** |  | [optional] 
**ball_in_court** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**buffer_time** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**current_revision** | **bool** |  | [optional] 
**distributed_at** | **datetime** |  | [optional] 
**due_date** | **date** |  | [optional] 
**for_record_only** | **bool** |  | [optional] 
**formatted_number** | **str** |  | [optional] 
**issue_date** | **date** |  | [optional] 
**private** | **bool** |  | [optional] 
**received_date** | **date** |  | [optional] 
**received_from** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**responsible_contractor** | [**RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.md) |  | [optional] 
**specification_section** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection.md) |  | [optional] 
**sub_job** | [**TimecardEntry3SubJob**](TimecardEntry3SubJob.md) |  | [optional] 
**submit_by** | **date** |  | [optional] 
**status** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerStatus**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerStatus.md) |  | [optional] 
**type** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerType**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerType.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**submittal_manager** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**submittal_package** | [**RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage**](RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**open_date** | **date** |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**id** | **int** |  | [optional] 
**number** | **str** |  | [optional] 
**revision** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner import RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInner from a JSON string
rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner_instance = RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner_dict = rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInner from a dict
rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner_from_dict = RestV11ProjectsProjectIdSubmittalsRecycleBinGet200ResponseInner.from_dict(rest_v11_projects_project_id_submittals_recycle_bin_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


