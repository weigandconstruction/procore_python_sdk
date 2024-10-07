# RestV10CompaniesCompanyIdGenericToolsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the generic tool. | [optional] 
**domain_id** | **int** | Unique identifier for the generic tool domain. | [optional] 
**title** | **str** | Primary name/title for the generic tool. | [optional] 
**abbreviation** | **str** | Abbreviation for the Title. Will be used as a prefix for the Generic Tool Item number. | [optional] 
**private_by_default** | **bool** | If true, items created in the tool are private by default. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_generic_tools_get200_response_inner import RestV10CompaniesCompanyIdGenericToolsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdGenericToolsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_generic_tools_get200_response_inner_instance = RestV10CompaniesCompanyIdGenericToolsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdGenericToolsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_generic_tools_get200_response_inner_dict = rest_v10_companies_company_id_generic_tools_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdGenericToolsGet200ResponseInner from a dict
rest_v10_companies_company_id_generic_tools_get200_response_inner_from_dict = RestV10CompaniesCompanyIdGenericToolsGet200ResponseInner.from_dict(rest_v10_companies_company_id_generic_tools_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


