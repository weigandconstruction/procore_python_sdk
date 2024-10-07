# RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig

Time and Materials Company Config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**materials_enabled** | **bool** |  | [optional] 
**labor_enabled** | **bool** |  | [optional] 
**equipment_enabled** | **bool** |  | [optional] 
**subcontractors_enabled** | **bool** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_company_configuration_get200_response_time_and_materials_company_config import RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig from a JSON string
rest_v10_company_configuration_get200_response_time_and_materials_company_config_instance = RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig.from_json(json)
# print the JSON string representation of the object
print(RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig.to_json())

# convert the object into a dict
rest_v10_company_configuration_get200_response_time_and_materials_company_config_dict = rest_v10_company_configuration_get200_response_time_and_materials_company_config_instance.to_dict()
# create an instance of RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig from a dict
rest_v10_company_configuration_get200_response_time_and_materials_company_config_from_dict = RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig.from_dict(rest_v10_company_configuration_get200_response_time_and_materials_company_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


