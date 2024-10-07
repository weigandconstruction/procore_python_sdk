# Body144BaseBidInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Base Bid Form Item Title | [optional] 
**position** | **int** | Position | [optional] 
**header** | **bool** | Whether the item is a header or not | [optional] 
**bid_form_items** | [**List[Body144BaseBidInnerBidFormItemsInner]**](Body144BaseBidInnerBidFormItemsInner.md) | Bid Form Items | [optional] 
**sub_sections** | [**List[Body144BaseBidInnerSubSectionsInner]**](Body144BaseBidInnerSubSectionsInner.md) | Sub Sections | [optional] 

## Example

```python
from procore_sdk.models.body144_base_bid_inner import Body144BaseBidInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body144BaseBidInner from a JSON string
body144_base_bid_inner_instance = Body144BaseBidInner.from_json(json)
# print the JSON string representation of the object
print(Body144BaseBidInner.to_json())

# convert the object into a dict
body144_base_bid_inner_dict = body144_base_bid_inner_instance.to_dict()
# create an instance of Body144BaseBidInner from a dict
body144_base_bid_inner_from_dict = Body144BaseBidInner.from_dict(body144_base_bid_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


