# BidFormBaseBidSectionBidFormItemsInner

A row of bid items for a cost code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bid Form Item ID | [optional] 
**cost_code_id** | **int** | Cost code ID | [optional] 
**full_code** | **str** | The Cost code Name &amp; Number in one string | [optional] 
**name** | **str** | Cost Code Name | [optional] 
**description** | **str** | Description | [optional] 
**number** | **str** | Cost Code Number | [optional] 
**item_type** | **str** | Line Item Type | [optional] 
**subject** | **str** | Plain text subject | [optional] 
**response_type** | **str** | Bid Form Items can have various response types. This property determines which one is used. | [optional] 
**bid_items** | [**List[BidFormBaseBidSectionBidFormItemsInnerBidItemsInner]**](BidFormBaseBidSectionBidFormItemsInnerBidItemsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bid_form_base_bid_section_bid_form_items_inner import BidFormBaseBidSectionBidFormItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BidFormBaseBidSectionBidFormItemsInner from a JSON string
bid_form_base_bid_section_bid_form_items_inner_instance = BidFormBaseBidSectionBidFormItemsInner.from_json(json)
# print the JSON string representation of the object
print(BidFormBaseBidSectionBidFormItemsInner.to_json())

# convert the object into a dict
bid_form_base_bid_section_bid_form_items_inner_dict = bid_form_base_bid_section_bid_form_items_inner_instance.to_dict()
# create an instance of BidFormBaseBidSectionBidFormItemsInner from a dict
bid_form_base_bid_section_bid_form_items_inner_from_dict = BidFormBaseBidSectionBidFormItemsInner.from_dict(bid_form_base_bid_section_bid_form_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


