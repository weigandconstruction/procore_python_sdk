# RestV10ToolsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Tool | [optional] 
**engine_name** | **str** | The name of the Tool engine | [optional] 
**is_active** | **bool** | Indicates whether the tool is currently active | [optional] 
**position** | **int** | The ordering position of the Tool | [optional] 
**required** | **bool** | Indicates whether the tool must be active | [optional] 
**user_access_level** | **str** | The user access level | [optional] 
**provider_id** | **int** | The Provider id | [optional] 
**provider_type** | **str** | The Provider type | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_tools_get200_response_inner import RestV10ToolsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ToolsGet200ResponseInner from a JSON string
rest_v10_tools_get200_response_inner_instance = RestV10ToolsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ToolsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_tools_get200_response_inner_dict = rest_v10_tools_get200_response_inner_instance.to_dict()
# create an instance of RestV10ToolsGet200ResponseInner from a dict
rest_v10_tools_get200_response_inner_from_dict = RestV10ToolsGet200ResponseInner.from_dict(rest_v10_tools_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


