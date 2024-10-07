# ChecklistSignatureRequestCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature_request** | [**SignatureRequest**](SignatureRequest.md) |  | 

## Example

```python
from procore_sdk.models.checklist_signature_request_create_body import ChecklistSignatureRequestCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSignatureRequestCreateBody from a JSON string
checklist_signature_request_create_body_instance = ChecklistSignatureRequestCreateBody.from_json(json)
# print the JSON string representation of the object
print(ChecklistSignatureRequestCreateBody.to_json())

# convert the object into a dict
checklist_signature_request_create_body_dict = checklist_signature_request_create_body_instance.to_dict()
# create an instance of ChecklistSignatureRequestCreateBody from a dict
checklist_signature_request_create_body_from_dict = ChecklistSignatureRequestCreateBody.from_dict(checklist_signature_request_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


