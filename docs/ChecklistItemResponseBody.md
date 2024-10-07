# ChecklistItemResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_response** | [**ItemResponse**](ItemResponse.md) |  | 

## Example

```python
from procore_sdk.models.checklist_item_response_body import ChecklistItemResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponseBody from a JSON string
checklist_item_response_body_instance = ChecklistItemResponseBody.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponseBody.to_json())

# convert the object into a dict
checklist_item_response_body_dict = checklist_item_response_body_instance.to_dict()
# create an instance of ChecklistItemResponseBody from a dict
checklist_item_response_body_from_dict = ChecklistItemResponseBody.from_dict(checklist_item_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


