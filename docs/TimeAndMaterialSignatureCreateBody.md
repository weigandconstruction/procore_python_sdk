# TimeAndMaterialSignatureCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | [**TimeAndMaterialSignatureCreateBodySignature**](TimeAndMaterialSignatureCreateBodySignature.md) |  | 

## Example

```python
from procore_sdk.models.time_and_material_signature_create_body import TimeAndMaterialSignatureCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialSignatureCreateBody from a JSON string
time_and_material_signature_create_body_instance = TimeAndMaterialSignatureCreateBody.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialSignatureCreateBody.to_json())

# convert the object into a dict
time_and_material_signature_create_body_dict = time_and_material_signature_create_body_instance.to_dict()
# create an instance of TimeAndMaterialSignatureCreateBody from a dict
time_and_material_signature_create_body_from_dict = TimeAndMaterialSignatureCreateBody.from_dict(time_and_material_signature_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


