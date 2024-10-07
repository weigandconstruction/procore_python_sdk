# Body145AlternatesInnerBidFormItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_code_id** | **int** | Cost Code ID | [optional] 
**description** | **str** | Bid Form Item Description | [optional] 
**position** | **int** | Position | [optional] 
**subject** | **str** | Subject for Plain Text Items | [optional] 
**item_type** | **str** | Bid Form Items can be of various types. This property does determine which one is used. | [optional] 

## Example

```python
from procore_sdk.models.body145_alternates_inner_bid_form_items_inner import Body145AlternatesInnerBidFormItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body145AlternatesInnerBidFormItemsInner from a JSON string
body145_alternates_inner_bid_form_items_inner_instance = Body145AlternatesInnerBidFormItemsInner.from_json(json)
# print the JSON string representation of the object
print(Body145AlternatesInnerBidFormItemsInner.to_json())

# convert the object into a dict
body145_alternates_inner_bid_form_items_inner_dict = body145_alternates_inner_bid_form_items_inner_instance.to_dict()
# create an instance of Body145AlternatesInnerBidFormItemsInner from a dict
body145_alternates_inner_bid_form_items_inner_from_dict = Body145AlternatesInnerBidFormItemsInner.from_dict(body145_alternates_inner_bid_form_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


