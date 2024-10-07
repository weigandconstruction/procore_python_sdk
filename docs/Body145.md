# Body145


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Bid Form Title | 
**base_bid** | [**List[Body145BaseBidInner]**](Body145BaseBidInner.md) | Base Bids | [optional] 
**alternates** | [**List[Body145AlternatesInner]**](Body145AlternatesInner.md) | Alternate bids | [optional] 

## Example

```python
from procore_sdk.models.body145 import Body145

# TODO update the JSON string below
json = "{}"
# create an instance of Body145 from a JSON string
body145_instance = Body145.from_json(json)
# print the JSON string representation of the object
print(Body145.to_json())

# convert the object into a dict
body145_dict = body145_instance.to_dict()
# create an instance of Body145 from a dict
body145_from_dict = Body145.from_dict(body145_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


