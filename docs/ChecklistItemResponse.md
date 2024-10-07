# ChecklistItemResponse

Item Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | Item ID | [optional] 
**status** | **str** | Item Status | [optional] 
**responded_at** | **datetime** | Timestamp indicating when Response was added | [optional] 
**responder** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**item_type** | [**ChecklistItemType**](ChecklistItemType.md) |  | [optional] 
**payload** | [**ChecklistItemResponsePayload**](ChecklistItemResponsePayload.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_response import ChecklistItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponse from a JSON string
checklist_item_response_instance = ChecklistItemResponse.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponse.to_json())

# convert the object into a dict
checklist_item_response_dict = checklist_item_response_instance.to_dict()
# create an instance of ChecklistItemResponse from a dict
checklist_item_response_from_dict = ChecklistItemResponse.from_dict(checklist_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


