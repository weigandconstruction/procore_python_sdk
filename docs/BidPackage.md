# BidPackage

Bid Package Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid_due_date** | **datetime** | Due date | 
**bid_email_message** | **str** | Bid package email information details | 
**bid_web_message** | **str** | Bid package bidding instructions | 
**title** | **str** | Bid package title | 
**accounting_method** | **str** | Bid package accounting method, either &#39;amount&#39; or &#39;unit&#39; | [optional] 
**bid_submission_confirmation** | **str** | Bid Package submission confirmation text | [optional] 
**anticipated_award_date** | **date** | Anticipated award date | [optional] 
**number** | **str** | Bid package number | [optional] 
**distribution_ids** | **List[int]** | Array of User IDs who will be on the bid package&#39;s distribution list | [optional] 
**blind_bidding** | **bool** | Blind bidding enabled | [optional] 
**pre_bid_walk_through_date** | **datetime** | Scheduled pre-bid walkthrough date | [optional] 
**pre_bid_walk_through_notes** | **str** | Pre-bid walkthrough notes | [optional] 
**enable_prebid_walkthrough** | **bool** | Pre-bid walkthrough enabled | [optional] 
**manager_id** | **int** | Login Information ID for Manager | [optional] 

## Example

```python
from procore_sdk.models.bid_package import BidPackage

# TODO update the JSON string below
json = "{}"
# create an instance of BidPackage from a JSON string
bid_package_instance = BidPackage.from_json(json)
# print the JSON string representation of the object
print(BidPackage.to_json())

# convert the object into a dict
bid_package_dict = bid_package_instance.to_dict()
# create an instance of BidPackage from a dict
bid_package_from_dict = BidPackage.from_dict(bid_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


