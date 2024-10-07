# RestV10WebhooksHooksHookIdTriggersBulkPost207Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | [**List[WebhooksTrigger]**](WebhooksTrigger.md) |  | [optional] 
**failed** | [**List[RestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInner]**](RestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_bulk_post207_response import RestV10WebhooksHooksHookIdTriggersBulkPost207Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WebhooksHooksHookIdTriggersBulkPost207Response from a JSON string
rest_v10_webhooks_hooks_hook_id_triggers_bulk_post207_response_instance = RestV10WebhooksHooksHookIdTriggersBulkPost207Response.from_json(json)
# print the JSON string representation of the object
print(RestV10WebhooksHooksHookIdTriggersBulkPost207Response.to_json())

# convert the object into a dict
rest_v10_webhooks_hooks_hook_id_triggers_bulk_post207_response_dict = rest_v10_webhooks_hooks_hook_id_triggers_bulk_post207_response_instance.to_dict()
# create an instance of RestV10WebhooksHooksHookIdTriggersBulkPost207Response from a dict
rest_v10_webhooks_hooks_hook_id_triggers_bulk_post207_response_from_dict = RestV10WebhooksHooksHookIdTriggersBulkPost207Response.from_dict(rest_v10_webhooks_hooks_hook_id_triggers_bulk_post207_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


