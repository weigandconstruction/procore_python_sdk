# ChecklistListGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**ChecklistListGroupHeader**](ChecklistListGroupHeader.md) |  | [optional] 
**data** | [**List[ChecklistListGroupedData]**](ChecklistListGroupedData.md) | Array of Inspections created from Inspection Template based on header information | [optional] 

## Example

```python
from procore_sdk.models.checklist_list_group import ChecklistListGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistListGroup from a JSON string
checklist_list_group_instance = ChecklistListGroup.from_json(json)
# print the JSON string representation of the object
print(ChecklistListGroup.to_json())

# convert the object into a dict
checklist_list_group_dict = checklist_list_group_instance.to_dict()
# create an instance of ChecklistListGroup from a dict
checklist_list_group_from_dict = ChecklistListGroup.from_dict(checklist_list_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


