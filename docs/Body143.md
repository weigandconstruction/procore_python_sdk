# Body143


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Bid Form Title | 
**base_bid** | [**List[Body143BaseBidInner]**](Body143BaseBidInner.md) | Base Bids | [optional] 
**alternates** | [**List[Body143AlternatesInner]**](Body143AlternatesInner.md) | Alternate bids | [optional] 

## Example

```python
from procore_sdk.models.body143 import Body143

# TODO update the JSON string below
json = "{}"
# create an instance of Body143 from a JSON string
body143_instance = Body143.from_json(json)
# print the JSON string representation of the object
print(Body143.to_json())

# convert the object into a dict
body143_dict = body143_instance.to_dict()
# create an instance of Body143 from a dict
body143_from_dict = Body143.from_dict(body143_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


