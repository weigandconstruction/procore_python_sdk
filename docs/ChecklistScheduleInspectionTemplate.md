# ChecklistScheduleInspectionTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**attachment_ids** | **List[int]** |  | [optional] 
**description** | **str** | Description | [optional] 
**inspection_type** | [**ChecklistScheduleInspectionTemplateInspectionType**](ChecklistScheduleInspectionTemplateInspectionType.md) |  | [optional] 
**name** | **str** | Name | [optional] 
**trade_id** | **int** | Trade ID | [optional] 

## Example

```python
from procore_sdk.models.checklist_schedule_inspection_template import ChecklistScheduleInspectionTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistScheduleInspectionTemplate from a JSON string
checklist_schedule_inspection_template_instance = ChecklistScheduleInspectionTemplate.from_json(json)
# print the JSON string representation of the object
print(ChecklistScheduleInspectionTemplate.to_json())

# convert the object into a dict
checklist_schedule_inspection_template_dict = checklist_schedule_inspection_template_instance.to_dict()
# create an instance of ChecklistScheduleInspectionTemplate from a dict
checklist_schedule_inspection_template_from_dict = ChecklistScheduleInspectionTemplate.from_dict(checklist_schedule_inspection_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


