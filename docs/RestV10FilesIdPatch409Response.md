# RestV10FilesIdPatch409Response

File Conflict Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**RestV10FilesIdPatch409ResponseErrors**](RestV10FilesIdPatch409ResponseErrors.md) |  | [optional] 
**error_type** | **str** |  | [optional] 
**file** | [**RestV10FilesIdPatch409ResponseFile**](RestV10FilesIdPatch409ResponseFile.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_files_id_patch409_response import RestV10FilesIdPatch409Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10FilesIdPatch409Response from a JSON string
rest_v10_files_id_patch409_response_instance = RestV10FilesIdPatch409Response.from_json(json)
# print the JSON string representation of the object
print(RestV10FilesIdPatch409Response.to_json())

# convert the object into a dict
rest_v10_files_id_patch409_response_dict = rest_v10_files_id_patch409_response_instance.to_dict()
# create an instance of RestV10FilesIdPatch409Response from a dict
rest_v10_files_id_patch409_response_from_dict = RestV10FilesIdPatch409Response.from_dict(rest_v10_files_id_patch409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


