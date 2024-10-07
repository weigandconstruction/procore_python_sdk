# InstructionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Instruction Type | 

## Example

```python
from procore_sdk.models.instruction_type import InstructionType

# TODO update the JSON string below
json = "{}"
# create an instance of InstructionType from a JSON string
instruction_type_instance = InstructionType.from_json(json)
# print the JSON string representation of the object
print(InstructionType.to_json())

# convert the object into a dict
instruction_type_dict = instruction_type_instance.to_dict()
# create an instance of InstructionType from a dict
instruction_type_from_dict = InstructionType.from_dict(instruction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


