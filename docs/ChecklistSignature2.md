# ChecklistSignature2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**captured_by** | [**ChecklistSignatureRequestSignatory**](ChecklistSignatureRequestSignatory.md) |  | [optional] 
**captured_at** | **datetime** | Timestamp of creation | [optional] 
**attachment** | [**RestV10WorkOrderContractsPost201ResponseAttachmentsInner**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_signature2 import ChecklistSignature2

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSignature2 from a JSON string
checklist_signature2_instance = ChecklistSignature2.from_json(json)
# print the JSON string representation of the object
print(ChecklistSignature2.to_json())

# convert the object into a dict
checklist_signature2_dict = checklist_signature2_instance.to_dict()
# create an instance of ChecklistSignature2 from a dict
checklist_signature2_from_dict = ChecklistSignature2.from_dict(checklist_signature2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


