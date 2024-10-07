# WebhooksResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | API Version | [optional] 
**product_category** | **str** | Product Category | [optional] 
**tools** | **str** | Tools | [optional] 
**var_except** | **List[str]** | Event types that cannot be subscribed to | [optional] 
**create** | **str** | Create Event | [optional] 
**update** | **str** | Update Event | [optional] 
**delete** | **str** | Delete Event | [optional] 

## Example

```python
from procore_sdk.models.webhooks_resource import WebhooksResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksResource from a JSON string
webhooks_resource_instance = WebhooksResource.from_json(json)
# print the JSON string representation of the object
print(WebhooksResource.to_json())

# convert the object into a dict
webhooks_resource_dict = webhooks_resource_instance.to_dict()
# create an instance of WebhooksResource from a dict
webhooks_resource_from_dict = WebhooksResource.from_dict(webhooks_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


