# ChecklistSection2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**position** | **int** | Position | [optional] 
**list_id** | **int** | Checklist ID. A Checklist Section will either have a &#x60;list_id&#x60; or &#x60;list_template_id&#x60;, but not both. | [optional] 
**not_applicable** | **bool** | Not applicable status | [optional] 

## Example

```python
from procore_sdk.models.checklist_section2 import ChecklistSection2

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSection2 from a JSON string
checklist_section2_instance = ChecklistSection2.from_json(json)
# print the JSON string representation of the object
print(ChecklistSection2.to_json())

# convert the object into a dict
checklist_section2_dict = checklist_section2_instance.to_dict()
# create an instance of ChecklistSection2 from a dict
checklist_section2_from_dict = ChecklistSection2.from_dict(checklist_section2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


