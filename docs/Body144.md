# Body144


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Bid Form Title | 
**base_bid** | [**List[Body144BaseBidInner]**](Body144BaseBidInner.md) | Base Bids | [optional] 
**alternates** | [**List[Body144AlternatesInner]**](Body144AlternatesInner.md) | Alternate bids | [optional] 

## Example

```python
from procore_sdk.models.body144 import Body144

# TODO update the JSON string below
json = "{}"
# create an instance of Body144 from a JSON string
body144_instance = Body144.from_json(json)
# print the JSON string representation of the object
print(Body144.to_json())

# convert the object into a dict
body144_dict = body144_instance.to_dict()
# create an instance of Body144 from a dict
body144_from_dict = Body144.from_dict(body144_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


