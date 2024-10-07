# RestV10NestedBimViewFoldersPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name of view folder | [optional] 
**parent_id** | **int** | Id of parent BimViewFolder | [optional] 
**bim_file_id** | **int** | Id of associated BimFile | [optional] 
**project_id** | **int** | Project Id | [optional] 
**created_by_id** | **int** | Id if creator | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_nested_bim_view_folders_post200_response import RestV10NestedBimViewFoldersPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10NestedBimViewFoldersPost200Response from a JSON string
rest_v10_nested_bim_view_folders_post200_response_instance = RestV10NestedBimViewFoldersPost200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10NestedBimViewFoldersPost200Response.to_json())

# convert the object into a dict
rest_v10_nested_bim_view_folders_post200_response_dict = rest_v10_nested_bim_view_folders_post200_response_instance.to_dict()
# create an instance of RestV10NestedBimViewFoldersPost200Response from a dict
rest_v10_nested_bim_view_folders_post200_response_from_dict = RestV10NestedBimViewFoldersPost200Response.from_dict(rest_v10_nested_bim_view_folders_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


