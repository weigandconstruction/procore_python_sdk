# ProjectTemplate1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Template ID | [optional] 
**name** | **str** | Project Template name | [optional] 

## Example

```python
from procore_sdk.models.project_template1 import ProjectTemplate1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplate1 from a JSON string
project_template1_instance = ProjectTemplate1.from_json(json)
# print the JSON string representation of the object
print(ProjectTemplate1.to_json())

# convert the object into a dict
project_template1_dict = project_template1_instance.to_dict()
# create an instance of ProjectTemplate1 from a dict
project_template1_from_dict = ProjectTemplate1.from_dict(project_template1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


