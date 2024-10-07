# RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_equipment_maintenance_log** | [**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequestManagedEquipmentMaintenanceLog**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequestManagedEquipmentMaintenanceLog.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest from a JSON string
rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request_instance = RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request_dict = rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest from a dict
rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request_from_dict = RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest.from_dict(rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


