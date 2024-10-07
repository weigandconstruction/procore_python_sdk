# Body145BaseBidInnerBidFormItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_code_id** | **int** | Cost Code ID | [optional] 
**description** | **str** | Bid Form Item Description | [optional] 
**position** | **int** | Position | [optional] 
**subject** | **str** | Subject for Plain Text Items. | [optional] 
**item_type** | **str** | Bid Form Items can be of various types. This property does determine which one is used. | [optional] 

## Example

```python
from procore_sdk.models.body145_base_bid_inner_bid_form_items_inner import Body145BaseBidInnerBidFormItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body145BaseBidInnerBidFormItemsInner from a JSON string
body145_base_bid_inner_bid_form_items_inner_instance = Body145BaseBidInnerBidFormItemsInner.from_json(json)
# print the JSON string representation of the object
print(Body145BaseBidInnerBidFormItemsInner.to_json())

# convert the object into a dict
body145_base_bid_inner_bid_form_items_inner_dict = body145_base_bid_inner_bid_form_items_inner_instance.to_dict()
# create an instance of Body145BaseBidInnerBidFormItemsInner from a dict
body145_base_bid_inner_bid_form_items_inner_from_dict = Body145BaseBidInnerBidFormItemsInner.from_dict(body145_base_bid_inner_bid_form_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


