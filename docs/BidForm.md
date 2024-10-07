# BidForm

Bid Form

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | [optional] 
**project_id** | **int** | Project ID | [optional] 
**accounting_method** | **str** |  | [optional] 
**company_name** | **str** | Company Name | [optional] 
**project_name** | **str** | Project Name | [optional] 
**base_bid_section** | [**BidFormBaseBidSection**](BidFormBaseBidSection.md) |  | [optional] 
**alternates_section** | [**BidFormBaseBidSection**](BidFormBaseBidSection.md) |  | [optional] 
**lump_sum_enabled** | **bool** | Lump Sum Enabled | [optional] 
**title** | **str** | Title | [optional] 

## Example

```python
from procore_sdk.models.bid_form import BidForm

# TODO update the JSON string below
json = "{}"
# create an instance of BidForm from a JSON string
bid_form_instance = BidForm.from_json(json)
# print the JSON string representation of the object
print(BidForm.to_json())

# convert the object into a dict
bid_form_dict = bid_form_instance.to_dict()
# create an instance of BidForm from a dict
bid_form_from_dict = BidForm.from_dict(bid_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


