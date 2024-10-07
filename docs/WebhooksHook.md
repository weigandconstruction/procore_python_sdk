# WebhooksHook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**api_version** | **str** | API Version | [optional] 
**destination_headers** | [**WebhooksHookDestinationHeaders**](WebhooksHookDestinationHeaders.md) |  | [optional] 
**destination_url** | **str** | Notification endpoint URL | [optional] 
**owned_by_company_id** | **int** | Hook Owned by Company ID | [optional] 
**owned_by_project_id** | **int** | Hook Owned by unique identifier for the Project | [optional] 
**owned_by_user_id** | **int** | Hook Owned by User ID | [optional] 
**namespace** | **str** | Hook namespace | [optional] 

## Example

```python
from procore_sdk.models.webhooks_hook import WebhooksHook

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksHook from a JSON string
webhooks_hook_instance = WebhooksHook.from_json(json)
# print the JSON string representation of the object
print(WebhooksHook.to_json())

# convert the object into a dict
webhooks_hook_dict = webhooks_hook_instance.to_dict()
# create an instance of WebhooksHook from a dict
webhooks_hook_from_dict = WebhooksHook.from_dict(webhooks_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


