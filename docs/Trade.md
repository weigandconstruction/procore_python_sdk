# Trade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Trade ID | [optional] 
**name** | **str** | Trade name | [optional] 
**active** | **bool** | Trade availability | [optional] 
**updated_at** | **datetime** | Timestamp of last update to Trade | [optional] 

## Example

```python
from procore_sdk.models.trade import Trade

# TODO update the JSON string below
json = "{}"
# create an instance of Trade from a JSON string
trade_instance = Trade.from_json(json)
# print the JSON string representation of the object
print(Trade.to_json())

# convert the object into a dict
trade_dict = trade_instance.to_dict()
# create an instance of Trade from a dict
trade_from_dict = Trade.from_dict(trade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


