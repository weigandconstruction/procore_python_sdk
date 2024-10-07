# Body143BaseBidInnerSubSectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Sub Section Title | [optional] 
**bid_form_items** | [**List[Body143BaseBidInnerBidFormItemsInner]**](Body143BaseBidInnerBidFormItemsInner.md) | Bid Form Items | [optional] 

## Example

```python
from procore_sdk.models.body143_base_bid_inner_sub_sections_inner import Body143BaseBidInnerSubSectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body143BaseBidInnerSubSectionsInner from a JSON string
body143_base_bid_inner_sub_sections_inner_instance = Body143BaseBidInnerSubSectionsInner.from_json(json)
# print the JSON string representation of the object
print(Body143BaseBidInnerSubSectionsInner.to_json())

# convert the object into a dict
body143_base_bid_inner_sub_sections_inner_dict = body143_base_bid_inner_sub_sections_inner_instance.to_dict()
# create an instance of Body143BaseBidInnerSubSectionsInner from a dict
body143_base_bid_inner_sub_sections_inner_from_dict = Body143BaseBidInnerSubSectionsInner.from_dict(body143_base_bid_inner_sub_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


