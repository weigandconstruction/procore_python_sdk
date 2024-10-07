# RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequestManagedEquipmentLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | ID of the project the equipment was logged for | [optional] 
**managed_equipment_id** | **int** | Equipment Id the log is associated with | [optional] 
**onsite** | **date** | The Date equipment arrived on site | [optional] 
**offsite** | **date** | The Date equipment left the site | [optional] 
**inspection_date** | **date** | The date the equipment was inspected | [optional] 
**induction_checklist_list_id** | **int** | Id of the inspection list the equipment uses | [optional] 
**induction_number** | **str** | The number used for equipment induction | [optional] 
**induction_status** | **bool** | Indicates if the equipemnt has been successfully inspected and allowed to perform work | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_post_request_managed_equipment_log import RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequestManagedEquipmentLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequestManagedEquipmentLog from a JSON string
rest_v10_companies_company_id_managed_equipment_logs_post_request_managed_equipment_log_instance = RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequestManagedEquipmentLog.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequestManagedEquipmentLog.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_logs_post_request_managed_equipment_log_dict = rest_v10_companies_company_id_managed_equipment_logs_post_request_managed_equipment_log_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequestManagedEquipmentLog from a dict
rest_v10_companies_company_id_managed_equipment_logs_post_request_managed_equipment_log_from_dict = RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequestManagedEquipmentLog.from_dict(rest_v10_companies_company_id_managed_equipment_logs_post_request_managed_equipment_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


