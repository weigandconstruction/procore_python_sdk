# RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200ResponseErrors

Errors on fields, empty object if valid is true

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_47393** | **List[str]** | An array of validation failure messages. | [optional] 
**custom_field_58238** | **List[str]** | An array of validation failure messages. | [optional] 
**number** | **List[str]** | An array of validation failure messages. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response_errors import RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200ResponseErrors

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200ResponseErrors from a JSON string
rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response_errors_instance = RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200ResponseErrors.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200ResponseErrors.to_json())

# convert the object into a dict
rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response_errors_dict = rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response_errors_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200ResponseErrors from a dict
rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response_errors_from_dict = RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200ResponseErrors.from_dict(rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


