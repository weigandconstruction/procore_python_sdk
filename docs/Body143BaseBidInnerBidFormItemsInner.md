# Body143BaseBidInnerBidFormItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_code_id** | **int** | Cost Code ID | [optional] 
**description** | **str** | Bid Form Item Description | [optional] 
**position** | **int** | Position | [optional] 
**subject** | **str** | Subject for Plain Text Items. | [optional] 
**item_type** | **str** | Bid Form Items can be of various types. This property does determine which one is used. | [optional] 
**response_type** | **str** | Bid Form Items can have various response types. This property determines which one is used. | [optional] 

## Example

```python
from procore_sdk.models.body143_base_bid_inner_bid_form_items_inner import Body143BaseBidInnerBidFormItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body143BaseBidInnerBidFormItemsInner from a JSON string
body143_base_bid_inner_bid_form_items_inner_instance = Body143BaseBidInnerBidFormItemsInner.from_json(json)
# print the JSON string representation of the object
print(Body143BaseBidInnerBidFormItemsInner.to_json())

# convert the object into a dict
body143_base_bid_inner_bid_form_items_inner_dict = body143_base_bid_inner_bid_form_items_inner_instance.to_dict()
# create an instance of Body143BaseBidInnerBidFormItemsInner from a dict
body143_base_bid_inner_bid_form_items_inner_from_dict = Body143BaseBidInnerBidFormItemsInner.from_dict(body143_base_bid_inner_bid_form_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


