# ChecklistInspectionAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**url** | **str** | URL | [optional] 
**thumbnail_url** | **str** | URL | [optional] 
**name** | **str** | Filename | [optional] 
**filename** | **str** | Filename (deprecated) | [optional] 
**content_type** | **str** |  | [optional] 
**viewable_document_id** | **int** | Viewable Document ID | [optional] 

## Example

```python
from procore_sdk.models.checklist_inspection_attachment import ChecklistInspectionAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistInspectionAttachment from a JSON string
checklist_inspection_attachment_instance = ChecklistInspectionAttachment.from_json(json)
# print the JSON string representation of the object
print(ChecklistInspectionAttachment.to_json())

# convert the object into a dict
checklist_inspection_attachment_dict = checklist_inspection_attachment_instance.to_dict()
# create an instance of ChecklistInspectionAttachment from a dict
checklist_inspection_attachment_from_dict = ChecklistInspectionAttachment.from_dict(checklist_inspection_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


