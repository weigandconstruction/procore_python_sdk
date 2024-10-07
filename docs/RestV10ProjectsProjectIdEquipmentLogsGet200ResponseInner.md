# RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Date of record | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**hours_idle** | **str** | Number of hours the Equipment was idle | [optional] 
**hours_operating** | **str** | Number of hours the Equipment was in operation | [optional] 
**inspected** | **bool** | Equipment was inspected before operation | [optional] 
**inspection_hour** | **int** | Time of inspection - hour | [optional] 
**inspection_minute** | **int** | Time of Inspection - minute | [optional] 
**notes** | **str** | Additional Notes | [optional] 
**position** | **int** | Order in which this entry was recorded for the day | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**location** | [**Location2**](Location2.md) |  | [optional] 
**cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**equipment** | [**RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInnerEquipment**](RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInnerEquipment.md) |  | [optional] 
**permissions** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | Equipment Log Attachments are not viewable or used on web | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_equipment_logs_get200_response_inner_instance = RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_equipment_logs_get200_response_inner_dict = rest_v10_projects_project_id_equipment_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_equipment_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_equipment_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


