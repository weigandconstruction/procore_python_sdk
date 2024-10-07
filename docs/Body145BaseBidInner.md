# Body145BaseBidInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Base Bid Form Item Title | [optional] 
**position** | **int** | Position | [optional] 
**header** | **bool** | Whether the item is a header or not | [optional] 
**bid_form_items** | [**List[Body145BaseBidInnerBidFormItemsInner]**](Body145BaseBidInnerBidFormItemsInner.md) | Bid Form Items | [optional] 

## Example

```python
from procore_sdk.models.body145_base_bid_inner import Body145BaseBidInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body145BaseBidInner from a JSON string
body145_base_bid_inner_instance = Body145BaseBidInner.from_json(json)
# print the JSON string representation of the object
print(Body145BaseBidInner.to_json())

# convert the object into a dict
body145_base_bid_inner_dict = body145_base_bid_inner_instance.to_dict()
# create an instance of Body145BaseBidInner from a dict
body145_base_bid_inner_from_dict = Body145BaseBidInner.from_dict(body145_base_bid_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


