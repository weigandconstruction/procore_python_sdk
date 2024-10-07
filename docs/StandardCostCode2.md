# StandardCostCode2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int** | Parent ID (keeps the same Parent ID as before if not provided) | [optional] 
**code** | **str** | Cost code, not including parent prefix | [optional] 
**name** | **str** | Description | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.standard_cost_code2 import StandardCostCode2

# TODO update the JSON string below
json = "{}"
# create an instance of StandardCostCode2 from a JSON string
standard_cost_code2_instance = StandardCostCode2.from_json(json)
# print the JSON string representation of the object
print(StandardCostCode2.to_json())

# convert the object into a dict
standard_cost_code2_dict = standard_cost_code2_instance.to_dict()
# create an instance of StandardCostCode2 from a dict
standard_cost_code2_from_dict = StandardCostCode2.from_dict(standard_cost_code2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


