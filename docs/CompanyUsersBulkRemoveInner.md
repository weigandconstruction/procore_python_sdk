# CompanyUsersBulkRemoveInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **float** | The ID of the user to remove | [optional] 
**project_id** | **float** | The ID of project to add the user to remove from | [optional] 

## Example

```python
from procore_sdk.models.company_users_bulk_remove_inner import CompanyUsersBulkRemoveInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUsersBulkRemoveInner from a JSON string
company_users_bulk_remove_inner_instance = CompanyUsersBulkRemoveInner.from_json(json)
# print the JSON string representation of the object
print(CompanyUsersBulkRemoveInner.to_json())

# convert the object into a dict
company_users_bulk_remove_inner_dict = company_users_bulk_remove_inner_instance.to_dict()
# create an instance of CompanyUsersBulkRemoveInner from a dict
company_users_bulk_remove_inner_from_dict = CompanyUsersBulkRemoveInner.from_dict(company_users_bulk_remove_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


