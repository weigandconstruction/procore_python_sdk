# RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequestManagedEquipmentAttachment

Managed Equipment Attachment Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_equipment_id** | **int** | ID of the Managed Equipment associated with the attachment(s) | [optional] 
**managed_equipment_attachment_ids** | **List[int]** | IDs of all the Managed Equipment Attachment values specified for bulk destroy | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete_request_managed_equipment_attachment import RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequestManagedEquipmentAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequestManagedEquipmentAttachment from a JSON string
rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete_request_managed_equipment_attachment_instance = RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequestManagedEquipmentAttachment.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequestManagedEquipmentAttachment.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete_request_managed_equipment_attachment_dict = rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete_request_managed_equipment_attachment_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequestManagedEquipmentAttachment from a dict
rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete_request_managed_equipment_attachment_from_dict = RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequestManagedEquipmentAttachment.from_dict(rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete_request_managed_equipment_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


