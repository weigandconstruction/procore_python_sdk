# ProjectRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Region ID | [optional] 
**name** | **str** | Project Region name | [optional] 

## Example

```python
from procore_sdk.models.project_region import ProjectRegion

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRegion from a JSON string
project_region_instance = ProjectRegion.from_json(json)
# print the JSON string representation of the object
print(ProjectRegion.to_json())

# convert the object into a dict
project_region_dict = project_region_instance.to_dict()
# create an instance of ProjectRegion from a dict
project_region_from_dict = ProjectRegion.from_dict(project_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


