# BIMFile

BIM File Item object. Each BIM File can be uniquely identified by name and UUID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the file to be associated a project. | 
**uuid** | **str** | UUID associated with the file | 

## Example

```python
from procore_sdk.models.bim_file import BIMFile

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFile from a JSON string
bim_file_instance = BIMFile.from_json(json)
# print the JSON string representation of the object
print(BIMFile.to_json())

# convert the object into a dict
bim_file_dict = bim_file_instance.to_dict()
# create an instance of BIMFile from a dict
bim_file_from_dict = BIMFile.from_dict(bim_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


