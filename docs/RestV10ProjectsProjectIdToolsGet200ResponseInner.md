# RestV10ProjectsProjectIdToolsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Tool | [optional] 
**engine_name** | **str** | The name of the Tool engine | [optional] 
**is_active** | **bool** | Indicates whether the tool is currently active | [optional] 
**position** | **int** | The ordering position of the Tool | [optional] 
**required** | **bool** | Indicates whether the tool must be active | [optional] 
**title** | **str** | A display name for the tool | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_tools_get200_response_inner import RestV10ProjectsProjectIdToolsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdToolsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_tools_get200_response_inner_instance = RestV10ProjectsProjectIdToolsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdToolsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_tools_get200_response_inner_dict = rest_v10_projects_project_id_tools_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdToolsGet200ResponseInner from a dict
rest_v10_projects_project_id_tools_get200_response_inner_from_dict = RestV10ProjectsProjectIdToolsGet200ResponseInner.from_dict(rest_v10_projects_project_id_tools_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


