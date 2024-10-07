# ChecklistItemAttachment1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attachment ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**created_by** | [**ChecklistItemAttachment1CreatedBy**](ChecklistItemAttachment1CreatedBy.md) |  | [optional] 
**attachment** | [**ChecklistItemAttachment1Attachment**](ChecklistItemAttachment1Attachment.md) |  | [optional] 
**item_id** | **int** | Checklist Item ID | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_attachment1 import ChecklistItemAttachment1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemAttachment1 from a JSON string
checklist_item_attachment1_instance = ChecklistItemAttachment1.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemAttachment1.to_json())

# convert the object into a dict
checklist_item_attachment1_dict = checklist_item_attachment1_instance.to_dict()
# create an instance of ChecklistItemAttachment1 from a dict
checklist_item_attachment1_from_dict = ChecklistItemAttachment1.from_dict(checklist_item_attachment1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


