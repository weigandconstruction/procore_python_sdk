# BidForm1

Bid Form

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | [optional] 
**project_id** | **int** | Project ID | [optional] 
**accounting_method** | **str** |  | [optional] 
**company_name** | **str** | Company Name | [optional] 
**project_name** | **str** | Project Name | [optional] 
**base_bid_totals** | [**List[BidFormBaseBidSectionSectionTotalsInner]**](BidFormBaseBidSectionSectionTotalsInner.md) |  | [optional] 
**base_bid** | [**List[BidFormBaseBidSectionBidFormItemsInner]**](BidFormBaseBidSectionBidFormItemsInner.md) |  | [optional] 
**alternates** | [**List[BidFormBaseBidSectionBidFormItemsInner]**](BidFormBaseBidSectionBidFormItemsInner.md) |  | [optional] 
**lump_sum_enabled** | **bool** | Lump Sum Enabled | [optional] 
**title** | **str** | Title | [optional] 

## Example

```python
from procore_sdk.models.bid_form1 import BidForm1

# TODO update the JSON string below
json = "{}"
# create an instance of BidForm1 from a JSON string
bid_form1_instance = BidForm1.from_json(json)
# print the JSON string representation of the object
print(BidForm1.to_json())

# convert the object into a dict
bid_form1_dict = bid_form1_instance.to_dict()
# create an instance of BidForm1 from a dict
bid_form1_from_dict = BidForm1.from_dict(bid_form1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


