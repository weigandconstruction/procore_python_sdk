# RestV13CompaniesCompanyIdUsersBulkRemovePost200Response

One key for each user ID passed in

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | [**RestV13CompaniesCompanyIdUsersBulkRemovePost200ResponseUserId**](RestV13CompaniesCompanyIdUsersBulkRemovePost200ResponseUserId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v13_companies_company_id_users_bulk_remove_post200_response import RestV13CompaniesCompanyIdUsersBulkRemovePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV13CompaniesCompanyIdUsersBulkRemovePost200Response from a JSON string
rest_v13_companies_company_id_users_bulk_remove_post200_response_instance = RestV13CompaniesCompanyIdUsersBulkRemovePost200Response.from_json(json)
# print the JSON string representation of the object
print(RestV13CompaniesCompanyIdUsersBulkRemovePost200Response.to_json())

# convert the object into a dict
rest_v13_companies_company_id_users_bulk_remove_post200_response_dict = rest_v13_companies_company_id_users_bulk_remove_post200_response_instance.to_dict()
# create an instance of RestV13CompaniesCompanyIdUsersBulkRemovePost200Response from a dict
rest_v13_companies_company_id_users_bulk_remove_post200_response_from_dict = RestV13CompaniesCompanyIdUsersBulkRemovePost200Response.from_dict(rest_v13_companies_company_id_users_bulk_remove_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


