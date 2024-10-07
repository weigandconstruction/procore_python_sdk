# RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the project. | [optional] 
**name** | **str** | Project Display Name (could include Project Number) | [optional] 
**assigned** | **bool** | Indicates whether the configurable field set is assigned to the project | [optional] 
**configurable_field_set_name** | **str** | Configurable Field Set Name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_id_project_options_get200_response_inner import RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_configurable_field_sets_id_project_options_get200_response_inner_instance = RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_configurable_field_sets_id_project_options_get200_response_inner_dict = rest_v10_companies_company_id_configurable_field_sets_id_project_options_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner from a dict
rest_v10_companies_company_id_configurable_field_sets_id_project_options_get200_response_inner_from_dict = RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner.from_dict(rest_v10_companies_company_id_configurable_field_sets_id_project_options_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


