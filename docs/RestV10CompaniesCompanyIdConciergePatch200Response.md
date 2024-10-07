# RestV10CompaniesCompanyIdConciergePatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**implementation_manager_origin_id** | **int** | ID for the IM in Liftoff | [optional] 
**estimated_initial_projects** | **int** | Estimates number of projects in first 3 month | [optional] 
**estimated_initial_users** | **int** | Estimates number of staff users in first 3 month | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_concierge_patch200_response import RestV10CompaniesCompanyIdConciergePatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdConciergePatch200Response from a JSON string
rest_v10_companies_company_id_concierge_patch200_response_instance = RestV10CompaniesCompanyIdConciergePatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdConciergePatch200Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_concierge_patch200_response_dict = rest_v10_companies_company_id_concierge_patch200_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdConciergePatch200Response from a dict
rest_v10_companies_company_id_concierge_patch200_response_from_dict = RestV10CompaniesCompanyIdConciergePatch200Response.from_dict(rest_v10_companies_company_id_concierge_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


