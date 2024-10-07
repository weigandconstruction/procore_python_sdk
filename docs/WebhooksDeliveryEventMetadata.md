# WebhooksDeliveryEventMetadata

Contextual information about the event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_user_id** | **int** | ID of the user who made the change | [optional] 
**source_company_id** | **int** | ID of the company that the changing user was in when the change was made | [optional] 
**source_project_id** | **int** | ID of the project that the changing user was in when the change was made | [optional] 
**source_application_id** | **str** | ID of the application used to make the change | [optional] 
**source_operation_id** | **str** | Identifying token provided by the client on the api request that was responsible for the change | [optional] 

## Example

```python
from procore_sdk.models.webhooks_delivery_event_metadata import WebhooksDeliveryEventMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksDeliveryEventMetadata from a JSON string
webhooks_delivery_event_metadata_instance = WebhooksDeliveryEventMetadata.from_json(json)
# print the JSON string representation of the object
print(WebhooksDeliveryEventMetadata.to_json())

# convert the object into a dict
webhooks_delivery_event_metadata_dict = webhooks_delivery_event_metadata_instance.to_dict()
# create an instance of WebhooksDeliveryEventMetadata from a dict
webhooks_delivery_event_metadata_from_dict = WebhooksDeliveryEventMetadata.from_dict(webhooks_delivery_event_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


