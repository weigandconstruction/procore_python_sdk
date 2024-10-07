# ChecklistSignature3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**captured_by** | [**ChecklistSignatureRequestSignatory**](ChecklistSignatureRequestSignatory.md) |  | [optional] 
**captured_at** | **datetime** | Timestamp of creation | [optional] 
**attachment** | [**ChecklistSignature3Attachment**](ChecklistSignature3Attachment.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_signature3 import ChecklistSignature3

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSignature3 from a JSON string
checklist_signature3_instance = ChecklistSignature3.from_json(json)
# print the JSON string representation of the object
print(ChecklistSignature3.to_json())

# convert the object into a dict
checklist_signature3_dict = checklist_signature3_instance.to_dict()
# create an instance of ChecklistSignature3 from a dict
checklist_signature3_from_dict = ChecklistSignature3.from_dict(checklist_signature3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


