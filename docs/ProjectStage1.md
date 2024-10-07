# ProjectStage1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Stage ID | [optional] 
**name** | **str** | Stage name | [optional] 

## Example

```python
from procore_sdk.models.project_stage1 import ProjectStage1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStage1 from a JSON string
project_stage1_instance = ProjectStage1.from_json(json)
# print the JSON string representation of the object
print(ProjectStage1.to_json())

# convert the object into a dict
project_stage1_dict = project_stage1_instance.to_dict()
# create an instance of ProjectStage1 from a dict
project_stage1_from_dict = ProjectStage1.from_dict(project_stage1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


