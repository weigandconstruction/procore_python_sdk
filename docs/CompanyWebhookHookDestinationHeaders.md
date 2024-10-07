# CompanyWebhookHookDestinationHeaders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | **str** | Authorization header for Destination URL | [optional] 

## Example

```python
from procore_sdk.models.company_webhook_hook_destination_headers import CompanyWebhookHookDestinationHeaders

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWebhookHookDestinationHeaders from a JSON string
company_webhook_hook_destination_headers_instance = CompanyWebhookHookDestinationHeaders.from_json(json)
# print the JSON string representation of the object
print(CompanyWebhookHookDestinationHeaders.to_json())

# convert the object into a dict
company_webhook_hook_destination_headers_dict = company_webhook_hook_destination_headers_instance.to_dict()
# create an instance of CompanyWebhookHookDestinationHeaders from a dict
company_webhook_hook_destination_headers_from_dict = CompanyWebhookHookDestinationHeaders.from_dict(company_webhook_hook_destination_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


