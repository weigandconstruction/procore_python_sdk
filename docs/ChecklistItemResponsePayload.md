# ChecklistItemResponsePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_value** | **str** | Response for an Open Ended Text Item | [optional] 
**number_value** | **int** | Response for an Open Ended Number Item | [optional] 
**date_value** | **date** | Response for an Open Ended Date Item | [optional] 
**response_option** | [**ChecklistItemResponsePayloadResponseOption**](ChecklistItemResponsePayloadResponseOption.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_response_payload import ChecklistItemResponsePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponsePayload from a JSON string
checklist_item_response_payload_instance = ChecklistItemResponsePayload.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponsePayload.to_json())

# convert the object into a dict
checklist_item_response_payload_dict = checklist_item_response_payload_instance.to_dict()
# create an instance of ChecklistItemResponsePayload from a dict
checklist_item_response_payload_from_dict = ChecklistItemResponsePayload.from_dict(checklist_item_response_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


