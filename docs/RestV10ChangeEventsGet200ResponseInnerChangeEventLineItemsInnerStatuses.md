# RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | Contract status | [optional] 
**commitment_contract_cost** | **str** | Commitment Contract Cost status | [optional] 
**commitment_contract_tooltip** | **str** | Commitment Contract tooltip | [optional] 
**commitment_pco_cost** | **str** | Commitment PCO cost status | [optional] 
**commitment_pco_tooltip** | **str** | Commitment PCO tooltip | [optional] 
**rfq_amount** | **str** | RFQ Amount status | [optional] 
**rfq_tooltip** | **str** | RFQ tooltip | [optional] 
**prime_pco_cost** | **str** | Prime PCO Cost status | [optional] 
**prime_pco_tooltip** | **str** | Prime PCO tooltip | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner_statuses import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses from a JSON string
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_statuses_instance = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses.to_json())

# convert the object into a dict
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_statuses_dict = rest_v10_change_events_get200_response_inner_change_event_line_items_inner_statuses_instance.to_dict()
# create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses from a dict
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_statuses_from_dict = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses.from_dict(rest_v10_change_events_get200_response_inner_change_event_line_items_inner_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


