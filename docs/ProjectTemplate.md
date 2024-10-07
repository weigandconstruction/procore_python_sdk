# ProjectTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier for the Project template | [optional] 
**name** | **str** | The name of the Project template | [optional] 

## Example

```python
from procore_sdk.models.project_template import ProjectTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplate from a JSON string
project_template_instance = ProjectTemplate.from_json(json)
# print the JSON string representation of the object
print(ProjectTemplate.to_json())

# convert the object into a dict
project_template_dict = project_template_instance.to_dict()
# create an instance of ProjectTemplate from a dict
project_template_from_dict = ProjectTemplate.from_dict(project_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


