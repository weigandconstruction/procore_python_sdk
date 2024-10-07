# CompanyTrigger2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID. You must supply either a company_id or project_id. | 
**triggers** | **List[int]** |  | 

## Example

```python
from procore_sdk.models.company_trigger2 import CompanyTrigger2

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyTrigger2 from a JSON string
company_trigger2_instance = CompanyTrigger2.from_json(json)
# print the JSON string representation of the object
print(CompanyTrigger2.to_json())

# convert the object into a dict
company_trigger2_dict = company_trigger2_instance.to_dict()
# create an instance of CompanyTrigger2 from a dict
company_trigger2_from_dict = CompanyTrigger2.from_dict(company_trigger2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


