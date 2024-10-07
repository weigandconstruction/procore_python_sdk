# WebhooksTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**webhook_hook_id** | **int** | Hook ID | [optional] 
**resource_name** | **str** | Resource Name | [optional] 
**resource_id** | **int** | Resource ID | [optional] 
**event_type** | **str** | Event Type | [optional] 
**company_id** | **int** | Company ID (for Company scope) | [optional] 
**project_id** | **int** | Project ID (for Project scope) | [optional] 
**user_id** | **int** | User ID | [optional] 

## Example

```python
from procore_sdk.models.webhooks_trigger import WebhooksTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksTrigger from a JSON string
webhooks_trigger_instance = WebhooksTrigger.from_json(json)
# print the JSON string representation of the object
print(WebhooksTrigger.to_json())

# convert the object into a dict
webhooks_trigger_dict = webhooks_trigger_instance.to_dict()
# create an instance of WebhooksTrigger from a dict
webhooks_trigger_from_dict = WebhooksTrigger.from_dict(webhooks_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


