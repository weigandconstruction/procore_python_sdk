# BidFormBaseBidSection

Bid Form Section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**title** | **str** | Bid Form Title | [optional] 
**position** | **int** | Position | [optional] 
**section_totals** | [**List[BidFormBaseBidSectionSectionTotalsInner]**](BidFormBaseBidSectionSectionTotalsInner.md) |  | [optional] 
**bid_form_items** | [**List[BidFormBaseBidSectionBidFormItemsInner]**](BidFormBaseBidSectionBidFormItemsInner.md) |  | [optional] 
**sub_sections** | [**List[BidFormBaseBidSectionSubSectionsInner]**](BidFormBaseBidSectionSubSectionsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bid_form_base_bid_section import BidFormBaseBidSection

# TODO update the JSON string below
json = "{}"
# create an instance of BidFormBaseBidSection from a JSON string
bid_form_base_bid_section_instance = BidFormBaseBidSection.from_json(json)
# print the JSON string representation of the object
print(BidFormBaseBidSection.to_json())

# convert the object into a dict
bid_form_base_bid_section_dict = bid_form_base_bid_section_instance.to_dict()
# create an instance of BidFormBaseBidSection from a dict
bid_form_base_bid_section_from_dict = BidFormBaseBidSection.from_dict(bid_form_base_bid_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


