# Body124BimViewFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of view folder | 
**parent_id** | **int** | Id of parent BimViewFolder | [optional] 
**bim_file_id** | **int** | Id of BimFile to associate | 

## Example

```python
from procore_sdk.models.body124_bim_view_folder import Body124BimViewFolder

# TODO update the JSON string below
json = "{}"
# create an instance of Body124BimViewFolder from a JSON string
body124_bim_view_folder_instance = Body124BimViewFolder.from_json(json)
# print the JSON string representation of the object
print(Body124BimViewFolder.to_json())

# convert the object into a dict
body124_bim_view_folder_dict = body124_bim_view_folder_instance.to_dict()
# create an instance of Body124BimViewFolder from a dict
body124_bim_view_folder_from_dict = Body124BimViewFolder.from_dict(body124_bim_view_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


