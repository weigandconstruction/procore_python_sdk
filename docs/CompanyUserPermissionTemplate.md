# CompanyUserPermissionTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the Permission Template | [optional] 
**name** | **str** | The name of the Permission Template | [optional] 
**project_specific** | **bool** | If the Permission Template is project specific | [optional] 
**type** | **str** | The type of the Permission Template | [optional] 

## Example

```python
from procore_sdk.models.company_user_permission_template import CompanyUserPermissionTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUserPermissionTemplate from a JSON string
company_user_permission_template_instance = CompanyUserPermissionTemplate.from_json(json)
# print the JSON string representation of the object
print(CompanyUserPermissionTemplate.to_json())

# convert the object into a dict
company_user_permission_template_dict = company_user_permission_template_instance.to_dict()
# create an instance of CompanyUserPermissionTemplate from a dict
company_user_permission_template_from_dict = CompanyUserPermissionTemplate.from_dict(company_user_permission_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


