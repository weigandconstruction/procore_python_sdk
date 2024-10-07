# StandardCostCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**standard_cost_code_list_id** | **int** | Standard Cost Code List ID | [optional] 
**parent_id** | **int** | Parent ID | [optional] 
**code** | **str** | Cost code, not including parent prefix | [optional] 
**full_code** | **str** | Cost code, including parent prefixes | [optional] 
**name** | **str** | Description | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.standard_cost_code import StandardCostCode

# TODO update the JSON string below
json = "{}"
# create an instance of StandardCostCode from a JSON string
standard_cost_code_instance = StandardCostCode.from_json(json)
# print the JSON string representation of the object
print(StandardCostCode.to_json())

# convert the object into a dict
standard_cost_code_dict = standard_cost_code_instance.to_dict()
# create an instance of StandardCostCode from a dict
standard_cost_code_from_dict = StandardCostCode.from_dict(standard_cost_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


