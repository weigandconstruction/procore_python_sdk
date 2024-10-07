# ChecklistSectionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**details** | **str** | Details | [optional] 
**status** | **str** | Status | [optional] 
**responded_with** | **str** | Representation of an Item&#39;s Response | [optional] 
**origin_id** | **int** | ID of Corresponding Checklist Template Item | [optional] 
**section_id** | **int** | Checklist Section ID | [optional] 
**position** | **int** | Position | [optional] 
**observations** | [**List[ChecklistSectionItemObservationsInner]**](ChecklistSectionItemObservationsInner.md) | Observations created from the Checklist Item | [optional] 
**attachment_histories** | [**List[ChecklistSectionItemAttachmentHistoriesInner]**](ChecklistSectionItemAttachmentHistoriesInner.md) | Item attachment histories | [optional] 
**attachments** | [**List[ChecklistSectionItemAttachmentHistoriesInner]**](ChecklistSectionItemAttachmentHistoriesInner.md) | Item attachments | [optional] 
**histories** | [**List[ChecklistSectionItemHistoriesInner]**](ChecklistSectionItemHistoriesInner.md) | Item histories | [optional] 
**item_response** | [**ChecklistItemResponse**](ChecklistItemResponse.md) |  | [optional] 
**comments** | [**List[ChecklistSectionItemCommentsInner]**](ChecklistSectionItemCommentsInner.md) | Item comments | [optional] 
**response** | [**ChecklistResponse**](ChecklistResponse.md) |  | [optional] 
**response_set** | [**ChecklistSectionItemResponseSet**](ChecklistSectionItemResponseSet.md) |  | [optional] 
**type** | [**ChecklistItemType**](ChecklistItemType.md) |  | [optional] 
**response_set_id** | **int** | Response Set ID | [optional] 
**template_item_id** | **int** | Template Item ID | [optional] 
**response_type_id** | **int** | Response Type ID | [optional] 

## Example

```python
from procore_sdk.models.checklist_section_item import ChecklistSectionItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSectionItem from a JSON string
checklist_section_item_instance = ChecklistSectionItem.from_json(json)
# print the JSON string representation of the object
print(ChecklistSectionItem.to_json())

# convert the object into a dict
checklist_section_item_dict = checklist_section_item_instance.to_dict()
# create an instance of ChecklistSectionItem from a dict
checklist_section_item_from_dict = ChecklistSectionItem.from_dict(checklist_section_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


