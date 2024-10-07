# RestV10WebhooksHooksIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID. You must supply either a company_id or project_id. | 
**hook** | [**CompanyWebhook1Hook**](CompanyWebhook1Hook.md) |  | 
**project_id** | **int** | Project ID. You must supply either a company_id or project_id. | 

## Example

```python
from procore_sdk.models.rest_v10_webhooks_hooks_id_patch_request import RestV10WebhooksHooksIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WebhooksHooksIdPatchRequest from a JSON string
rest_v10_webhooks_hooks_id_patch_request_instance = RestV10WebhooksHooksIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10WebhooksHooksIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_webhooks_hooks_id_patch_request_dict = rest_v10_webhooks_hooks_id_patch_request_instance.to_dict()
# create an instance of RestV10WebhooksHooksIdPatchRequest from a dict
rest_v10_webhooks_hooks_id_patch_request_from_dict = RestV10WebhooksHooksIdPatchRequest.from_dict(rest_v10_webhooks_hooks_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


