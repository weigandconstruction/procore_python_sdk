# CompanyTriggerTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_name** | **str** | Resource Name | 
**event_type** | **str** | Event Type | 

## Example

```python
from procore_sdk.models.company_trigger_trigger import CompanyTriggerTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyTriggerTrigger from a JSON string
company_trigger_trigger_instance = CompanyTriggerTrigger.from_json(json)
# print the JSON string representation of the object
print(CompanyTriggerTrigger.to_json())

# convert the object into a dict
company_trigger_trigger_dict = company_trigger_trigger_instance.to_dict()
# create an instance of CompanyTriggerTrigger from a dict
company_trigger_trigger_from_dict = CompanyTriggerTrigger.from_dict(company_trigger_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


