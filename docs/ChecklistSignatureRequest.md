# ChecklistSignatureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**signatory** | [**ChecklistSignatureRequestSignatory**](ChecklistSignatureRequestSignatory.md) |  | [optional] 
**signature** | [**ChecklistSignature1**](ChecklistSignature1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_signature_request import ChecklistSignatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSignatureRequest from a JSON string
checklist_signature_request_instance = ChecklistSignatureRequest.from_json(json)
# print the JSON string representation of the object
print(ChecklistSignatureRequest.to_json())

# convert the object into a dict
checklist_signature_request_dict = checklist_signature_request_instance.to_dict()
# create an instance of ChecklistSignatureRequest from a dict
checklist_signature_request_from_dict = ChecklistSignatureRequest.from_dict(checklist_signature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


