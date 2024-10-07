# RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequestManagedEquipmentType

Managed Equipment Type Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | If the equipment type is active | [optional] 
**managed_equipment_category_id** | **int** | The category id the Managed Equipment Type is associated with | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch_request_managed_equipment_type import RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequestManagedEquipmentType

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequestManagedEquipmentType from a JSON string
rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch_request_managed_equipment_type_instance = RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequestManagedEquipmentType.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequestManagedEquipmentType.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch_request_managed_equipment_type_dict = rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch_request_managed_equipment_type_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequestManagedEquipmentType from a dict
rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch_request_managed_equipment_type_from_dict = RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequestManagedEquipmentType.from_dict(rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch_request_managed_equipment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


