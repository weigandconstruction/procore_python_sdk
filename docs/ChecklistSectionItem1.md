# ChecklistSectionItem1


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
**observations** | [**List[ChecklistSectionItem1ObservationsInner]**](ChecklistSectionItem1ObservationsInner.md) | Observations created from the Checklist Item | [optional] 
**attachment_histories** | [**List[ChecklistSectionItem1AttachmentHistoriesInner]**](ChecklistSectionItem1AttachmentHistoriesInner.md) | Item attachment histories | [optional] 
**attachments** | [**List[ChecklistSectionItem1AttachmentsInner]**](ChecklistSectionItem1AttachmentsInner.md) | Item attachments | [optional] 
**histories** | [**List[ChecklistSectionItemHistoriesInner]**](ChecklistSectionItemHistoriesInner.md) | Item histories | [optional] 
**item_response** | [**ChecklistItemResponse**](ChecklistItemResponse.md) |  | [optional] 
**comments** | [**List[ChecklistSectionItemCommentsInner]**](ChecklistSectionItemCommentsInner.md) | Item comments | [optional] 
**response** | [**ChecklistResponse**](ChecklistResponse.md) |  | [optional] 
**response_set** | [**ChecklistSectionItem1ResponseSet**](ChecklistSectionItem1ResponseSet.md) |  | [optional] 
**response_set_id** | **int** | Response Set ID | [optional] 
**type** | [**ChecklistItemType**](ChecklistItemType.md) |  | [optional] 
**template_item_id** | **int** | Template Item ID | [optional] 
**response_type_id** | **int** | Response Type ID | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.checklist_section_item1 import ChecklistSectionItem1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSectionItem1 from a JSON string
checklist_section_item1_instance = ChecklistSectionItem1.from_json(json)
# print the JSON string representation of the object
print(ChecklistSectionItem1.to_json())

# convert the object into a dict
checklist_section_item1_dict = checklist_section_item1_instance.to_dict()
# create an instance of ChecklistSectionItem1 from a dict
checklist_section_item1_from_dict = ChecklistSectionItem1.from_dict(checklist_section_item1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


