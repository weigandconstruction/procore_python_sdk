# ChecklistItemResponsePayloadResponseOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Response Option ID | [optional] 
**name** | **str** | Response Option Name | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_response_payload_response_option import ChecklistItemResponsePayloadResponseOption

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponsePayloadResponseOption from a JSON string
checklist_item_response_payload_response_option_instance = ChecklistItemResponsePayloadResponseOption.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponsePayloadResponseOption.to_json())

# convert the object into a dict
checklist_item_response_payload_response_option_dict = checklist_item_response_payload_response_option_instance.to_dict()
# create an instance of ChecklistItemResponsePayloadResponseOption from a dict
checklist_item_response_payload_response_option_from_dict = ChecklistItemResponsePayloadResponseOption.from_dict(checklist_item_response_payload_response_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


