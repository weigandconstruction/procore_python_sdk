# Body59BimViewFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **List[str]** |  | 
**bim_file_id** | **int** | Id of BimFile to associate | 

## Example

```python
from procore_sdk.models.body59_bim_view_folder import Body59BimViewFolder

# TODO update the JSON string below
json = "{}"
# create an instance of Body59BimViewFolder from a JSON string
body59_bim_view_folder_instance = Body59BimViewFolder.from_json(json)
# print the JSON string representation of the object
print(Body59BimViewFolder.to_json())

# convert the object into a dict
body59_bim_view_folder_dict = body59_bim_view_folder_instance.to_dict()
# create an instance of Body59BimViewFolder from a dict
body59_bim_view_folder_from_dict = Body59BimViewFolder.from_dict(body59_bim_view_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


