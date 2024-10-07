# Body143AlternatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Alternate Bid Form Item Title | [optional] 
**position** | **int** | Position | [optional] 
**header** | **bool** | Whether the item is a header or not | [optional] 
**bid_form_items** | [**List[Body143BaseBidInnerBidFormItemsInner]**](Body143BaseBidInnerBidFormItemsInner.md) | Bid Form Items | [optional] 
**sub_sections** | [**List[Body143BaseBidInnerSubSectionsInner]**](Body143BaseBidInnerSubSectionsInner.md) | Sub Sections | [optional] 

## Example

```python
from procore_sdk.models.body143_alternates_inner import Body143AlternatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body143AlternatesInner from a JSON string
body143_alternates_inner_instance = Body143AlternatesInner.from_json(json)
# print the JSON string representation of the object
print(Body143AlternatesInner.to_json())

# convert the object into a dict
body143_alternates_inner_dict = body143_alternates_inner_instance.to_dict()
# create an instance of Body143AlternatesInner from a dict
body143_alternates_inner_from_dict = Body143AlternatesInner.from_dict(body143_alternates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


