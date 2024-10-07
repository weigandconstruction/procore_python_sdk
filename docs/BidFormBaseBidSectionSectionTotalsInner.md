# BidFormBaseBidSectionSectionTotalsInner

Base Bid Columns

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid_id** | **int** | Bid ID | [optional] 
**vendor_id** | **int** | Vendor ID | [optional] 
**vendor_name** | **str** | Vendor Name | [optional] 
**total** | **float** | Total of all base bid items | [optional] 

## Example

```python
from procore_sdk.models.bid_form_base_bid_section_section_totals_inner import BidFormBaseBidSectionSectionTotalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BidFormBaseBidSectionSectionTotalsInner from a JSON string
bid_form_base_bid_section_section_totals_inner_instance = BidFormBaseBidSectionSectionTotalsInner.from_json(json)
# print the JSON string representation of the object
print(BidFormBaseBidSectionSectionTotalsInner.to_json())

# convert the object into a dict
bid_form_base_bid_section_section_totals_inner_dict = bid_form_base_bid_section_section_totals_inner_instance.to_dict()
# create an instance of BidFormBaseBidSectionSectionTotalsInner from a dict
bid_form_base_bid_section_section_totals_inner_from_dict = BidFormBaseBidSectionSectionTotalsInner.from_dict(bid_form_base_bid_section_section_totals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


