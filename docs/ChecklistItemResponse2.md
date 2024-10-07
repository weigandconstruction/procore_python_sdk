# ChecklistItemResponse2

Item Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | Item ID | [optional] 
**status** | **str** | Item Status. Possible values are &#39;conforming&#39;, &#39;non_conforming&#39;, and &#39;not_applicable&#39;. | [optional] 
**responded_at** | **datetime** | Timestamp indicating when Response was added | [optional] 
**responder** | [**PunchItem6CreatedBy**](PunchItem6CreatedBy.md) |  | [optional] 
**item_type** | [**ChecklistItemType**](ChecklistItemType.md) |  | [optional] 
**payload** | [**ChecklistItemResponsePayload**](ChecklistItemResponsePayload.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_response2 import ChecklistItemResponse2

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponse2 from a JSON string
checklist_item_response2_instance = ChecklistItemResponse2.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponse2.to_json())

# convert the object into a dict
checklist_item_response2_dict = checklist_item_response2_instance.to_dict()
# create an instance of ChecklistItemResponse2 from a dict
checklist_item_response2_from_dict = ChecklistItemResponse2.from_dict(checklist_item_response2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


