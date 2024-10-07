# RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner

Equipment Log

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**project_id** | **int** | ID of the project the equipment was logged for | [optional] 
**managed_equipment_id** | **int** | Equipment Id the log is associated with | [optional] 
**onsite** | **date** | The date equipment arrived on site | [optional] 
**offsite** | **date** | The date equipment leaves the site | [optional] 
**updated_at** | **datetime** | Date the equipment log was updated | [optional] 
**created_at** | **datetime** | Date the equipment log was created | [optional] 
**deleted_at** | **datetime** | Date the equipment log was deleted | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**formatted_offsite** | **date** | The formatted date equipment left on site | [optional] 
**formatted_onsite** | **date** | The formatted date equipment arrived on site | [optional] 
**responsible_contractor** | **str** | The responsible contractor | [optional] 
**inspection_date** | **date** | The date the equipment was inspected | [optional] 
**induction_checklist_list_id** | **int** | Id of the inspection list the equipment uses | [optional] 
**induction_number** | **str** | The number used for equipment induction | [optional] 
**induction_status** | **bool** | Indicates if the equipemnt has been successfully inspected and allowed to perform work | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner_instance = RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner_dict = rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner from a dict
rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner_from_dict = RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner.from_dict(rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


