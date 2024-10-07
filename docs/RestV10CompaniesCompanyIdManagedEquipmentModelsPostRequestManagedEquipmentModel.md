# RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequestManagedEquipmentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the equipment model | 
**managed_equipment_make_id** | **int** | Equipment make ID the model is associated to | 
**managed_equipment_type_id** | **int** | Equipment type ID the model is associated to | 
**is_active** | **bool** | If the equipment model is active | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_models_post_request_managed_equipment_model import RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequestManagedEquipmentModel

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequestManagedEquipmentModel from a JSON string
rest_v10_companies_company_id_managed_equipment_models_post_request_managed_equipment_model_instance = RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequestManagedEquipmentModel.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequestManagedEquipmentModel.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_models_post_request_managed_equipment_model_dict = rest_v10_companies_company_id_managed_equipment_models_post_request_managed_equipment_model_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequestManagedEquipmentModel from a dict
rest_v10_companies_company_id_managed_equipment_models_post_request_managed_equipment_model_from_dict = RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequestManagedEquipmentModel.from_dict(rest_v10_companies_company_id_managed_equipment_models_post_request_managed_equipment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


