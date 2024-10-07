# TimesheetsSignatureCreateBodySignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Attachment representing the Signature. To upload an attachment, you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;data&#x60; file. | 
**user_id** | **int** | ID of the user the signature is attributed to | 
**signature_text** | **str** | Acknowedgement text the signature was signed against. | [optional] 

## Example

```python
from procore_sdk.models.timesheets_signature_create_body_signature import TimesheetsSignatureCreateBodySignature

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetsSignatureCreateBodySignature from a JSON string
timesheets_signature_create_body_signature_instance = TimesheetsSignatureCreateBodySignature.from_json(json)
# print the JSON string representation of the object
print(TimesheetsSignatureCreateBodySignature.to_json())

# convert the object into a dict
timesheets_signature_create_body_signature_dict = timesheets_signature_create_body_signature_instance.to_dict()
# create an instance of TimesheetsSignatureCreateBodySignature from a dict
timesheets_signature_create_body_signature_from_dict = TimesheetsSignatureCreateBodySignature.from_dict(timesheets_signature_create_body_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


