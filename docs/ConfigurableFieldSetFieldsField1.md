# ConfigurableFieldSetFieldsField1

The first Observation Field object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field. | [optional] 
**visible** | **bool** | If this property is set to true, the field is visible. If this property is set to false, the field is not visible. | [optional] 
**required** | **bool** | If this property is set to true, the field is required, if the property is set to false, the field is not required. | [optional] 

## Example

```python
from procore_sdk.models.configurable_field_set_fields_field1 import ConfigurableFieldSetFieldsField1

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableFieldSetFieldsField1 from a JSON string
configurable_field_set_fields_field1_instance = ConfigurableFieldSetFieldsField1.from_json(json)
# print the JSON string representation of the object
print(ConfigurableFieldSetFieldsField1.to_json())

# convert the object into a dict
configurable_field_set_fields_field1_dict = configurable_field_set_fields_field1_instance.to_dict()
# create an instance of ConfigurableFieldSetFieldsField1 from a dict
configurable_field_set_fields_field1_from_dict = ConfigurableFieldSetFieldsField1.from_dict(configurable_field_set_fields_field1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


