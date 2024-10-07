# Trade2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Trade ID | [optional] 
**name** | **str** | Trade name | [optional] 
**active** | **bool** | Trade availability | [optional] 
**updated_at** | **datetime** | Timestamp of last update to Trade | [optional] 

## Example

```python
from procore_sdk.models.trade2 import Trade2

# TODO update the JSON string below
json = "{}"
# create an instance of Trade2 from a JSON string
trade2_instance = Trade2.from_json(json)
# print the JSON string representation of the object
print(Trade2.to_json())

# convert the object into a dict
trade2_dict = trade2_instance.to_dict()
# create an instance of Trade2 from a dict
trade2_from_dict = Trade2.from_dict(trade2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


