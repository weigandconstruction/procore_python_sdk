# BidFormBaseBidSectionSubSectionsInner

Bid Form Section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**title** | **str** | Bid Form Title | [optional] 
**position** | **int** | Position | [optional] 
**section_totals** | [**List[BidFormBaseBidSectionSectionTotalsInner]**](BidFormBaseBidSectionSectionTotalsInner.md) |  | [optional] 
**bid_form_items** | [**List[BidFormBaseBidSectionBidFormItemsInner]**](BidFormBaseBidSectionBidFormItemsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bid_form_base_bid_section_sub_sections_inner import BidFormBaseBidSectionSubSectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BidFormBaseBidSectionSubSectionsInner from a JSON string
bid_form_base_bid_section_sub_sections_inner_instance = BidFormBaseBidSectionSubSectionsInner.from_json(json)
# print the JSON string representation of the object
print(BidFormBaseBidSectionSubSectionsInner.to_json())

# convert the object into a dict
bid_form_base_bid_section_sub_sections_inner_dict = bid_form_base_bid_section_sub_sections_inner_instance.to_dict()
# create an instance of BidFormBaseBidSectionSubSectionsInner from a dict
bid_form_base_bid_section_sub_sections_inner_from_dict = BidFormBaseBidSectionSubSectionsInner.from_dict(bid_form_base_bid_section_sub_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


