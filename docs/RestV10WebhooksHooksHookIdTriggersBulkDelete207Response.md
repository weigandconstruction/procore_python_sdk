# RestV10WebhooksHooksHookIdTriggersBulkDelete207Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **List[int]** |  | [optional] 
**failed** | [**List[RestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner]**](RestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete207_response import RestV10WebhooksHooksHookIdTriggersBulkDelete207Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WebhooksHooksHookIdTriggersBulkDelete207Response from a JSON string
rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete207_response_instance = RestV10WebhooksHooksHookIdTriggersBulkDelete207Response.from_json(json)
# print the JSON string representation of the object
print(RestV10WebhooksHooksHookIdTriggersBulkDelete207Response.to_json())

# convert the object into a dict
rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete207_response_dict = rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete207_response_instance.to_dict()
# create an instance of RestV10WebhooksHooksHookIdTriggersBulkDelete207Response from a dict
rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete207_response_from_dict = RestV10WebhooksHooksHookIdTriggersBulkDelete207Response.from_dict(rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete207_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


