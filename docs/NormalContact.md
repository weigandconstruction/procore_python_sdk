# NormalContact

The Contact associated with the Project Person

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | The active status of the Contact associated with the Project Person | [optional] 
**email** | **str** | The email address of the contact. | [optional] 

## Example

```python
from procore_sdk.models.normal_contact import NormalContact

# TODO update the JSON string below
json = "{}"
# create an instance of NormalContact from a JSON string
normal_contact_instance = NormalContact.from_json(json)
# print the JSON string representation of the object
print(NormalContact.to_json())

# convert the object into a dict
normal_contact_dict = normal_contact_instance.to_dict()
# create an instance of NormalContact from a dict
normal_contact_from_dict = NormalContact.from_dict(normal_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


