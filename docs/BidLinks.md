# BidLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uploads** | **str** | Upload link for current company | [optional] 
**cost_codes** | **str** | Available cost codes link for bid | [optional] 
**bid_pdf** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.bid_links import BidLinks

# TODO update the JSON string below
json = "{}"
# create an instance of BidLinks from a JSON string
bid_links_instance = BidLinks.from_json(json)
# print the JSON string representation of the object
print(BidLinks.to_json())

# convert the object into a dict
bid_links_dict = bid_links_instance.to_dict()
# create an instance of BidLinks from a dict
bid_links_from_dict = BidLinks.from_dict(bid_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


