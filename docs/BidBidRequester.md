# BidBidRequester

Bid Requester Info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** | The bid requesters company name | [optional] 
**contact** | **str** | The bid requester&#39;s contact information | [optional] 
**company_address** | **str** | Bid requesters company address | [optional] 
**company_phone** | **str** | Bid requesters company phone | [optional] 
**company_website** | **str** | Bid requesters company website | [optional] 
**email_address** | **str** | Bid requesters email_address | [optional] 
**first_name** | **str** | Bid requesters first_name | [optional] 
**last_name** | **str** | Bid requesters last_name | [optional] 
**mobile_phone** | **str** | Bid requesters mobile number | [optional] 
**vendor_address** | **str** | Bid requesters company address | [optional] 
**business_phone** | **str** | Bid requesters company phone number | [optional] 
**fax_number** | **str** | Bid requesters company fax number | [optional] 

## Example

```python
from procore_sdk.models.bid_bid_requester import BidBidRequester

# TODO update the JSON string below
json = "{}"
# create an instance of BidBidRequester from a JSON string
bid_bid_requester_instance = BidBidRequester.from_json(json)
# print the JSON string representation of the object
print(BidBidRequester.to_json())

# convert the object into a dict
bid_bid_requester_dict = bid_bid_requester_instance.to_dict()
# create an instance of BidBidRequester from a dict
bid_bid_requester_from_dict = BidBidRequester.from_dict(bid_bid_requester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


