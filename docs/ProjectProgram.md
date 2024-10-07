# ProjectProgram


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Program ID | [optional] 
**name** | **str** | Program name | [optional] 

## Example

```python
from procore_sdk.models.project_program import ProjectProgram

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectProgram from a JSON string
project_program_instance = ProjectProgram.from_json(json)
# print the JSON string representation of the object
print(ProjectProgram.to_json())

# convert the object into a dict
project_program_dict = project_program_instance.to_dict()
# create an instance of ProjectProgram from a dict
project_program_from_dict = ProjectProgram.from_dict(project_program_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


