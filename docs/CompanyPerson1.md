# CompanyPerson1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The First Name of the Company Person | [optional] 
**last_name** | **str** | The Last Name of the Company Person | 
**is_employee** | **bool** | The Employee status of the Company Person | [optional] [default to False]
**employee_id** | **str** | The Employee ID of the Company Person | [optional] 
**active** | **bool** | The active status of the Company Person | [optional] 
**origin_id** | **str** | The Origin ID of the Company User | [optional] 

## Example

```python
from procore_sdk.models.company_person1 import CompanyPerson1

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyPerson1 from a JSON string
company_person1_instance = CompanyPerson1.from_json(json)
# print the JSON string representation of the object
print(CompanyPerson1.to_json())

# convert the object into a dict
company_person1_dict = company_person1_instance.to_dict()
# create an instance of CompanyPerson1 from a dict
company_person1_from_dict = CompanyPerson1.from_dict(company_person1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


