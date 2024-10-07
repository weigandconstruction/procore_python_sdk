# CompanyWebhook1Hook

Hook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | API Version | [optional] 
**namespace** | **str** | Namespace | [optional] 
**destination_url** | **str** | Notification Endpoint Destination URL | [optional] 
**destination_headers** | [**CompanyWebhookHookDestinationHeaders**](CompanyWebhookHookDestinationHeaders.md) |  | [optional] 

## Example

```python
from procore_sdk.models.company_webhook1_hook import CompanyWebhook1Hook

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWebhook1Hook from a JSON string
company_webhook1_hook_instance = CompanyWebhook1Hook.from_json(json)
# print the JSON string representation of the object
print(CompanyWebhook1Hook.to_json())

# convert the object into a dict
company_webhook1_hook_dict = company_webhook1_hook_instance.to_dict()
# create an instance of CompanyWebhook1Hook from a dict
company_webhook1_hook_from_dict = CompanyWebhook1Hook.from_dict(company_webhook1_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


