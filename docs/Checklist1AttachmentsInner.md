# Checklist1AttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**thumbnail_url** | **str** | Thumbnail URL | [optional] 
**url** | **str** | URL | [optional] 
**filename** | **str** | Filename | [optional] 
**viewable_document_id** | **int** | Viewable Document ID | [optional] 

## Example

```python
from procore_sdk.models.checklist1_attachments_inner import Checklist1AttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist1AttachmentsInner from a JSON string
checklist1_attachments_inner_instance = Checklist1AttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(Checklist1AttachmentsInner.to_json())

# convert the object into a dict
checklist1_attachments_inner_dict = checklist1_attachments_inner_instance.to_dict()
# create an instance of Checklist1AttachmentsInner from a dict
checklist1_attachments_inner_from_dict = Checklist1AttachmentsInner.from_dict(checklist1_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


