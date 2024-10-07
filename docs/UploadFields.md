# UploadFields

Fields to send with the file data to sucessfully complete the upload. Do not make any assumptions about the names or contents of the fields because they may change at any time to any other value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the file for upload | [optional] 
**content_type** | **str** | Content-Type for the upload | [optional] 
**content_disposition** | **str** | Disposition for the upload | [optional] 
**policy** | **str** | The Base64-encoded security policy that describes what is permitted in the request. | [optional] 
**x_amz_credential** | **str** | Scope information for calculating the signing key for signature calculation. | [optional] 
**x_amz_algorithm** | **str** | The signing algorithm used | [optional] 
**x_amz_date** | **str** | The date value in ISO8601 format | [optional] 
**x_amz_signature** | **str** | The HMAC-SHA256 hash of the security policy. | [optional] 

## Example

```python
from procore_sdk.models.upload_fields import UploadFields

# TODO update the JSON string below
json = "{}"
# create an instance of UploadFields from a JSON string
upload_fields_instance = UploadFields.from_json(json)
# print the JSON string representation of the object
print(UploadFields.to_json())

# convert the object into a dict
upload_fields_dict = upload_fields_instance.to_dict()
# create an instance of UploadFields from a dict
upload_fields_from_dict = UploadFields.from_dict(upload_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


