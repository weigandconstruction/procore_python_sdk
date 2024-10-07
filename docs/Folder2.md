# Folder2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Folder id | [optional] 
**name** | **str** | Folder name | [optional] 
**name_with_path** | **str** | Full file path with folder name | [optional] 

## Example

```python
from procore_sdk.models.folder2 import Folder2

# TODO update the JSON string below
json = "{}"
# create an instance of Folder2 from a JSON string
folder2_instance = Folder2.from_json(json)
# print the JSON string representation of the object
print(Folder2.to_json())

# convert the object into a dict
folder2_dict = folder2_instance.to_dict()
# create an instance of Folder2 from a dict
folder2_from_dict = Folder2.from_dict(folder2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


