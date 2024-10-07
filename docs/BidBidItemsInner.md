# BidBidItemsInner

Bid Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount in cents. It&#39;s an optional parameter when the blind bidding is on. | [optional] 
**bid_form_item_id** | **int** | Bid Form Item ID | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**cost_code_name** | **str** | Cost Code name | [optional] 
**cost_code_number** | **str** | Cost Code number | [optional] 
**id** | **int** | ID | [optional] 
**included** | **bool** | Included | [optional] 
**quantity** | **float** | Quantity. It&#39;s an optional parameter when the blind bidding is on. | [optional] 
**unit_cost** | **float** | Unit cost of bid item. It&#39;s an optional parameter when the blind bidding is on. | [optional] 
**uom** | **str** | Unit of Measure. It&#39;s an optional parameter when the blind bidding is on. | [optional] 

## Example

```python
from procore_sdk.models.bid_bid_items_inner import BidBidItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BidBidItemsInner from a JSON string
bid_bid_items_inner_instance = BidBidItemsInner.from_json(json)
# print the JSON string representation of the object
print(BidBidItemsInner.to_json())

# convert the object into a dict
bid_bid_items_inner_dict = bid_bid_items_inner_instance.to_dict()
# create an instance of BidBidItemsInner from a dict
bid_bid_items_inner_from_dict = BidBidItemsInner.from_dict(bid_bid_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


