# RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequestManagedEquipment

Managed Equipment Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_equipment_ids** | **List[int]** | IDs of all Managed Equipment specified for bulk restore | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_bulk_restore_patch_request_managed_equipment import RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequestManagedEquipment

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequestManagedEquipment from a JSON string
rest_v10_companies_company_id_managed_equipment_bulk_restore_patch_request_managed_equipment_instance = RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequestManagedEquipment.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequestManagedEquipment.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_bulk_restore_patch_request_managed_equipment_dict = rest_v10_companies_company_id_managed_equipment_bulk_restore_patch_request_managed_equipment_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequestManagedEquipment from a dict
rest_v10_companies_company_id_managed_equipment_bulk_restore_patch_request_managed_equipment_from_dict = RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequestManagedEquipment.from_dict(rest_v10_companies_company_id_managed_equipment_bulk_restore_patch_request_managed_equipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


