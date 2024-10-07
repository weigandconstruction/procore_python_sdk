# ChecklistItemAttachments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | The ID of the Checklist Item | 
**prostore_file_ids** | **List[int]** | An array of Prostore Files to link to the Checklist Item | 

## Example

```python
from procore_sdk.models.checklist_item_attachments import ChecklistItemAttachments

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemAttachments from a JSON string
checklist_item_attachments_instance = ChecklistItemAttachments.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemAttachments.to_json())

# convert the object into a dict
checklist_item_attachments_dict = checklist_item_attachments_instance.to_dict()
# create an instance of ChecklistItemAttachments from a dict
checklist_item_attachments_from_dict = ChecklistItemAttachments.from_dict(checklist_item_attachments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


