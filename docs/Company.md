# Company

Company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Company id | [optional] 
**name** | **str** | Company name | [optional] 
**is_active** | **bool** | Company is active status | [optional] 
**logo_url** | **str** | Company Logo URL | [optional] 
**pcn_business_experience** | **bool** | Company has business experience enabled | [optional] 
**my_company** | **bool** | The current user is an active employee of this company. This will only return as true for a single company in the response. | [optional] 

## Example

```python
from procore_sdk.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print(Company.to_json())

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_from_dict = Company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


