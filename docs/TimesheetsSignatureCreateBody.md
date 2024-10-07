# TimesheetsSignatureCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | [**TimesheetsSignatureCreateBodySignature**](TimesheetsSignatureCreateBodySignature.md) |  | 

## Example

```python
from procore_sdk.models.timesheets_signature_create_body import TimesheetsSignatureCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetsSignatureCreateBody from a JSON string
timesheets_signature_create_body_instance = TimesheetsSignatureCreateBody.from_json(json)
# print the JSON string representation of the object
print(TimesheetsSignatureCreateBody.to_json())

# convert the object into a dict
timesheets_signature_create_body_dict = timesheets_signature_create_body_instance.to_dict()
# create an instance of TimesheetsSignatureCreateBody from a dict
timesheets_signature_create_body_from_dict = TimesheetsSignatureCreateBody.from_dict(timesheets_signature_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


