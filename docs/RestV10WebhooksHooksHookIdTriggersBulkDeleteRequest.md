# RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID. You must supply either a company_id or project_id. | 
**triggers** | **List[int]** |  | 
**project_id** | **int** | Project ID. You must supply either a company_id or project_id. | 

## Example

```python
from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete_request import RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest from a JSON string
rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete_request_instance = RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest.to_json())

# convert the object into a dict
rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete_request_dict = rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete_request_instance.to_dict()
# create an instance of RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest from a dict
rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete_request_from_dict = RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest.from_dict(rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


