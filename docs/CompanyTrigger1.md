# CompanyTrigger1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID. You must supply either a company_id or project_id. | 
**api_version** | **str** | API Version | 
**triggers** | [**List[CompanyTriggerTrigger]**](CompanyTriggerTrigger.md) |  | 

## Example

```python
from procore_sdk.models.company_trigger1 import CompanyTrigger1

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyTrigger1 from a JSON string
company_trigger1_instance = CompanyTrigger1.from_json(json)
# print the JSON string representation of the object
print(CompanyTrigger1.to_json())

# convert the object into a dict
company_trigger1_dict = company_trigger1_instance.to_dict()
# create an instance of CompanyTrigger1 from a dict
company_trigger1_from_dict = CompanyTrigger1.from_dict(company_trigger1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


