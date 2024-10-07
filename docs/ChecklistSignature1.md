# ChecklistSignature1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**captured_by** | [**ChecklistSignatureRequestSignatory**](ChecklistSignatureRequestSignatory.md) |  | [optional] 
**captured_at** | **datetime** | Timestamp of creation | [optional] 
**attachment** | [**ChecklistSignature1Attachment**](ChecklistSignature1Attachment.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_signature1 import ChecklistSignature1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSignature1 from a JSON string
checklist_signature1_instance = ChecklistSignature1.from_json(json)
# print the JSON string representation of the object
print(ChecklistSignature1.to_json())

# convert the object into a dict
checklist_signature1_dict = checklist_signature1_instance.to_dict()
# create an instance of ChecklistSignature1 from a dict
checklist_signature1_from_dict = ChecklistSignature1.from_dict(checklist_signature1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


