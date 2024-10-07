# LookaheadTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lookahead_id** | **int** | ID of the associated Lookahead | 
**parent_id** | **int** | ID of the parent Lookahead Task | 
**name** | **str** | The name of the Task | 
**start_date** | **str** | Task start date, in project time zone | [optional] 
**end_date** | **str** | Task end date, in project time zone | [optional] 
**resource_ids** | **List[int]** | ID of Resource(s) to assign to this Lookahead Task | [optional] 
**comment** | **str** | Additional comments | [optional] 
**segments** | [**List[RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerSegmentsInner]**](RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerSegmentsInner.md) |  | [optional] 
**assignee_ids** | **List[int]** | ID of Contact(s) to assign to this Lookahead Task | [optional] 
**vendor_ids** | **List[int]** | ID of Company(s) to assign to this Lookahead Task | [optional] 

## Example

```python
from procore_sdk.models.lookahead_task import LookaheadTask

# TODO update the JSON string below
json = "{}"
# create an instance of LookaheadTask from a JSON string
lookahead_task_instance = LookaheadTask.from_json(json)
# print the JSON string representation of the object
print(LookaheadTask.to_json())

# convert the object into a dict
lookahead_task_dict = lookahead_task_instance.to_dict()
# create an instance of LookaheadTask from a dict
lookahead_task_from_dict = LookaheadTask.from_dict(lookahead_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


