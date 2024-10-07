# CompanyPerson

The Company Person object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**CompanyPersonContact**](CompanyPersonContact.md) |  | [optional] 
**employee_id** | **str** | The employee id of the Company Person. | [optional] 
**first_name** | **str** | The first name of the Company Person. | [optional] 
**id** | **int** | The unique identifier of the Company Person. | [optional] 
**is_employee** | **bool** | The employee status of the Company Person. If this property is set to true, the Company Person is an employee. | [optional] 
**last_name** | **str** | The last name of the Company Person. | [optional] 
**user_id** | **int** | The unique identifier if this Company Person represents a user. This value is set to NULL for a Reference User. | [optional] 
**user_uuid** | **int** | The user UUID for if this Company Person represents a user. This value is set to NULL for a Reference User. | [optional] 
**work_classification_id** | **int** | The unique identifier for the work classification of the Company Person. | [optional] 
**origin_id** | **str** | The Origin ID of the Company User | [optional] 

## Example

```python
from procore_sdk.models.company_person import CompanyPerson

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyPerson from a JSON string
company_person_instance = CompanyPerson.from_json(json)
# print the JSON string representation of the object
print(CompanyPerson.to_json())

# convert the object into a dict
company_person_dict = company_person_instance.to_dict()
# create an instance of CompanyPerson from a dict
company_person_from_dict = CompanyPerson.from_dict(company_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


