# ChecklistSection1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**position** | **int** | Position | [optional] 
**template_section_id** | **int** | ID of Corresponding Checklist Template Section | [optional] 
**updated_at** | **datetime** | Timestamp of update | [optional] 

## Example

```python
from procore_sdk.models.checklist_section1 import ChecklistSection1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSection1 from a JSON string
checklist_section1_instance = ChecklistSection1.from_json(json)
# print the JSON string representation of the object
print(ChecklistSection1.to_json())

# convert the object into a dict
checklist_section1_dict = checklist_section1_instance.to_dict()
# create an instance of ChecklistSection1 from a dict
checklist_section1_from_dict = ChecklistSection1.from_dict(checklist_section1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


