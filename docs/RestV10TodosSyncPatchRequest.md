# RestV10TodosSyncPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[RestV10TodosSyncPatchRequestUpdatesInner]**](RestV10TodosSyncPatchRequestUpdatesInner.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_todos_sync_patch_request import RestV10TodosSyncPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TodosSyncPatchRequest from a JSON string
rest_v10_todos_sync_patch_request_instance = RestV10TodosSyncPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10TodosSyncPatchRequest.to_json())

# convert the object into a dict
rest_v10_todos_sync_patch_request_dict = rest_v10_todos_sync_patch_request_instance.to_dict()
# create an instance of RestV10TodosSyncPatchRequest from a dict
rest_v10_todos_sync_patch_request_from_dict = RestV10TodosSyncPatchRequest.from_dict(rest_v10_todos_sync_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


