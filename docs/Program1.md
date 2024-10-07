# Program1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Program | [optional] 
**address_freeform** | **str** | The Address of the Program | [optional] 
**website** | **str** | The Website of the Program | [optional] 
**zip** | **str** | The Zip code of the Program | [optional] 

## Example

```python
from procore_sdk.models.program1 import Program1

# TODO update the JSON string below
json = "{}"
# create an instance of Program1 from a JSON string
program1_instance = Program1.from_json(json)
# print the JSON string representation of the object
print(Program1.to_json())

# convert the object into a dict
program1_dict = program1_instance.to_dict()
# create an instance of Program1 from a dict
program1_from_dict = Program1.from_dict(program1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


