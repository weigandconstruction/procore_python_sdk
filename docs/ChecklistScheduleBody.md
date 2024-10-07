# ChecklistScheduleBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**ChecklistSchedule1**](ChecklistSchedule1.md) |  | 

## Example

```python
from procore_sdk.models.checklist_schedule_body import ChecklistScheduleBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistScheduleBody from a JSON string
checklist_schedule_body_instance = ChecklistScheduleBody.from_json(json)
# print the JSON string representation of the object
print(ChecklistScheduleBody.to_json())

# convert the object into a dict
checklist_schedule_body_dict = checklist_schedule_body_instance.to_dict()
# create an instance of ChecklistScheduleBody from a dict
checklist_schedule_body_from_dict = ChecklistScheduleBody.from_dict(checklist_schedule_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


