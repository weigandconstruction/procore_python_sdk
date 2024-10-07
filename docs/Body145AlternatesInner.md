# Body145AlternatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Alternate Bid Form Item Title | [optional] 
**position** | **int** | Position | [optional] 
**header** | **bool** | Whether the item is a header or not | [optional] 
**bid_form_items** | [**List[Body145AlternatesInnerBidFormItemsInner]**](Body145AlternatesInnerBidFormItemsInner.md) | Bid Form Items | [optional] 

## Example

```python
from procore_sdk.models.body145_alternates_inner import Body145AlternatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body145AlternatesInner from a JSON string
body145_alternates_inner_instance = Body145AlternatesInner.from_json(json)
# print the JSON string representation of the object
print(Body145AlternatesInner.to_json())

# convert the object into a dict
body145_alternates_inner_dict = body145_alternates_inner_instance.to_dict()
# create an instance of Body145AlternatesInner from a dict
body145_alternates_inner_from_dict = Body145AlternatesInner.from_dict(body145_alternates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


