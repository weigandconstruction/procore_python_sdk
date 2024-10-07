# RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Permission Template | [optional] 
**name** | **str** | The name of the Permission Template | [optional] 
**project_specific** | **bool** | If the Permission Template is project specific | [optional] 
**type** | **str** | Permission Template type | [optional] [default to 'global']

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_permission_templates_get200_response_inner import RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_permission_templates_get200_response_inner_instance = RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_permission_templates_get200_response_inner_dict = rest_v10_projects_project_id_permission_templates_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner from a dict
rest_v10_projects_project_id_permission_templates_get200_response_inner_from_dict = RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner.from_dict(rest_v10_projects_project_id_permission_templates_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


