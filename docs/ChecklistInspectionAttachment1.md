# ChecklistInspectionAttachment1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**url** | **str** | URL | [optional] 
**thumbnail_url** | **str** | URL | [optional] 
**name** | **str** | Filename | [optional] 
**filename** | **str** | Filename (deprecated) | [optional] 
**content_type** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_inspection_attachment1 import ChecklistInspectionAttachment1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistInspectionAttachment1 from a JSON string
checklist_inspection_attachment1_instance = ChecklistInspectionAttachment1.from_json(json)
# print the JSON string representation of the object
print(ChecklistInspectionAttachment1.to_json())

# convert the object into a dict
checklist_inspection_attachment1_dict = checklist_inspection_attachment1_instance.to_dict()
# create an instance of ChecklistInspectionAttachment1 from a dict
checklist_inspection_attachment1_from_dict = ChecklistInspectionAttachment1.from_dict(checklist_inspection_attachment1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


