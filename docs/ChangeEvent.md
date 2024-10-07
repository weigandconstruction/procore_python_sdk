# ChangeEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | [optional] 
**number** | **str** | Number | [optional] 
**status** | **str** | DEPRECATED: Use :change_event_status_id. Status | [optional] 
**change_event_status_id** | **int** | Change Event Status ID | 
**change_order_change_reason_id** | **int** | Change Order Change Reason ID | [optional] 
**event_scope** | **str** | Event Scope | 
**event_type** | **str** | Event Type | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**rfi_id** | **int** | RFI ID | [optional] 
**change_event_line_items_attributes** | [**List[ChangeEventLineItem]**](ChangeEventLineItem.md) | Change Event Line Items | [optional] 
**attachments_by_drawing_revision** | [**List[ChangeEventAttachmentsByDrawingRevisionInner]**](ChangeEventAttachmentsByDrawingRevisionInner.md) |  | [optional] 
**attachments_by_file_version** | [**List[ChangeEventAttachmentsByDrawingRevisionInner]**](ChangeEventAttachmentsByDrawingRevisionInner.md) |  | [optional] 
**attachments_by_form** | [**List[ChangeEventAttachmentsByDrawingRevisionInner]**](ChangeEventAttachmentsByDrawingRevisionInner.md) |  | [optional] 
**attachments_by_image** | [**List[ChangeEventAttachmentsByDrawingRevisionInner]**](ChangeEventAttachmentsByDrawingRevisionInner.md) |  | [optional] 
**attachments_by_uuid** | [**List[ChangeEventAttachmentsByUuidInner]**](ChangeEventAttachmentsByUuidInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.change_event import ChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeEvent from a JSON string
change_event_instance = ChangeEvent.from_json(json)
# print the JSON string representation of the object
print(ChangeEvent.to_json())

# convert the object into a dict
change_event_dict = change_event_instance.to_dict()
# create an instance of ChangeEvent from a dict
change_event_from_dict = ChangeEvent.from_dict(change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


