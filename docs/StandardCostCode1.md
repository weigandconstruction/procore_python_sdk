# StandardCostCode1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int** | Parent ID (creates a root Standard Cost Code if not provided) | [optional] 
**code** | **str** | Cost code, not including parent prefix | [optional] 
**name** | **str** | Description | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.standard_cost_code1 import StandardCostCode1

# TODO update the JSON string below
json = "{}"
# create an instance of StandardCostCode1 from a JSON string
standard_cost_code1_instance = StandardCostCode1.from_json(json)
# print the JSON string representation of the object
print(StandardCostCode1.to_json())

# convert the object into a dict
standard_cost_code1_dict = standard_cost_code1_instance.to_dict()
# create an instance of StandardCostCode1 from a dict
standard_cost_code1_from_dict = StandardCostCode1.from_dict(standard_cost_code1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


