# RestV10ProjectsProjectIdToolsPatchRequestToolsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Tool | [optional] 
**is_active** | **bool** | Indicates whether the tool is currently active | [optional] 
**position** | **int** | The ordering position of the Tool | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_tools_patch_request_tools_inner import RestV10ProjectsProjectIdToolsPatchRequestToolsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdToolsPatchRequestToolsInner from a JSON string
rest_v10_projects_project_id_tools_patch_request_tools_inner_instance = RestV10ProjectsProjectIdToolsPatchRequestToolsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdToolsPatchRequestToolsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_tools_patch_request_tools_inner_dict = rest_v10_projects_project_id_tools_patch_request_tools_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdToolsPatchRequestToolsInner from a dict
rest_v10_projects_project_id_tools_patch_request_tools_inner_from_dict = RestV10ProjectsProjectIdToolsPatchRequestToolsInner.from_dict(rest_v10_projects_project_id_tools_patch_request_tools_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


