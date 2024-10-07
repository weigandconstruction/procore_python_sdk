# BidFormBaseBidSectionBidFormItemsInnerBidItemsInner

A bid form item row for bid leveling table

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bid Item ID | [optional] 
**bid_id** | **int** | Bid ID | [optional] 
**bid_item_id** | **int** | Bid Item ID | [optional] 
**vendor_id** | **int** | Vendor ID | [optional] 
**amount** | **float** | Cost to complete a cost code. Only used in Amount-based Accounting Bid packages | [optional] 
**unit_cost** | **str** | Cost of each unit. Only used in Unit-based Accounting Bid packages | [optional] 
**quantity** | **str** | Quantity of units. Only used in Unit-based Accounting Bid packages | [optional] 
**uom** | **str** | Unit of Measure. Only used in Unit-based Accounting Bid packages | [optional] 
**included** | **bool** | Indicates whether a line item is included in the bid or not. | [optional] 

## Example

```python
from procore_sdk.models.bid_form_base_bid_section_bid_form_items_inner_bid_items_inner import BidFormBaseBidSectionBidFormItemsInnerBidItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BidFormBaseBidSectionBidFormItemsInnerBidItemsInner from a JSON string
bid_form_base_bid_section_bid_form_items_inner_bid_items_inner_instance = BidFormBaseBidSectionBidFormItemsInnerBidItemsInner.from_json(json)
# print the JSON string representation of the object
print(BidFormBaseBidSectionBidFormItemsInnerBidItemsInner.to_json())

# convert the object into a dict
bid_form_base_bid_section_bid_form_items_inner_bid_items_inner_dict = bid_form_base_bid_section_bid_form_items_inner_bid_items_inner_instance.to_dict()
# create an instance of BidFormBaseBidSectionBidFormItemsInnerBidItemsInner from a dict
bid_form_base_bid_section_bid_form_items_inner_bid_items_inner_from_dict = BidFormBaseBidSectionBidFormItemsInnerBidItemsInner.from_dict(bid_form_base_bid_section_bid_form_items_inner_bid_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


