# RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner

Equipment Maintenance Log

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**project_id** | **int** | ID of the project the equipment was logged for | [optional] 
**managed_equipment_id** | **int** | Equipment ID the log is associated to | [optional] 
**last_service_date** | **date** | The Date the equipment was last services | [optional] 
**next_service_date** | **date** | Next service date for the equipment | [optional] 
**updated_at** | **datetime** | Date the equipment log was updated | [optional] 
**created_at** | **datetime** | Date the equipment log was created | [optional] 
**deleted_at** | **datetime** | Date the equipment log was deleted | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner_instance = RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner_dict = rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner from a dict
rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner_from_dict = RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.from_dict(rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


