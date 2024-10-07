# RFQChangeEventChangeEventLineItemsInnerStatuses

Statuses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | Contract status | [optional] 
**commitment_contract_cost** | **str** | Commitment contract cost status | [optional] 
**commitment_pco_cost** | **str** | Commitment Potential Change Order cost status | [optional] 
**prime_pco_cost** | **str** | Prime Potential Change Order cost status | [optional] 
**rfq_amount** | **str** | RFQ status | [optional] 

## Example

```python
from procore_sdk.models.rfq_change_event_change_event_line_items_inner_statuses import RFQChangeEventChangeEventLineItemsInnerStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of RFQChangeEventChangeEventLineItemsInnerStatuses from a JSON string
rfq_change_event_change_event_line_items_inner_statuses_instance = RFQChangeEventChangeEventLineItemsInnerStatuses.from_json(json)
# print the JSON string representation of the object
print(RFQChangeEventChangeEventLineItemsInnerStatuses.to_json())

# convert the object into a dict
rfq_change_event_change_event_line_items_inner_statuses_dict = rfq_change_event_change_event_line_items_inner_statuses_instance.to_dict()
# create an instance of RFQChangeEventChangeEventLineItemsInnerStatuses from a dict
rfq_change_event_change_event_line_items_inner_statuses_from_dict = RFQChangeEventChangeEventLineItemsInnerStatuses.from_dict(rfq_change_event_change_event_line_items_inner_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


