# RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequestManagedEquipmentMaintenanceLogsAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_equipment_maintenance_logs_id** | **int** | Maintenance log Id the maintenance log attachment is associated with | [optional] 
**documents** | **List[int]** |  | [optional] 
**folders** | **List[int]** |  | [optional] 
**upload_uuids** | **List[int]** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post_request_managed_equipment_maintenance_logs_attachment import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequestManagedEquipmentMaintenanceLogsAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequestManagedEquipmentMaintenanceLogsAttachment from a JSON string
rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post_request_managed_equipment_maintenance_logs_attachment_instance = RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequestManagedEquipmentMaintenanceLogsAttachment.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequestManagedEquipmentMaintenanceLogsAttachment.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post_request_managed_equipment_maintenance_logs_attachment_dict = rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post_request_managed_equipment_maintenance_logs_attachment_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequestManagedEquipmentMaintenanceLogsAttachment from a dict
rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post_request_managed_equipment_maintenance_logs_attachment_from_dict = RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequestManagedEquipmentMaintenanceLogsAttachment.from_dict(rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post_request_managed_equipment_maintenance_logs_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


