# RestV13CompaniesCompanyIdUsersBulkRemovePost200ResponseUserId

One key for each project ID for that nested user ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Success if the user ID / project ID combination succeeded, failure if not | [optional] 

## Example

```python
from procore_sdk.models.rest_v13_companies_company_id_users_bulk_remove_post200_response_user_id import RestV13CompaniesCompanyIdUsersBulkRemovePost200ResponseUserId

# TODO update the JSON string below
json = "{}"
# create an instance of RestV13CompaniesCompanyIdUsersBulkRemovePost200ResponseUserId from a JSON string
rest_v13_companies_company_id_users_bulk_remove_post200_response_user_id_instance = RestV13CompaniesCompanyIdUsersBulkRemovePost200ResponseUserId.from_json(json)
# print the JSON string representation of the object
print(RestV13CompaniesCompanyIdUsersBulkRemovePost200ResponseUserId.to_json())

# convert the object into a dict
rest_v13_companies_company_id_users_bulk_remove_post200_response_user_id_dict = rest_v13_companies_company_id_users_bulk_remove_post200_response_user_id_instance.to_dict()
# create an instance of RestV13CompaniesCompanyIdUsersBulkRemovePost200ResponseUserId from a dict
rest_v13_companies_company_id_users_bulk_remove_post200_response_user_id_from_dict = RestV13CompaniesCompanyIdUsersBulkRemovePost200ResponseUserId.from_dict(rest_v13_companies_company_id_users_bulk_remove_post200_response_user_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


