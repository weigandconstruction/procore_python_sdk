# ChecklistSignature1Attachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**url** | **str** | URL | [optional] 
**filename** | **str** | Filename | [optional] 
**name** | **str** | Attachment name | [optional] 

## Example

```python
from procore_sdk.models.checklist_signature1_attachment import ChecklistSignature1Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSignature1Attachment from a JSON string
checklist_signature1_attachment_instance = ChecklistSignature1Attachment.from_json(json)
# print the JSON string representation of the object
print(ChecklistSignature1Attachment.to_json())

# convert the object into a dict
checklist_signature1_attachment_dict = checklist_signature1_attachment_instance.to_dict()
# create an instance of ChecklistSignature1Attachment from a dict
checklist_signature1_attachment_from_dict = ChecklistSignature1Attachment.from_dict(checklist_signature1_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


