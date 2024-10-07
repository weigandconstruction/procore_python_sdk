# RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | True &#x3D; attributes is valid, errors is empty, False &#x3D; invalid, errors not empty | [optional] 
**errors** | [**RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200ResponseErrors**](RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200ResponseErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response import RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200Response from a JSON string
rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response_instance = RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response_dict = rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200Response from a dict
rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response_from_dict = RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200Response.from_dict(rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


