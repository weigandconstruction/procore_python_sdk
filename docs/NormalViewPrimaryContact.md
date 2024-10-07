# NormalViewPrimaryContact

Primary contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**business_phone** | **str** | Business phone | [optional] 
**business_phone_extension** | **int** | Business phone extension | [optional] 
**fax_number** | **str** | Fax number | [optional] 
**mobile_phone** | **str** | Mobile phone | [optional] 
**email_address** | **str** | Email | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 

## Example

```python
from procore_sdk.models.normal_view_primary_contact import NormalViewPrimaryContact

# TODO update the JSON string below
json = "{}"
# create an instance of NormalViewPrimaryContact from a JSON string
normal_view_primary_contact_instance = NormalViewPrimaryContact.from_json(json)
# print the JSON string representation of the object
print(NormalViewPrimaryContact.to_json())

# convert the object into a dict
normal_view_primary_contact_dict = normal_view_primary_contact_instance.to_dict()
# create an instance of NormalViewPrimaryContact from a dict
normal_view_primary_contact_from_dict = NormalViewPrimaryContact.from_dict(normal_view_primary_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


