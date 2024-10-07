# ProjectType2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Type ID | [optional] 
**name** | **str** | Project Type name | [optional] 

## Example

```python
from procore_sdk.models.project_type2 import ProjectType2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectType2 from a JSON string
project_type2_instance = ProjectType2.from_json(json)
# print the JSON string representation of the object
print(ProjectType2.to_json())

# convert the object into a dict
project_type2_dict = project_type2_instance.to_dict()
# create an instance of ProjectType2 from a dict
project_type2_from_dict = ProjectType2.from_dict(project_type2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


