# ProjectType1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier for the Project Type | [optional] 
**name** | **str** | The name for the Project Type | [optional] 

## Example

```python
from procore_sdk.models.project_type1 import ProjectType1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectType1 from a JSON string
project_type1_instance = ProjectType1.from_json(json)
# print the JSON string representation of the object
print(ProjectType1.to_json())

# convert the object into a dict
project_type1_dict = project_type1_instance.to_dict()
# create an instance of ProjectType1 from a dict
project_type1_from_dict = ProjectType1.from_dict(project_type1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


