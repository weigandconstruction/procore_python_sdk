# RFQChangeEventChangeEventLineItemsInnerLinks

Links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | **str** | Edit link | [optional] 
**view** | **str** | View link | [optional] 
**contract** | **str** | Contract link | [optional] 
**prime_pco_cost** | **str** | Prime Potential Change Order (PCO) link | [optional] 
**commitment_contract_cost** | **str** | Commitment Contract cost link | [optional] 
**commitment_pco_cost** | **str** | Commitment Potential Change Order (PCO) cost link | [optional] 
**rfq_amount** | **str** | RFQ amount link | [optional] 
**rom** | **str** | Rough order of magnitude (ROM) link | [optional] 

## Example

```python
from procore_sdk.models.rfq_change_event_change_event_line_items_inner_links import RFQChangeEventChangeEventLineItemsInnerLinks

# TODO update the JSON string below
json = "{}"
# create an instance of RFQChangeEventChangeEventLineItemsInnerLinks from a JSON string
rfq_change_event_change_event_line_items_inner_links_instance = RFQChangeEventChangeEventLineItemsInnerLinks.from_json(json)
# print the JSON string representation of the object
print(RFQChangeEventChangeEventLineItemsInnerLinks.to_json())

# convert the object into a dict
rfq_change_event_change_event_line_items_inner_links_dict = rfq_change_event_change_event_line_items_inner_links_instance.to_dict()
# create an instance of RFQChangeEventChangeEventLineItemsInnerLinks from a dict
rfq_change_event_change_event_line_items_inner_links_from_dict = RFQChangeEventChangeEventLineItemsInnerLinks.from_dict(rfq_change_event_change_event_line_items_inner_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


