# SignatureRequest

Checklist Signature Request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signatory_id** | **int** | ID of the User requested to sign | 

## Example

```python
from procore_sdk.models.signature_request import SignatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureRequest from a JSON string
signature_request_instance = SignatureRequest.from_json(json)
# print the JSON string representation of the object
print(SignatureRequest.to_json())

# convert the object into a dict
signature_request_dict = signature_request_instance.to_dict()
# create an instance of SignatureRequest from a dict
signature_request_from_dict = SignatureRequest.from_dict(signature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


