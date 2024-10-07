# ConfigurableFieldSetFieldsCustomField1

Custom Field object for an existing custom field in this configurable field set object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The metadatum identifier of the custom field. | [optional] 
**name** | **str** | The name of the custom field. | [optional] 
**label** | **str** | The label of the custom field definition. | [optional] 
**description** | **str** | The description of the custom field definition. | [optional] 
**custom_field_definition_id** | **int** | The definition identifier of the custom field. | [optional] 
**data_type** | **str** | Data type of the custom field. | [optional] 
**variant** | **str** | The variant type of the custom field. | [optional] 
**position** | **int** | The display position of the custom field, which is sorted ascending, lowest position is visually the top left of the page on a grid basis (used in conjunction with column_width property to calculate row and column properties). | [optional] 
**required** | **bool** | If this property is set to true, the custom field is required. If this property is set to false, the custom field is not required. | [optional] 
**visible** | **bool** | If this property is set to true, the custom field is visible. If this property is set to false, the custom field is not visible. | [optional] 
**row** | **float** | The number of the row where the custom field is positioned on the form. | [optional] 
**column** | **float** | The number of the column where the custom field is positioned on the form. | [optional] 
**column_width** | **float** | The number of columns the custom field spans on the form. | [optional] 

## Example

```python
from procore_sdk.models.configurable_field_set_fields_custom_field1 import ConfigurableFieldSetFieldsCustomField1

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableFieldSetFieldsCustomField1 from a JSON string
configurable_field_set_fields_custom_field1_instance = ConfigurableFieldSetFieldsCustomField1.from_json(json)
# print the JSON string representation of the object
print(ConfigurableFieldSetFieldsCustomField1.to_json())

# convert the object into a dict
configurable_field_set_fields_custom_field1_dict = configurable_field_set_fields_custom_field1_instance.to_dict()
# create an instance of ConfigurableFieldSetFieldsCustomField1 from a dict
configurable_field_set_fields_custom_field1_from_dict = ConfigurableFieldSetFieldsCustomField1.from_dict(configurable_field_set_fields_custom_field1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


