# WebhooksDeliveryEvent

The event payload sent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | ID of the user who made the change | [optional] 
**timestamp** | **datetime** | Time the change was made | [optional] 
**resource_name** | **str** | Name of the changed resource | [optional] 
**resource_id** | **int** | ID of the changed resource | [optional] 
**project_id** | **int** | ID of the project the resource belongs to | [optional] 
**id** | **int** | ID of the event | [optional] 
**ulid** | **str** | Unique identifier encoded as a 26 character string. | [optional] 
**event_type** | **str** | Type of event: [create | update | delete] | [optional] 
**company_id** | **int** | ID of the company the resource belongs to | [optional] 
**api_version** | **str** | Version of the originating api resource | [optional] 
**metadata** | [**WebhooksDeliveryEventMetadata**](WebhooksDeliveryEventMetadata.md) |  | [optional] 

## Example

```python
from procore_sdk.models.webhooks_delivery_event import WebhooksDeliveryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksDeliveryEvent from a JSON string
webhooks_delivery_event_instance = WebhooksDeliveryEvent.from_json(json)
# print the JSON string representation of the object
print(WebhooksDeliveryEvent.to_json())

# convert the object into a dict
webhooks_delivery_event_dict = webhooks_delivery_event_instance.to_dict()
# create an instance of WebhooksDeliveryEvent from a dict
webhooks_delivery_event_from_dict = WebhooksDeliveryEvent.from_dict(webhooks_delivery_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


