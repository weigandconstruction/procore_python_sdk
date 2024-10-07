# CompanyUserBodyBulkRemove


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[CompanyUsersBulkRemoveInner]**](CompanyUsersBulkRemoveInner.md) | Array of existing company users with a project id that they will be removed from. The maximum amount per request is 1000 user_id, project_id duplets. If more than 1000 objects are sent then a worker will be triggered to perform the action asynchronously. | 

## Example

```python
from procore_sdk.models.company_user_body_bulk_remove import CompanyUserBodyBulkRemove

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUserBodyBulkRemove from a JSON string
company_user_body_bulk_remove_instance = CompanyUserBodyBulkRemove.from_json(json)
# print the JSON string representation of the object
print(CompanyUserBodyBulkRemove.to_json())

# convert the object into a dict
company_user_body_bulk_remove_dict = company_user_body_bulk_remove_instance.to_dict()
# create an instance of CompanyUserBodyBulkRemove from a dict
company_user_body_bulk_remove_from_dict = CompanyUserBodyBulkRemove.from_dict(company_user_body_bulk_remove_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


