# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for this task. | [optional] 
**name** | **str** | Task name as the user sees it in Procore. Depending on the project settings this may include the full outline path | [optional] 
**task_name** | **str** | Task name. This will always contain just the task name, and will not include the full outline path. | [optional] 
**key** | **str** | A deprecated value which was originally used to uniquely identify tasks. This value will be removed in a later version of the API. | [optional] 
**start_datetime** | **datetime** | Task start timestamp in ISO 8601 UTC format. | [optional] 
**finish_datetime** | **datetime** | Task finish timestamp in ISO 8601 UTC format. | [optional] 
**percentage** | **int** | Percent complete value for this task. | [optional] 
**color** | **str** | The RGB color value, expressed in hex digits for the color used when displaying the task in Procore. The color varies depending on whether the task is on the critical path, complete, unstarted or in progress. | [optional] 
**parent_id** | **int** | ID of the parent task. | [optional] 
**pending** | **bool** | True if one or more change requests are pending for this task. | [optional] 
**activity_id** | **str** | The external unique identifier for this task. Note that due to an oversight in the original API, the value returned for this attribute will be the &#x60;source_uid&#x60; value supplied when creating a task. | [optional] 
**schedule_activity_id** | **str** | For tasks imported from external systems which have the concept of an \&quot;Activity ID\&quot; (for example Primavera P6), this attribute is used to hold the Activity ID value. Note that due to an oversight during the creation of this API, this is the value supplied in the &#x60;activity_id&#x60; attribute. This will be corrected in a later version of the API. | [optional] 
**resource_name** | **str** | Names of any resources assigned to this task. | [optional] 
**critical_path** | **bool** | True if this task is on the critical path. | [optional] 
**milestone** | **bool** | True if this task is a milestone. | [optional] 
**actual_start** | **datetime** | Actual start timestamp for this task in ISO 8601 UTC format. | [optional] 
**actual_finish** | **datetime** | Actual finish timestamp for this task in ISO 8601 UTC format. | [optional] 
**row_number** | **int** | The row number of a task defines the sequence in which tasks are normally expected to be displayed. | [optional] 
**has_children** | **bool** | True if this is a summary task, i.e. this task has child tasks. | [optional] 
**full_outline_path** | **str** | Task full outline path | [optional] 
**source_uid** | **str** | The unique identifier for this task from the external system which owns the schedule data. | [optional] 
**wbs** | **str** | Work Breakdown Structure (WBS) number for this task. | [optional] 
**schedule_duration** | **float** | The duration of this task in days as defined by the external system which owns the schedule data. | [optional] 
**resource_ids** | **List[int]** | The resources assigned to this task, represented as an array of resource ID values. | [optional] 
**notes** | **str** | Arbitrary notes about this task. | [optional] 
**baseline_start** | **datetime** | The baseline start timestamp for this task in ISO 8601 UTC format. | [optional] 
**baseline_finish** | **datetime** | The baseline finish timestamp for this task in ISO 8601 UTC format. | [optional] 
**start_variance** | **float** | The start variance in days for this task. | [optional] 
**finish_variance** | **float** | The finish variance in days for this task. | [optional] 
**manually_edited** | **bool** | Set to true if the task has been created or modified in Procore, false if the task was imported from an external schedule and has not been modified in Procore. | [optional] 
**created_at** | **datetime** | Date/time the Task was created in ISO 8601 UTC format. | [optional] 
**updated_at** | **datetime** | Date/time the Task was last updated in ISO 8601 UTC format. | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**updated_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


