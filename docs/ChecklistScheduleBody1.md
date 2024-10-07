# ChecklistScheduleBody1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**ChecklistSchedule2**](ChecklistSchedule2.md) |  | 

## Example

```python
from procore_sdk.models.checklist_schedule_body1 import ChecklistScheduleBody1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistScheduleBody1 from a JSON string
checklist_schedule_body1_instance = ChecklistScheduleBody1.from_json(json)
# print the JSON string representation of the object
print(ChecklistScheduleBody1.to_json())

# convert the object into a dict
checklist_schedule_body1_dict = checklist_schedule_body1_instance.to_dict()
# create an instance of ChecklistScheduleBody1 from a dict
checklist_schedule_body1_from_dict = ChecklistScheduleBody1.from_dict(checklist_schedule_body1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


