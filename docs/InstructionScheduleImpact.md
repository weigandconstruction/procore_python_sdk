# InstructionScheduleImpact

The Schedule Impact of the Instruction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The Status of the Schedule Impact | [optional] 
**value** | **int** | The Value in days of the Schedule Impact | [optional] 

## Example

```python
from procore_sdk.models.instruction_schedule_impact import InstructionScheduleImpact

# TODO update the JSON string below
json = "{}"
# create an instance of InstructionScheduleImpact from a JSON string
instruction_schedule_impact_instance = InstructionScheduleImpact.from_json(json)
# print the JSON string representation of the object
print(InstructionScheduleImpact.to_json())

# convert the object into a dict
instruction_schedule_impact_dict = instruction_schedule_impact_instance.to_dict()
# create an instance of InstructionScheduleImpact from a dict
instruction_schedule_impact_from_dict = InstructionScheduleImpact.from_dict(instruction_schedule_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


