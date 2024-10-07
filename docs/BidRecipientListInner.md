# BidRecipientListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** | Recipients first name | [optional] 
**last** | **str** | Recipients last name | [optional] 
**email** | **str** | Recipients email | [optional] 
**numbers** | **str** | Recipients office and mobile numbers | [optional] 

## Example

```python
from procore_sdk.models.bid_recipient_list_inner import BidRecipientListInner

# TODO update the JSON string below
json = "{}"
# create an instance of BidRecipientListInner from a JSON string
bid_recipient_list_inner_instance = BidRecipientListInner.from_json(json)
# print the JSON string representation of the object
print(BidRecipientListInner.to_json())

# convert the object into a dict
bid_recipient_list_inner_dict = bid_recipient_list_inner_instance.to_dict()
# create an instance of BidRecipientListInner from a dict
bid_recipient_list_inner_from_dict = BidRecipientListInner.from_dict(bid_recipient_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


