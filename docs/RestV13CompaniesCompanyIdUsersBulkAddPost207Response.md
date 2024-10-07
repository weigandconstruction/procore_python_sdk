# RestV13CompaniesCompanyIdUsersBulkAddPost207Response

entities with successes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | **Dict[Dict[str, object]]** | One key for each user ID passed in, with an array of project IDs for that nested user ID | [optional] 
**errors** | **Dict[Dict[str, object]]** | One key for each user ID passed in, with an array of project IDs for that nested user ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v13_companies_company_id_users_bulk_add_post207_response import RestV13CompaniesCompanyIdUsersBulkAddPost207Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV13CompaniesCompanyIdUsersBulkAddPost207Response from a JSON string
rest_v13_companies_company_id_users_bulk_add_post207_response_instance = RestV13CompaniesCompanyIdUsersBulkAddPost207Response.from_json(json)
# print the JSON string representation of the object
print(RestV13CompaniesCompanyIdUsersBulkAddPost207Response.to_json())

# convert the object into a dict
rest_v13_companies_company_id_users_bulk_add_post207_response_dict = rest_v13_companies_company_id_users_bulk_add_post207_response_instance.to_dict()
# create an instance of RestV13CompaniesCompanyIdUsersBulkAddPost207Response from a dict
rest_v13_companies_company_id_users_bulk_add_post207_response_from_dict = RestV13CompaniesCompanyIdUsersBulkAddPost207Response.from_dict(rest_v13_companies_company_id_users_bulk_add_post207_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


