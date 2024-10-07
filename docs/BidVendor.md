# BidVendor

Bid Vendor Info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**avatar_url** | **str** | Link to avatar picture | [optional] 
**trades** | **str** | List of trades for the vendor | [optional] 

## Example

```python
from procore_sdk.models.bid_vendor import BidVendor

# TODO update the JSON string below
json = "{}"
# create an instance of BidVendor from a JSON string
bid_vendor_instance = BidVendor.from_json(json)
# print the JSON string representation of the object
print(BidVendor.to_json())

# convert the object into a dict
bid_vendor_dict = bid_vendor_instance.to_dict()
# create an instance of BidVendor from a dict
bid_vendor_from_dict = BidVendor.from_dict(bid_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


