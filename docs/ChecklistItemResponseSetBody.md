# ChecklistItemResponseSetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_set** | [**ItemResponseSet**](ItemResponseSet.md) |  | 

## Example

```python
from procore_sdk.models.checklist_item_response_set_body import ChecklistItemResponseSetBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponseSetBody from a JSON string
checklist_item_response_set_body_instance = ChecklistItemResponseSetBody.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponseSetBody.to_json())

# convert the object into a dict
checklist_item_response_set_body_dict = checklist_item_response_set_body_instance.to_dict()
# create an instance of ChecklistItemResponseSetBody from a dict
checklist_item_response_set_body_from_dict = ChecklistItemResponseSetBody.from_dict(checklist_item_response_set_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


