# ChecklistSignature3Attachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**thumbnail_url** | **str** | URL | [optional] 
**url** | **str** | URL | [optional] 
**filename** | **str** | Filename | [optional] 
**name** | **str** | Attachment Name | [optional] 
**viewable_document_id** | **int** | Viewable Document ID | [optional] 

## Example

```python
from procore_sdk.models.checklist_signature3_attachment import ChecklistSignature3Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSignature3Attachment from a JSON string
checklist_signature3_attachment_instance = ChecklistSignature3Attachment.from_json(json)
# print the JSON string representation of the object
print(ChecklistSignature3Attachment.to_json())

# convert the object into a dict
checklist_signature3_attachment_dict = checklist_signature3_attachment_instance.to_dict()
# create an instance of ChecklistSignature3Attachment from a dict
checklist_signature3_attachment_from_dict = ChecklistSignature3Attachment.from_dict(checklist_signature3_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


