# ProjectProgram1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier for the Project Program | [optional] 
**name** | **str** | The name for the Project Program | [optional] 

## Example

```python
from procore_sdk.models.project_program1 import ProjectProgram1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectProgram1 from a JSON string
project_program1_instance = ProjectProgram1.from_json(json)
# print the JSON string representation of the object
print(ProjectProgram1.to_json())

# convert the object into a dict
project_program1_dict = project_program1_instance.to_dict()
# create an instance of ProjectProgram1 from a dict
project_program1_from_dict = ProjectProgram1.from_dict(project_program1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


