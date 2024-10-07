# ConfigurableFieldSet2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the configurable field set. | [optional] 
**name** | **str** | The name of the configurable field set. | [optional] 
**type** | **str** | The type of configurable field set | [optional] 
**category** | **str** | Specifies the category for the configurable field set if it exists or an empty string. This property was added for the ConfigurableFieldSet::Observations::Item class. | [optional] 
**class_name** | **str** | Specifies the class the configurable field set is associated with. | [optional] 
**fields** | [**ConfigurableFieldSet2Fields**](ConfigurableFieldSet2Fields.md) |  | [optional] 
**sections** | [**List[ConfigurableFieldSetSectionsInner]**](ConfigurableFieldSetSectionsInner.md) | An array of sections that are used for custom fields. | [optional] 
**deletable** | **bool** | Deletable status | [optional] 
**updated_at** | **datetime** | Date updated | [optional] 
**updated_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**inspection_type_id** | **int** | The unique identifier of the inspection type. | [optional] 
**generic_tool_id** | **int** | The unique idenfitier of the generic tool. | [optional] 
**action_plan_type_id** | **int** | The unique idenfitier of the action plan type. | [optional] 
**projects** | [**List[ConfigurableFieldSet2ProjectsInner]**](ConfigurableFieldSet2ProjectsInner.md) | An array of projects that are associated with the configurable field set. | [optional] 

## Example

```python
from procore_sdk.models.configurable_field_set2 import ConfigurableFieldSet2

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableFieldSet2 from a JSON string
configurable_field_set2_instance = ConfigurableFieldSet2.from_json(json)
# print the JSON string representation of the object
print(ConfigurableFieldSet2.to_json())

# convert the object into a dict
configurable_field_set2_dict = configurable_field_set2_instance.to_dict()
# create an instance of ConfigurableFieldSet2 from a dict
configurable_field_set2_from_dict = ConfigurableFieldSet2.from_dict(configurable_field_set2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


