# Compact1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**full_code** | **str** | Full Cost code, including parent prefixes | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**standard_cost_code_id** | **int** | Standard Cost Code ID | [optional] 

## Example

```python
from procore_sdk.models.compact1 import Compact1

# TODO update the JSON string below
json = "{}"
# create an instance of Compact1 from a JSON string
compact1_instance = Compact1.from_json(json)
# print the JSON string representation of the object
print(Compact1.to_json())

# convert the object into a dict
compact1_dict = compact1_instance.to_dict()
# create an instance of Compact1 from a dict
compact1_from_dict = Compact1.from_dict(compact1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


