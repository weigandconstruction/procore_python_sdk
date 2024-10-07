# CompanyUserBodyBulkAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[CompanyUsersBulkAddInner]**](CompanyUsersBulkAddInner.md) | Array of existing company users with a permission template id and project id that they will be assinged to. The maximum amount per request is 1000 user_id, project_id, permission_template_id triplets. If more than 1000 objects are sent then a worker will be triggered to perform the action asynchronously. | 

## Example

```python
from procore_sdk.models.company_user_body_bulk_add import CompanyUserBodyBulkAdd

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUserBodyBulkAdd from a JSON string
company_user_body_bulk_add_instance = CompanyUserBodyBulkAdd.from_json(json)
# print the JSON string representation of the object
print(CompanyUserBodyBulkAdd.to_json())

# convert the object into a dict
company_user_body_bulk_add_dict = company_user_body_bulk_add_instance.to_dict()
# create an instance of CompanyUserBodyBulkAdd from a dict
company_user_body_bulk_add_from_dict = CompanyUserBodyBulkAdd.from_dict(company_user_body_bulk_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


