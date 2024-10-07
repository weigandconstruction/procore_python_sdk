# SubJobSyncBodyUpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | unique identifier | [optional] 
**name** | **str** | Name | [optional] 
**code** | **str** | Unique code in the scope of a Project | [optional] 
**origin_id** | **str** | The Third-party unique identifier of the Sub Job | [optional] 
**origin_data** | **str** | The Third-party Data of the Sub Job | [optional] 

## Example

```python
from procore_sdk.models.sub_job_sync_body_updates_inner import SubJobSyncBodyUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubJobSyncBodyUpdatesInner from a JSON string
sub_job_sync_body_updates_inner_instance = SubJobSyncBodyUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(SubJobSyncBodyUpdatesInner.to_json())

# convert the object into a dict
sub_job_sync_body_updates_inner_dict = sub_job_sync_body_updates_inner_instance.to_dict()
# create an instance of SubJobSyncBodyUpdatesInner from a dict
sub_job_sync_body_updates_inner_from_dict = SubJobSyncBodyUpdatesInner.from_dict(sub_job_sync_body_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


