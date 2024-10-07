# RestV10TodosSyncPatchRequestUpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the ToDo item to update | [optional] 
**assignment_id** | **int** | The ID of the Assignment of the ToDo | [optional] 
**color** | **str** | The Color of the ToDo | [optional] 
**finish_datetime** | **datetime** | The Finish date-time of the ToDo | [optional] 
**name** | **str** | The Name of the ToDo | [optional] 
**description** | **str** | The Description of the ToDo | [optional] 
**percentage** | **int** | The Percentage of the ToDo | [optional] 
**private** | **bool** | The Private status of the ToDo | [optional] 
**start_datetime** | **datetime** | The Start date-time of the ToDo | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_todos_sync_patch_request_updates_inner import RestV10TodosSyncPatchRequestUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TodosSyncPatchRequestUpdatesInner from a JSON string
rest_v10_todos_sync_patch_request_updates_inner_instance = RestV10TodosSyncPatchRequestUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10TodosSyncPatchRequestUpdatesInner.to_json())

# convert the object into a dict
rest_v10_todos_sync_patch_request_updates_inner_dict = rest_v10_todos_sync_patch_request_updates_inner_instance.to_dict()
# create an instance of RestV10TodosSyncPatchRequestUpdatesInner from a dict
rest_v10_todos_sync_patch_request_updates_inner_from_dict = RestV10TodosSyncPatchRequestUpdatesInner.from_dict(rest_v10_todos_sync_patch_request_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


