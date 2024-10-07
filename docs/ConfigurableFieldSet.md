# ConfigurableFieldSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the configurable field set. | [optional] 
**name** | **str** | The name of the configurable field set. | [optional] 
**type** | **str** | The type of configurable field set | [optional] 
**category** | **str** | Specifies the category for the configurable field set if it exists or an empty string. This property was added for the ConfigurableFieldSet::Observations::Item class. | [optional] 
**class_name** | **str** | Specifies the class the configurable field set is associated with. | [optional] 
**fields** | [**ConfigurableFieldSetFields**](ConfigurableFieldSetFields.md) |  | [optional] 
**sections** | [**List[ConfigurableFieldSetSectionsInner]**](ConfigurableFieldSetSectionsInner.md) | An array of sections that are used for custom fields. | [optional] 
**inspection_type_id** | **int** | The unique identifier of the inspection type. | [optional] 
**generic_tool_id** | **int** | The unique idenfitier of the generic tool. | [optional] 
**action_plan_type_id** | **int** | The unique idenfitier of the action plan type. | [optional] 

## Example

```python
from procore_sdk.models.configurable_field_set import ConfigurableFieldSet

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableFieldSet from a JSON string
configurable_field_set_instance = ConfigurableFieldSet.from_json(json)
# print the JSON string representation of the object
print(ConfigurableFieldSet.to_json())

# convert the object into a dict
configurable_field_set_dict = configurable_field_set_instance.to_dict()
# create an instance of ConfigurableFieldSet from a dict
configurable_field_set_from_dict = ConfigurableFieldSet.from_dict(configurable_field_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


