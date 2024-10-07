# CompanyTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID. You must supply either a company_id or project_id. | 
**api_version** | **str** | API Version | 
**trigger** | [**CompanyTriggerTrigger**](CompanyTriggerTrigger.md) |  | 

## Example

```python
from procore_sdk.models.company_trigger import CompanyTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyTrigger from a JSON string
company_trigger_instance = CompanyTrigger.from_json(json)
# print the JSON string representation of the object
print(CompanyTrigger.to_json())

# convert the object into a dict
company_trigger_dict = company_trigger_instance.to_dict()
# create an instance of CompanyTrigger from a dict
company_trigger_from_dict = CompanyTrigger.from_dict(company_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


