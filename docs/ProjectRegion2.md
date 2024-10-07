# ProjectRegion2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Region ID | [optional] 
**name** | **str** | Project Region name | [optional] 

## Example

```python
from procore_sdk.models.project_region2 import ProjectRegion2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRegion2 from a JSON string
project_region2_instance = ProjectRegion2.from_json(json)
# print the JSON string representation of the object
print(ProjectRegion2.to_json())

# convert the object into a dict
project_region2_dict = project_region2_instance.to_dict()
# create an instance of ProjectRegion2 from a dict
project_region2_from_dict = ProjectRegion2.from_dict(project_region2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


