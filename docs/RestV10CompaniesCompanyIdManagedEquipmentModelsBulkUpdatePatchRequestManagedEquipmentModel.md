# RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel

Managed Equipment Model Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | If the equipment model is active | [optional] 
**managed_equipment_make_id** | **int** | The make id the Managed Equipment Model is associated with | [optional] 
**managed_equipment_type_id** | **int** | The make id the Managed Equipment Model is associated with | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request_managed_equipment_model import RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel from a JSON string
rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request_managed_equipment_model_instance = RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request_managed_equipment_model_dict = rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request_managed_equipment_model_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel from a dict
rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request_managed_equipment_model_from_dict = RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel.from_dict(rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request_managed_equipment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


