# ChecklistItemResponse1

Item Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | Item ID | [optional] 
**item_type** | [**ChecklistItemType**](ChecklistItemType.md) |  | [optional] 
**payload** | [**ChecklistItemResponsePayload**](ChecklistItemResponsePayload.md) |  | [optional] 
**responded_at** | **datetime** | Timestamp indicating when Response was added | [optional] 
**responder** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**status** | **str** | Item Status | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_response1 import ChecklistItemResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponse1 from a JSON string
checklist_item_response1_instance = ChecklistItemResponse1.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponse1.to_json())

# convert the object into a dict
checklist_item_response1_dict = checklist_item_response1_instance.to_dict()
# create an instance of ChecklistItemResponse1 from a dict
checklist_item_response1_from_dict = ChecklistItemResponse1.from_dict(checklist_item_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


