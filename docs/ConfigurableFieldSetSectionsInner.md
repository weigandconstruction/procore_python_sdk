# ConfigurableFieldSetSectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the section. | [optional] 
**name** | **str** | The name of the section. | [optional] 
**description** | **str** | The description of the section. | [optional] 
**position** | **int** | The display position of the section, which is sorted ascending, lowest position is visually the top of the page. | [optional] 
**from_v1_custom_fields** | **bool** | If field was migrated from a v1 custom field. | [optional] 

## Example

```python
from procore_sdk.models.configurable_field_set_sections_inner import ConfigurableFieldSetSectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableFieldSetSectionsInner from a JSON string
configurable_field_set_sections_inner_instance = ConfigurableFieldSetSectionsInner.from_json(json)
# print the JSON string representation of the object
print(ConfigurableFieldSetSectionsInner.to_json())

# convert the object into a dict
configurable_field_set_sections_inner_dict = configurable_field_set_sections_inner_instance.to_dict()
# create an instance of ConfigurableFieldSetSectionsInner from a dict
configurable_field_set_sections_inner_from_dict = ConfigurableFieldSetSectionsInner.from_dict(configurable_field_set_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


