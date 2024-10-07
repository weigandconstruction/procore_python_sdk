# ChecklistScheduleChangeHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**column** | **str** | Name of the column changed | [optional] 
**old_value** | **str** | Value of the column before change | [optional] 
**new_value** | **str** | Value of the column after change | [optional] 
**created_by_id** | **int** | The ID of the user | [optional] 
**created_at** | **datetime** | Created date | [optional] 

## Example

```python
from procore_sdk.models.checklist_schedule_change_history import ChecklistScheduleChangeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistScheduleChangeHistory from a JSON string
checklist_schedule_change_history_instance = ChecklistScheduleChangeHistory.from_json(json)
# print the JSON string representation of the object
print(ChecklistScheduleChangeHistory.to_json())

# convert the object into a dict
checklist_schedule_change_history_dict = checklist_schedule_change_history_instance.to_dict()
# create an instance of ChecklistScheduleChangeHistory from a dict
checklist_schedule_change_history_from_dict = ChecklistScheduleChangeHistory.from_dict(checklist_schedule_change_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


