# ChecklistClosedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**login** | **str** | Email | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.checklist_closed_by import ChecklistClosedBy

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistClosedBy from a JSON string
checklist_closed_by_instance = ChecklistClosedBy.from_json(json)
# print the JSON string representation of the object
print(ChecklistClosedBy.to_json())

# convert the object into a dict
checklist_closed_by_dict = checklist_closed_by_instance.to_dict()
# create an instance of ChecklistClosedBy from a dict
checklist_closed_by_from_dict = ChecklistClosedBy.from_dict(checklist_closed_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


