# CostCode

Cost Code object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_id** | **int** | Position | [optional] 
**name** | **str** | Crew Name | [optional] 
**employee_ids** | **List[int]** |  | [optional] 

## Example

```python
from procore_sdk.models.cost_code import CostCode

# TODO update the JSON string below
json = "{}"
# create an instance of CostCode from a JSON string
cost_code_instance = CostCode.from_json(json)
# print the JSON string representation of the object
print(CostCode.to_json())

# convert the object into a dict
cost_code_dict = cost_code_instance.to_dict()
# create an instance of CostCode from a dict
cost_code_from_dict = CostCode.from_dict(cost_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


