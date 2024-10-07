# RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | **str** | Edit link | [optional] 
**view** | **str** | View link | [optional] 
**contract** | **str** | Contract link | [optional] 
**commitment_contract_cost** | **str** | Commitment Contract cost link | [optional] 
**commitment_pco_cost** | **str** | Commitment PCO cost link | [optional] 
**rfq_amount** | **str** | RFQ amount link | [optional] 
**rom** | **str** | ROM link | [optional] 
**prime_pco_cost** | **str** | Prime PCO cost link | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner_links import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks from a JSON string
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_links_instance = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks.to_json())

# convert the object into a dict
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_links_dict = rest_v10_change_events_get200_response_inner_change_event_line_items_inner_links_instance.to_dict()
# create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks from a dict
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_links_from_dict = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks.from_dict(rest_v10_change_events_get200_response_inner_change_event_line_items_inner_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


