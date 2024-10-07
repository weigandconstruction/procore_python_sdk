# TimeAndMaterialSignatureCreateBodySignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Attachment representing the Signature. To upload an attachment, you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;data&#x60; file. | 
**party_id** | **int** | ID of the party the signature is attributed to | 
**signature_text** | **str** | Acknowedgement text the signature was signed against. | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_signature_create_body_signature import TimeAndMaterialSignatureCreateBodySignature

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialSignatureCreateBodySignature from a JSON string
time_and_material_signature_create_body_signature_instance = TimeAndMaterialSignatureCreateBodySignature.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialSignatureCreateBodySignature.to_json())

# convert the object into a dict
time_and_material_signature_create_body_signature_dict = time_and_material_signature_create_body_signature_instance.to_dict()
# create an instance of TimeAndMaterialSignatureCreateBodySignature from a dict
time_and_material_signature_create_body_signature_from_dict = TimeAndMaterialSignatureCreateBodySignature.from_dict(time_and_material_signature_create_body_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


