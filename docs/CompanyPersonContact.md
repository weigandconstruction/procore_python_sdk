# CompanyPersonContact

The contact associated with the Company Person.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | The status of the contact. If this property is set to true, the status of the contact is active. If this property is set to false, the status of the contact is inactive. | [optional] 
**email** | **str** | The email address of the contact. | [optional] 

## Example

```python
from procore_sdk.models.company_person_contact import CompanyPersonContact

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyPersonContact from a JSON string
company_person_contact_instance = CompanyPersonContact.from_json(json)
# print the JSON string representation of the object
print(CompanyPersonContact.to_json())

# convert the object into a dict
company_person_contact_dict = company_person_contact_instance.to_dict()
# create an instance of CompanyPersonContact from a dict
company_person_contact_from_dict = CompanyPersonContact.from_dict(company_person_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


