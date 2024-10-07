# CompanyWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID. You must supply either a company_id or project_id. | 
**hook** | [**CompanyWebhookHook**](CompanyWebhookHook.md) |  | 

## Example

```python
from procore_sdk.models.company_webhook import CompanyWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWebhook from a JSON string
company_webhook_instance = CompanyWebhook.from_json(json)
# print the JSON string representation of the object
print(CompanyWebhook.to_json())

# convert the object into a dict
company_webhook_dict = company_webhook_instance.to_dict()
# create an instance of CompanyWebhook from a dict
company_webhook_from_dict = CompanyWebhook.from_dict(company_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


