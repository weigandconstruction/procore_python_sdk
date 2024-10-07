# RestV10CompaniesCompanyIdFiltersGet200ResponseFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Filter index | [optional] 
**key** | **str** | Filter key | [optional] 
**endpoint** | **str** | Filter endpoint | [optional] 
**value** | **str** | Filter value | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_filters_get200_response_filters_inner import RestV10CompaniesCompanyIdFiltersGet200ResponseFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdFiltersGet200ResponseFiltersInner from a JSON string
rest_v10_companies_company_id_filters_get200_response_filters_inner_instance = RestV10CompaniesCompanyIdFiltersGet200ResponseFiltersInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdFiltersGet200ResponseFiltersInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_filters_get200_response_filters_inner_dict = rest_v10_companies_company_id_filters_get200_response_filters_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdFiltersGet200ResponseFiltersInner from a dict
rest_v10_companies_company_id_filters_get200_response_filters_inner_from_dict = RestV10CompaniesCompanyIdFiltersGet200ResponseFiltersInner.from_dict(rest_v10_companies_company_id_filters_get200_response_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


