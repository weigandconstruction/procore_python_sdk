# Instruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | The Number of the Instruction | [optional] 
**title** | **str** | The Title of the Instruction | 
**status** | **str** | The Status of the Instruction | 
**instruction_type_id** | **int** | ID of the Instruction Type | 
**instruction_from_id** | **int** | ID of the User who the Instruction is from | [optional] 
**date_received** | **date** |  | [optional] 
**schedule_impact** | [**InstructionScheduleImpact**](InstructionScheduleImpact.md) |  | [optional] 
**cost_impact** | [**InstructionCostImpact**](InstructionCostImpact.md) |  | [optional] 
**private** | **bool** | The Private status of the Instruction | [optional] [default to False]
**description** | **str** | The Description of the Instruction | [optional] 
**attention_ids** | **List[int]** | An array of IDs of the Attentions of the Instruction | [optional] 
**distribution_member_ids** | **List[int]** | An array of IDs of the Distributions of the Instruction | [optional] 
**trade_ids** | **List[int]** | An array of IDs of the Trades of the Instruction | [optional] 
**attachments** | **List[str]** | Instruction&#39;s Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.instruction import Instruction

# TODO update the JSON string below
json = "{}"
# create an instance of Instruction from a JSON string
instruction_instance = Instruction.from_json(json)
# print the JSON string representation of the object
print(Instruction.to_json())

# convert the object into a dict
instruction_dict = instruction_instance.to_dict()
# create an instance of Instruction from a dict
instruction_from_dict = Instruction.from_dict(instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


