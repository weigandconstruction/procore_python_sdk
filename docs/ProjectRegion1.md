# ProjectRegion1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier for the Project Region | [optional] 
**name** | **str** | The name for the Project Region | [optional] 

## Example

```python
from procore_sdk.models.project_region1 import ProjectRegion1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRegion1 from a JSON string
project_region1_instance = ProjectRegion1.from_json(json)
# print the JSON string representation of the object
print(ProjectRegion1.to_json())

# convert the object into a dict
project_region1_dict = project_region1_instance.to_dict()
# create an instance of ProjectRegion1 from a dict
project_region1_from_dict = ProjectRegion1.from_dict(project_region1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


