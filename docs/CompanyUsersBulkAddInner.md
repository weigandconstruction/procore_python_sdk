# CompanyUsersBulkAddInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **float** | The ID of the user to add | [optional] 
**project_id** | **float** | The ID of project to add the user to | [optional] 
**permission_template_id** | **float** | The ID of the permission template to assign to the user | [optional] 

## Example

```python
from procore_sdk.models.company_users_bulk_add_inner import CompanyUsersBulkAddInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUsersBulkAddInner from a JSON string
company_users_bulk_add_inner_instance = CompanyUsersBulkAddInner.from_json(json)
# print the JSON string representation of the object
print(CompanyUsersBulkAddInner.to_json())

# convert the object into a dict
company_users_bulk_add_inner_dict = company_users_bulk_add_inner_instance.to_dict()
# create an instance of CompanyUsersBulkAddInner from a dict
company_users_bulk_add_inner_from_dict = CompanyUsersBulkAddInner.from_dict(company_users_bulk_add_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


