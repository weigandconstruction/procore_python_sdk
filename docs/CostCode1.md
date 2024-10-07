# CostCode1

Cost Code object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | Position | [optional] 
**code** | **str** | Cost code, not including parent prefix. e.g., for cost code \&quot;02-300\&quot;, the value of this field should be \&quot;300\&quot;. | 
**name** | **str** | Name | 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Unique identifier for the Origin | [optional] 
**parent_id** | **int** | Unique identifier for the Parent | [optional] 
**standard_cost_code_id** | **int** | Unique identifier for the Standard Cost Code | [optional] 

## Example

```python
from procore_sdk.models.cost_code1 import CostCode1

# TODO update the JSON string below
json = "{}"
# create an instance of CostCode1 from a JSON string
cost_code1_instance = CostCode1.from_json(json)
# print the JSON string representation of the object
print(CostCode1.to_json())

# convert the object into a dict
cost_code1_dict = cost_code1_instance.to_dict()
# create an instance of CostCode1 from a dict
cost_code1_from_dict = CostCode1.from_dict(cost_code1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


