# RestV10CompaniesCompanyIdConfigurableFieldSetsIdDuplicatePost400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | True &#x3D; attributes is valid, errors is empty, False &#x3D; invalid, errors not empty | [optional] 
**errors** | **str** | Errors on fields, empty object if valid is true | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post400_response import RestV10CompaniesCompanyIdConfigurableFieldSetsIdDuplicatePost400Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdDuplicatePost400Response from a JSON string
rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post400_response_instance = RestV10CompaniesCompanyIdConfigurableFieldSetsIdDuplicatePost400Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdConfigurableFieldSetsIdDuplicatePost400Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post400_response_dict = rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post400_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdDuplicatePost400Response from a dict
rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post400_response_from_dict = RestV10CompaniesCompanyIdConfigurableFieldSetsIdDuplicatePost400Response.from_dict(rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


