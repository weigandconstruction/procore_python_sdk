# CompanyWebhookHook

Hook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | API Version | 
**namespace** | **str** | Namespace | [optional] 
**destination_url** | **str** | Notification Endpoint Destination URL | 
**destination_headers** | [**CompanyWebhookHookDestinationHeaders**](CompanyWebhookHookDestinationHeaders.md) |  | [optional] 

## Example

```python
from procore_sdk.models.company_webhook_hook import CompanyWebhookHook

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWebhookHook from a JSON string
company_webhook_hook_instance = CompanyWebhookHook.from_json(json)
# print the JSON string representation of the object
print(CompanyWebhookHook.to_json())

# convert the object into a dict
company_webhook_hook_dict = company_webhook_hook_instance.to_dict()
# create an instance of CompanyWebhookHook from a dict
company_webhook_hook_from_dict = CompanyWebhookHook.from_dict(company_webhook_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


