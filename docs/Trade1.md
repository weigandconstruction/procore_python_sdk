# Trade1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Trade | [optional] 
**active** | **bool** | The availability status of the Trade | [optional] 

## Example

```python
from procore_sdk.models.trade1 import Trade1

# TODO update the JSON string below
json = "{}"
# create an instance of Trade1 from a JSON string
trade1_instance = Trade1.from_json(json)
# print the JSON string representation of the object
print(Trade1.to_json())

# convert the object into a dict
trade1_dict = trade1_instance.to_dict()
# create an instance of Trade1 from a dict
trade1_from_dict = Trade1.from_dict(trade1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


