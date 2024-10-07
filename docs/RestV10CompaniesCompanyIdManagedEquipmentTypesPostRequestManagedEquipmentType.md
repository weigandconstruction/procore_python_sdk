# RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the equipment Type | 
**managed_equipment_category_id** | **int** | Equipment category ID the type is associated to | 
**is_active** | **bool** | If the equipment model is active | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_types_post_request_managed_equipment_type import RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType from a JSON string
rest_v10_companies_company_id_managed_equipment_types_post_request_managed_equipment_type_instance = RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType.to_json())

# convert the object into a dict
rest_v10_companies_company_id_managed_equipment_types_post_request_managed_equipment_type_dict = rest_v10_companies_company_id_managed_equipment_types_post_request_managed_equipment_type_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType from a dict
rest_v10_companies_company_id_managed_equipment_types_post_request_managed_equipment_type_from_dict = RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType.from_dict(rest_v10_companies_company_id_managed_equipment_types_post_request_managed_equipment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


