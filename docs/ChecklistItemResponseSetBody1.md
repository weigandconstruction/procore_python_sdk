# ChecklistItemResponseSetBody1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_set** | [**ItemResponseSet1**](ItemResponseSet1.md) |  | 

## Example

```python
from procore_sdk.models.checklist_item_response_set_body1 import ChecklistItemResponseSetBody1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponseSetBody1 from a JSON string
checklist_item_response_set_body1_instance = ChecklistItemResponseSetBody1.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponseSetBody1.to_json())

# convert the object into a dict
checklist_item_response_set_body1_dict = checklist_item_response_set_body1_instance.to_dict()
# create an instance of ChecklistItemResponseSetBody1 from a dict
checklist_item_response_set_body1_from_dict = ChecklistItemResponseSetBody1.from_dict(checklist_item_response_set_body1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


