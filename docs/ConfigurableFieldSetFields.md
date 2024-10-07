# ConfigurableFieldSetFields

Specifies the hash of fields on an object. This is for example purposes only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_1** | [**ConfigurableFieldSetFieldsField1**](ConfigurableFieldSetFieldsField1.md) |  | [optional] 
**custom_field_1** | [**ConfigurableFieldSetFieldsCustomField1**](ConfigurableFieldSetFieldsCustomField1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.configurable_field_set_fields import ConfigurableFieldSetFields

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableFieldSetFields from a JSON string
configurable_field_set_fields_instance = ConfigurableFieldSetFields.from_json(json)
# print the JSON string representation of the object
print(ConfigurableFieldSetFields.to_json())

# convert the object into a dict
configurable_field_set_fields_dict = configurable_field_set_fields_instance.to_dict()
# create an instance of ConfigurableFieldSetFields from a dict
configurable_field_set_fields_from_dict = ConfigurableFieldSetFields.from_dict(configurable_field_set_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


