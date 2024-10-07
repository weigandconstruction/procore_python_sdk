# RestV10TasksSyncPatchRequestUpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Task name. | [optional] 
**start** | **datetime** | Task start timestamp. | [optional] 
**finish** | **datetime** | Task finish timestamp. | [optional] 
**actual_start** | **datetime** | Actual start timestamp for this task. | [optional] 
**actual_finish** | **datetime** | Actual finish timestamp for this task. | [optional] 
**percentage** | **int** | Percent complete value for this task. | [optional] 
**critical_path** | **bool** | True if this task is on the critical path. | [optional] 
**milestone** | **bool** | True if this task is a milestone. | [optional] 
**row_number** | **int** | The row number of a task defines the sequence in which tasks are normally expected to be displayed. | [optional] 
**has_children** | **bool** | Flag set to true if this is a summary task, i.e. this task has child tasks. | [optional] 
**source_uid** | **str** | The unique identifier for this task from the external system which owns the schedule data. | [optional] 
**parent_id** | **int** | ID of the parent task. | [optional] 
**full_outline_path** | **str** | Task full outline path. | [optional] 
**activity_id** | **str** | For tasks imported from external systems which have the concept of an \&quot;Activity ID\&quot; (for example Primavera P6), this attribute is used to hold the Activity ID value. Note that due to an oversight during the creation of this API, the value supplied here will be rendered as the &#x60;schedule_activity_id&#x60; attribute in the response body. This will be corrected in a later version of the API. | [optional] 
**wbs** | **str** | Work Breakdown Structure (WBS) number for this task. | [optional] 
**schedule_duration** | **float** | The duration of this task in days as defined by the external system which owns the schedule data. | [optional] 
**resource_ids** | **List[int]** | Resources assigned to this task, represented as an array of resource ID values. | [optional] 
**notes** | **str** | Arbitrary notes about this task. | [optional] 
**baseline_start** | **datetime** | The baseline start timestamp for this task. | [optional] 
**baseline_finish** | **datetime** | The baseline finish timestamp for this task. | [optional] 
**start_variance** | **float** | The start variance in days for this task, as calculated by the external system which owns the schedule data. | [optional] 
**finish_variance** | **float** | The finish variance in days for this task, as calculated by the external system which owns the schedule data. | [optional] 
**manually_edited** | **bool** | Set to true if the task has been created or modified in Procore, false if the task was imported from an external schedule and has not been modified in Procore. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_tasks_sync_patch_request_updates_inner import RestV10TasksSyncPatchRequestUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TasksSyncPatchRequestUpdatesInner from a JSON string
rest_v10_tasks_sync_patch_request_updates_inner_instance = RestV10TasksSyncPatchRequestUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10TasksSyncPatchRequestUpdatesInner.to_json())

# convert the object into a dict
rest_v10_tasks_sync_patch_request_updates_inner_dict = rest_v10_tasks_sync_patch_request_updates_inner_instance.to_dict()
# create an instance of RestV10TasksSyncPatchRequestUpdatesInner from a dict
rest_v10_tasks_sync_patch_request_updates_inner_from_dict = RestV10TasksSyncPatchRequestUpdatesInner.from_dict(rest_v10_tasks_sync_patch_request_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


