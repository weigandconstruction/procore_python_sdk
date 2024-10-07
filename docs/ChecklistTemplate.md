# ChecklistTemplate

Checklist Template object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | [optional] 
**inspection_type_id** | **int** | The ID of an Inspection Type | [optional] 
**alternative_response_set_id** | **int** | The ID of an Alternative Response Set | [optional] 
**name** | **str** | Name | [optional] 
**trade_id** | **int** | The ID of a Trade | [optional] 

## Example

```python
from procore_sdk.models.checklist_template import ChecklistTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplate from a JSON string
checklist_template_instance = ChecklistTemplate.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplate.to_json())

# convert the object into a dict
checklist_template_dict = checklist_template_instance.to_dict()
# create an instance of ChecklistTemplate from a dict
checklist_template_from_dict = ChecklistTemplate.from_dict(checklist_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


