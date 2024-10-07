# RestV10CompanyConfigurationGet200ResponseRoundingConfiguration

Rounding Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | **str** | Rounding Rule | [optional] 
**time_increment** | **int** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_company_configuration_get200_response_rounding_configuration import RestV10CompanyConfigurationGet200ResponseRoundingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompanyConfigurationGet200ResponseRoundingConfiguration from a JSON string
rest_v10_company_configuration_get200_response_rounding_configuration_instance = RestV10CompanyConfigurationGet200ResponseRoundingConfiguration.from_json(json)
# print the JSON string representation of the object
print(RestV10CompanyConfigurationGet200ResponseRoundingConfiguration.to_json())

# convert the object into a dict
rest_v10_company_configuration_get200_response_rounding_configuration_dict = rest_v10_company_configuration_get200_response_rounding_configuration_instance.to_dict()
# create an instance of RestV10CompanyConfigurationGet200ResponseRoundingConfiguration from a dict
rest_v10_company_configuration_get200_response_rounding_configuration_from_dict = RestV10CompanyConfigurationGet200ResponseRoundingConfiguration.from_dict(rest_v10_company_configuration_get200_response_rounding_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


