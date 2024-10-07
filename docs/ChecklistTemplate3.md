# ChecklistTemplate3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Checklist Template ID | [optional] 
**name** | **str** | Checklist Template Name | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**description** | **str** | Checklist Template Description | [optional] 
**inspection_type** | [**InspectionType2**](InspectionType2.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_template3 import ChecklistTemplate3

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplate3 from a JSON string
checklist_template3_instance = ChecklistTemplate3.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplate3.to_json())

# convert the object into a dict
checklist_template3_dict = checklist_template3_instance.to_dict()
# create an instance of ChecklistTemplate3 from a dict
checklist_template3_from_dict = ChecklistTemplate3.from_dict(checklist_template3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


