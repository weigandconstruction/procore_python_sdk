# CompanyWebhook1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID. You must supply either a company_id or project_id. | 
**hook** | [**CompanyWebhook1Hook**](CompanyWebhook1Hook.md) |  | 

## Example

```python
from procore_sdk.models.company_webhook1 import CompanyWebhook1

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWebhook1 from a JSON string
company_webhook1_instance = CompanyWebhook1.from_json(json)
# print the JSON string representation of the object
print(CompanyWebhook1.to_json())

# convert the object into a dict
company_webhook1_dict = company_webhook1_instance.to_dict()
# create an instance of CompanyWebhook1 from a dict
company_webhook1_from_dict = CompanyWebhook1.from_dict(company_webhook1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


