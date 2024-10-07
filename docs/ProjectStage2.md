# ProjectStage2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Stage ID | [optional] 
**name** | **str** | Project Stage name | [optional] 
**is_bidding_stage** | **bool** | Project Stage is bidding stage status | [optional] 
**category** | **str** | The Category Type of the Project Stage | [optional] 
**readonly** | **bool** | Indicates whether the stage is editable or deletable | [optional] 

## Example

```python
from procore_sdk.models.project_stage2 import ProjectStage2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStage2 from a JSON string
project_stage2_instance = ProjectStage2.from_json(json)
# print the JSON string representation of the object
print(ProjectStage2.to_json())

# convert the object into a dict
project_stage2_dict = project_stage2_instance.to_dict()
# create an instance of ProjectStage2 from a dict
project_stage2_from_dict = ProjectStage2.from_dict(project_stage2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


