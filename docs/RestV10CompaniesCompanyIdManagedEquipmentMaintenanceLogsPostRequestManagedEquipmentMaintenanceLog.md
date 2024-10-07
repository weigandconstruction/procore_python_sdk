# RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequestManagedEquipmentMaintenanceLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_equipment_id** | **int** | Equipment Id the maintenance log is associated with | [optional] 
**last_service_date** | **date** | The Date the equipment was last services | [optional] 
**next_service_date** | **date** | Next service date for the equipment | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request_managed_equipment_maintenance_log import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequestManagedEquipmentMaintenanceLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequestManagedEquipmentMaintenanceLog from a JSON string
rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request_managed_equipment_maintenance_log_instance = RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequestManagedEquipmentMaintenanceLog.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequestManagedEquipmentMaintenanceLog.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request_managed_equipment_maintenance_log_dict = rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request_managed_equipment_maintenance_log_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequestManagedEquipmentMaintenanceLog from a dict
rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request_managed_equipment_maintenance_log_from_dict = RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequestManagedEquipmentMaintenanceLog.from_dict(rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request_managed_equipment_maintenance_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


