# Body144BaseBidInnerSubSectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**title** | **str** | Sub Section Title | [optional] 
**position** | **int** | Position | [optional] 
**bid_form_items** | [**List[Body143BaseBidInnerBidFormItemsInner]**](Body143BaseBidInnerBidFormItemsInner.md) | Bid Form Items | [optional] 

## Example

```python
from procore_sdk.models.body144_base_bid_inner_sub_sections_inner import Body144BaseBidInnerSubSectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body144BaseBidInnerSubSectionsInner from a JSON string
body144_base_bid_inner_sub_sections_inner_instance = Body144BaseBidInnerSubSectionsInner.from_json(json)
# print the JSON string representation of the object
print(Body144BaseBidInnerSubSectionsInner.to_json())

# convert the object into a dict
body144_base_bid_inner_sub_sections_inner_dict = body144_base_bid_inner_sub_sections_inner_instance.to_dict()
# create an instance of Body144BaseBidInnerSubSectionsInner from a dict
body144_base_bid_inner_sub_sections_inner_from_dict = Body144BaseBidInnerSubSectionsInner.from_dict(body144_base_bid_inner_sub_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


