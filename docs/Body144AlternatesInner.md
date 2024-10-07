# Body144AlternatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Alternate Bid Form Item Title | [optional] 
**position** | **int** | Position | [optional] 
**header** | **bool** | Whether the item is a header or not | [optional] 
**bid_form_items** | [**List[Body144BaseBidInnerBidFormItemsInner]**](Body144BaseBidInnerBidFormItemsInner.md) | Bid Form Items | [optional] 
**sub_sections** | [**List[Body144BaseBidInnerSubSectionsInner]**](Body144BaseBidInnerSubSectionsInner.md) | Sub Sections | [optional] 

## Example

```python
from procore_sdk.models.body144_alternates_inner import Body144AlternatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body144AlternatesInner from a JSON string
body144_alternates_inner_instance = Body144AlternatesInner.from_json(json)
# print the JSON string representation of the object
print(Body144AlternatesInner.to_json())

# convert the object into a dict
body144_alternates_inner_dict = body144_alternates_inner_instance.to_dict()
# create an instance of Body144AlternatesInner from a dict
body144_alternates_inner_from_dict = Body144AlternatesInner.from_dict(body144_alternates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


