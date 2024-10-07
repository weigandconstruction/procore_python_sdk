# Body143BaseBidInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Base Bid Form Item Title | [optional] 
**position** | **int** | Position | [optional] 
**header** | **bool** | Whether the item is a header or not | [optional] 
**bid_form_items** | [**List[Body143BaseBidInnerBidFormItemsInner]**](Body143BaseBidInnerBidFormItemsInner.md) | Bid Form Items | [optional] 
**sub_sections** | [**List[Body143BaseBidInnerSubSectionsInner]**](Body143BaseBidInnerSubSectionsInner.md) | Sub Sections | [optional] 

## Example

```python
from procore_sdk.models.body143_base_bid_inner import Body143BaseBidInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body143BaseBidInner from a JSON string
body143_base_bid_inner_instance = Body143BaseBidInner.from_json(json)
# print the JSON string representation of the object
print(Body143BaseBidInner.to_json())

# convert the object into a dict
body143_base_bid_inner_dict = body143_base_bid_inner_instance.to_dict()
# create an instance of Body143BaseBidInner from a dict
body143_base_bid_inner_from_dict = Body143BaseBidInner.from_dict(body143_base_bid_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


