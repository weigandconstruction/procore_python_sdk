# RestV10CompaniesCompanyIdConciergePatchRequestConcierge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_initial_projects** | **int** | Estimated number of projects in first three months | [optional] 
**estimated_initial_users** | **int** | Estimated number of staff users in first three months | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_concierge_patch_request_concierge import RestV10CompaniesCompanyIdConciergePatchRequestConcierge

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdConciergePatchRequestConcierge from a JSON string
rest_v10_companies_company_id_concierge_patch_request_concierge_instance = RestV10CompaniesCompanyIdConciergePatchRequestConcierge.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdConciergePatchRequestConcierge.to_json())

# convert the object into a dict
rest_v10_companies_company_id_concierge_patch_request_concierge_dict = rest_v10_companies_company_id_concierge_patch_request_concierge_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdConciergePatchRequestConcierge from a dict
rest_v10_companies_company_id_concierge_patch_request_concierge_from_dict = RestV10CompaniesCompanyIdConciergePatchRequestConcierge.from_dict(rest_v10_companies_company_id_concierge_patch_request_concierge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


