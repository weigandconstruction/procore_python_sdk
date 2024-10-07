# ChecklistSignatureRequest2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**signatory** | [**ChecklistSignatureRequestSignatory**](ChecklistSignatureRequestSignatory.md) |  | [optional] 
**signature** | [**ChecklistSignature3**](ChecklistSignature3.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_signature_request2 import ChecklistSignatureRequest2

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSignatureRequest2 from a JSON string
checklist_signature_request2_instance = ChecklistSignatureRequest2.from_json(json)
# print the JSON string representation of the object
print(ChecklistSignatureRequest2.to_json())

# convert the object into a dict
checklist_signature_request2_dict = checklist_signature_request2_instance.to_dict()
# create an instance of ChecklistSignatureRequest2 from a dict
checklist_signature_request2_from_dict = ChecklistSignatureRequest2.from_dict(checklist_signature_request2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


