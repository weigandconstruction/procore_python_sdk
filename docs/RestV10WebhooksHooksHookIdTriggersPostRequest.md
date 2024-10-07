# RestV10WebhooksHooksHookIdTriggersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID. You must supply either a company_id or project_id. | 
**api_version** | **str** | API Version | 
**trigger** | [**CompanyTriggerTrigger**](CompanyTriggerTrigger.md) |  | 
**project_id** | **int** | Project ID. You must supply either a company_id or project_id. | 

## Example

```python
from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_post_request import RestV10WebhooksHooksHookIdTriggersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WebhooksHooksHookIdTriggersPostRequest from a JSON string
rest_v10_webhooks_hooks_hook_id_triggers_post_request_instance = RestV10WebhooksHooksHookIdTriggersPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10WebhooksHooksHookIdTriggersPostRequest.to_json())

# convert the object into a dict
rest_v10_webhooks_hooks_hook_id_triggers_post_request_dict = rest_v10_webhooks_hooks_hook_id_triggers_post_request_instance.to_dict()
# create an instance of RestV10WebhooksHooksHookIdTriggersPostRequest from a dict
rest_v10_webhooks_hooks_hook_id_triggers_post_request_from_dict = RestV10WebhooksHooksHookIdTriggersPostRequest.from_dict(rest_v10_webhooks_hooks_hook_id_triggers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


