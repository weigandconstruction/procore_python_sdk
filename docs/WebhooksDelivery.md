# WebhooksDelivery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**WebhooksDeliveryEvent**](WebhooksDeliveryEvent.md) |  | [optional] 
**event_id** | **int** | ID of the audited API event | [optional] 
**outcome** | **str** | Outcome of the delivery | [optional] 
**response_body** | **str** | Reponse body returned from the request, if any. | [optional] 
**response_error** | **str** | Error response message, if any. | [optional] 
**started_at** | **datetime** | Start time of the request | [optional] 
**completed_at** | **datetime** | Completion time of the request | [optional] 
**response_status** | **int** | Status code returned from the request. | [optional] 
**response_headers** | **object** | Headers returned from the request. | [optional] 

## Example

```python
from procore_sdk.models.webhooks_delivery import WebhooksDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksDelivery from a JSON string
webhooks_delivery_instance = WebhooksDelivery.from_json(json)
# print the JSON string representation of the object
print(WebhooksDelivery.to_json())

# convert the object into a dict
webhooks_delivery_dict = webhooks_delivery_instance.to_dict()
# create an instance of WebhooksDelivery from a dict
webhooks_delivery_from_dict = WebhooksDelivery.from_dict(webhooks_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


