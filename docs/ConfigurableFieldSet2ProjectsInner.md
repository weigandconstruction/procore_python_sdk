# ConfigurableFieldSet2ProjectsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the project. | [optional] 
**name** | **str** | The name of the project. | [optional] 

## Example

```python
from procore_sdk.models.configurable_field_set2_projects_inner import ConfigurableFieldSet2ProjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableFieldSet2ProjectsInner from a JSON string
configurable_field_set2_projects_inner_instance = ConfigurableFieldSet2ProjectsInner.from_json(json)
# print the JSON string representation of the object
print(ConfigurableFieldSet2ProjectsInner.to_json())

# convert the object into a dict
configurable_field_set2_projects_inner_dict = configurable_field_set2_projects_inner_instance.to_dict()
# create an instance of ConfigurableFieldSet2ProjectsInner from a dict
configurable_field_set2_projects_inner_from_dict = ConfigurableFieldSet2ProjectsInner.from_dict(configurable_field_set2_projects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


