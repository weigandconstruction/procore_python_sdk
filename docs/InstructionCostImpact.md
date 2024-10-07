# InstructionCostImpact

The Cost Impact of the Instruction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The Status of the Cost Impact | [optional] 
**value** | **float** | Cost impact value in dollars | [optional] 

## Example

```python
from procore_sdk.models.instruction_cost_impact import InstructionCostImpact

# TODO update the JSON string below
json = "{}"
# create an instance of InstructionCostImpact from a JSON string
instruction_cost_impact_instance = InstructionCostImpact.from_json(json)
# print the JSON string representation of the object
print(InstructionCostImpact.to_json())

# convert the object into a dict
instruction_cost_impact_dict = instruction_cost_impact_instance.to_dict()
# create an instance of InstructionCostImpact from a dict
instruction_cost_impact_from_dict = InstructionCostImpact.from_dict(instruction_cost_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


