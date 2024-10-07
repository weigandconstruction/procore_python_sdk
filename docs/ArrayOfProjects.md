# ArrayOfProjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[Project4]**](Project4.md) |  | [optional] 
**errors** | [**List[ArrayOfProjectsErrorsInner]**](ArrayOfProjectsErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_projects import ArrayOfProjects

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProjects from a JSON string
array_of_projects_instance = ArrayOfProjects.from_json(json)
# print the JSON string representation of the object
print(ArrayOfProjects.to_json())

# convert the object into a dict
array_of_projects_dict = array_of_projects_instance.to_dict()
# create an instance of ArrayOfProjects from a dict
array_of_projects_from_dict = ArrayOfProjects.from_dict(array_of_projects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


