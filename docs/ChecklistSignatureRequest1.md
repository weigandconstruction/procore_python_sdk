# ChecklistSignatureRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**signatory** | [**ChecklistSignatureRequestSignatory**](ChecklistSignatureRequestSignatory.md) |  | [optional] 
**signature** | [**ChecklistSignature2**](ChecklistSignature2.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_signature_request1 import ChecklistSignatureRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSignatureRequest1 from a JSON string
checklist_signature_request1_instance = ChecklistSignatureRequest1.from_json(json)
# print the JSON string representation of the object
print(ChecklistSignatureRequest1.to_json())

# convert the object into a dict
checklist_signature_request1_dict = checklist_signature_request1_instance.to_dict()
# create an instance of ChecklistSignatureRequest1 from a dict
checklist_signature_request1_from_dict = ChecklistSignatureRequest1.from_dict(checklist_signature_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


