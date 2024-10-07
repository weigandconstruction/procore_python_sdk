# ProjectStage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier for the Project Stage | [optional] 
**name** | **str** | The name for the Project Stage | [optional] 

## Example

```python
from procore_sdk.models.project_stage import ProjectStage

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStage from a JSON string
project_stage_instance = ProjectStage.from_json(json)
# print the JSON string representation of the object
print(ProjectStage.to_json())

# convert the object into a dict
project_stage_dict = project_stage_instance.to_dict()
# create an instance of ProjectStage from a dict
project_stage_from_dict = ProjectStage.from_dict(project_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


