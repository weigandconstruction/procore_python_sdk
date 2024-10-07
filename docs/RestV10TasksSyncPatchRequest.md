# RestV10TasksSyncPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Tasks belongs to | 
**updates** | [**List[RestV10TasksSyncPatchRequestUpdatesInner]**](RestV10TasksSyncPatchRequestUpdatesInner.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_tasks_sync_patch_request import RestV10TasksSyncPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TasksSyncPatchRequest from a JSON string
rest_v10_tasks_sync_patch_request_instance = RestV10TasksSyncPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10TasksSyncPatchRequest.to_json())

# convert the object into a dict
rest_v10_tasks_sync_patch_request_dict = rest_v10_tasks_sync_patch_request_instance.to_dict()
# create an instance of RestV10TasksSyncPatchRequest from a dict
rest_v10_tasks_sync_patch_request_from_dict = RestV10TasksSyncPatchRequest.from_dict(rest_v10_tasks_sync_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


