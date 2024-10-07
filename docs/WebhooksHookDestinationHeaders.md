# WebhooksHookDestinationHeaders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | **str** | Authorization header | [optional] 

## Example

```python
from procore_sdk.models.webhooks_hook_destination_headers import WebhooksHookDestinationHeaders

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksHookDestinationHeaders from a JSON string
webhooks_hook_destination_headers_instance = WebhooksHookDestinationHeaders.from_json(json)
# print the JSON string representation of the object
print(WebhooksHookDestinationHeaders.to_json())

# convert the object into a dict
webhooks_hook_destination_headers_dict = webhooks_hook_destination_headers_instance.to_dict()
# create an instance of WebhooksHookDestinationHeaders from a dict
webhooks_hook_destination_headers_from_dict = WebhooksHookDestinationHeaders.from_dict(webhooks_hook_destination_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


