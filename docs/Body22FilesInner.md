# Body22FilesInner

File associated with the requisition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of file | 
**id** | **int** | Unique identifier for the file. | 
**url** | **str** | Url of the file | [optional] 

## Example

```python
from procore_sdk.models.body22_files_inner import Body22FilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body22FilesInner from a JSON string
body22_files_inner_instance = Body22FilesInner.from_json(json)
# print the JSON string representation of the object
print(Body22FilesInner.to_json())

# convert the object into a dict
body22_files_inner_dict = body22_files_inner_instance.to_dict()
# create an instance of Body22FilesInner from a dict
body22_files_inner_from_dict = Body22FilesInner.from_dict(body22_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


