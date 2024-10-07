# CompanyPersonBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person** | [**CompanyPerson1**](CompanyPerson1.md) |  | 

## Example

```python
from procore_sdk.models.company_person_body import CompanyPersonBody

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyPersonBody from a JSON string
company_person_body_instance = CompanyPersonBody.from_json(json)
# print the JSON string representation of the object
print(CompanyPersonBody.to_json())

# convert the object into a dict
company_person_body_dict = company_person_body_instance.to_dict()
# create an instance of CompanyPersonBody from a dict
company_person_body_from_dict = CompanyPersonBody.from_dict(company_person_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


