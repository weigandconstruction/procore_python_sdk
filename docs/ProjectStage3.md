# ProjectStage3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_bidding_stage** | **bool** | The Bidding Stage status of the Project Stage | [optional] [default to False]
**name** | **str** | The Name of the Project Stage | [optional] 
**category** | **str** | The Category Type of the Project Stage | [optional] 

## Example

```python
from procore_sdk.models.project_stage3 import ProjectStage3

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStage3 from a JSON string
project_stage3_instance = ProjectStage3.from_json(json)
# print the JSON string representation of the object
print(ProjectStage3.to_json())

# convert the object into a dict
project_stage3_dict = project_stage3_instance.to_dict()
# create an instance of ProjectStage3 from a dict
project_stage3_from_dict = ProjectStage3.from_dict(project_stage3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


