# RestV10WebhooksHooksPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID. You must supply either a company_id or project_id. | 
**hook** | [**CompanyWebhookHook**](CompanyWebhookHook.md) |  | 
**project_id** | **int** | Project ID. You must supply either a company_id or project_id. | 

## Example

```python
from procore_sdk.models.rest_v10_webhooks_hooks_post_request import RestV10WebhooksHooksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WebhooksHooksPostRequest from a JSON string
rest_v10_webhooks_hooks_post_request_instance = RestV10WebhooksHooksPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10WebhooksHooksPostRequest.to_json())

# convert the object into a dict
rest_v10_webhooks_hooks_post_request_dict = rest_v10_webhooks_hooks_post_request_instance.to_dict()
# create an instance of RestV10WebhooksHooksPostRequest from a dict
rest_v10_webhooks_hooks_post_request_from_dict = RestV10WebhooksHooksPostRequest.from_dict(rest_v10_webhooks_hooks_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


