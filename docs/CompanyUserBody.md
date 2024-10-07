# CompanyUserBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**CompanyUser**](CompanyUser.md) |  | 

## Example

```python
from procore_sdk.models.company_user_body import CompanyUserBody

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUserBody from a JSON string
company_user_body_instance = CompanyUserBody.from_json(json)
# print the JSON string representation of the object
print(CompanyUserBody.to_json())

# convert the object into a dict
company_user_body_dict = company_user_body_instance.to_dict()
# create an instance of CompanyUserBody from a dict
company_user_body_from_dict = CompanyUserBody.from_dict(company_user_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


