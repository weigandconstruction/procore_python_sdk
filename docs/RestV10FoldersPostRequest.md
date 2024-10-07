# RestV10FoldersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | [**RestV10FoldersPostRequestFolder**](RestV10FoldersPostRequestFolder.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_folders_post_request import RestV10FoldersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10FoldersPostRequest from a JSON string
rest_v10_folders_post_request_instance = RestV10FoldersPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10FoldersPostRequest.to_json())

# convert the object into a dict
rest_v10_folders_post_request_dict = rest_v10_folders_post_request_instance.to_dict()
# create an instance of RestV10FoldersPostRequest from a dict
rest_v10_folders_post_request_from_dict = RestV10FoldersPostRequest.from_dict(rest_v10_folders_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


