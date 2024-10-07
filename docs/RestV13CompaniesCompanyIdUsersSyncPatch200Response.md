# RestV13CompaniesCompanyIdUsersSyncPatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[CompanyUser2]**](CompanyUser2.md) | Array of updated entities | [optional] 
**errors** | [**List[RestV13CompaniesCompanyIdUsersSyncPatch200ResponseErrorsInner]**](RestV13CompaniesCompanyIdUsersSyncPatch200ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v13_companies_company_id_users_sync_patch200_response import RestV13CompaniesCompanyIdUsersSyncPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV13CompaniesCompanyIdUsersSyncPatch200Response from a JSON string
rest_v13_companies_company_id_users_sync_patch200_response_instance = RestV13CompaniesCompanyIdUsersSyncPatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV13CompaniesCompanyIdUsersSyncPatch200Response.to_json())

# convert the object into a dict
rest_v13_companies_company_id_users_sync_patch200_response_dict = rest_v13_companies_company_id_users_sync_patch200_response_instance.to_dict()
# create an instance of RestV13CompaniesCompanyIdUsersSyncPatch200Response from a dict
rest_v13_companies_company_id_users_sync_patch200_response_from_dict = RestV13CompaniesCompanyIdUsersSyncPatch200Response.from_dict(rest_v13_companies_company_id_users_sync_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


