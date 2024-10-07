# RestV11ProjectsProjectIdSubmittalsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_delivery_date** | **date** |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**confirmed_delivery_date** | **date** |  | [optional] 
**cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**custom_textarea_1** | **str** |  | [optional] 
**custom_textfield_1** | **str** |  | [optional] 
**deleted_at** | **datetime** | *This field only displays on deleted items | [optional] 
**description** | **str** |  | [optional] 
**design_team_review_time** | **int** |  | [optional] 
**distribution_members** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**internal_review_time** | **int** |  | [optional] 
**lead_time** | **int** |  | [optional] 
**required_on_site_date** | **date** |  | [optional] 
**scheduled_task** | [**Task2**](Task2.md) |  | [optional] 
**source_submittal_log_id** | **int** |  | [optional] 
**distributed_submittals** | [**List[RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfDistributedSubmittalsInner]**](RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfDistributedSubmittalsInner.md) |  | [optional] 
**approvers** | [**List[RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfApproversInner]**](RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfApproversInner.md) |  | [optional] 
**attachments_count** | **int** |  | [optional] 
**ball_in_court** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**buffer_time** | **int** |  | [optional] 
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
from procore_sdk.models.rest_v11_projects_project_id_submittals_post201_response import RestV11ProjectsProjectIdSubmittalsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsPost201Response from a JSON string
rest_v11_projects_project_id_submittals_post201_response_instance = RestV11ProjectsProjectIdSubmittalsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsPost201Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_post201_response_dict = rest_v11_projects_project_id_submittals_post201_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsPost201Response from a dict
rest_v11_projects_project_id_submittals_post201_response_from_dict = RestV11ProjectsProjectIdSubmittalsPost201Response.from_dict(rest_v11_projects_project_id_submittals_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


