# ConfigurableFieldSet2Fields

Specifies the hash of fields on an object. This is for example purposes only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_1** | [**ConfigurableFieldSetFieldsField1**](ConfigurableFieldSetFieldsField1.md) |  | [optional] 
**custom_field_1** | [**ConfigurableFieldSet2FieldsCustomField1**](ConfigurableFieldSet2FieldsCustomField1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.configurable_field_set2_fields import ConfigurableFieldSet2Fields

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableFieldSet2Fields from a JSON string
configurable_field_set2_fields_instance = ConfigurableFieldSet2Fields.from_json(json)
# print the JSON string representation of the object
print(ConfigurableFieldSet2Fields.to_json())

# convert the object into a dict
configurable_field_set2_fields_dict = configurable_field_set2_fields_instance.to_dict()
# create an instance of ConfigurableFieldSet2Fields from a dict
configurable_field_set2_fields_from_dict = ConfigurableFieldSet2Fields.from_dict(configurable_field_set2_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


