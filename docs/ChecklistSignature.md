# ChecklistSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**captured_by** | [**InspectionItemSignatureCapturedBy**](InspectionItemSignatureCapturedBy.md) |  | [optional] 
**captured_at** | **datetime** | Timestamp of creation | [optional] 
**attachment** | [**InspectionItemSignatureAttachment**](InspectionItemSignatureAttachment.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_signature import ChecklistSignature

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSignature from a JSON string
checklist_signature_instance = ChecklistSignature.from_json(json)
# print the JSON string representation of the object
print(ChecklistSignature.to_json())

# convert the object into a dict
checklist_signature_dict = checklist_signature_instance.to_dict()
# create an instance of ChecklistSignature from a dict
checklist_signature_from_dict = ChecklistSignature.from_dict(checklist_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


