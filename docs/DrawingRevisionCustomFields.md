# DrawingRevisionCustomFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_custom_field_string_definition_id** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldStringDefinitionId**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldStringDefinitionId.md) |  | [optional] 
**custom_field_custom_field_decimal_definition_id** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldDecimalDefinitionId**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldDecimalDefinitionId.md) |  | [optional] 
**custom_field_custom_field_boolean_definition_id** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId.md) |  | [optional] 
**custom_field_custom_field_lov_entry_definition_id** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldLovEntryDefinitionId**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldLovEntryDefinitionId.md) |  | [optional] 
**custom_field_custom_field_lov_entries_definition_id** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldLovEntriesDefinitionId**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldLovEntriesDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.drawing_revision_custom_fields import DrawingRevisionCustomFields

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingRevisionCustomFields from a JSON string
drawing_revision_custom_fields_instance = DrawingRevisionCustomFields.from_json(json)
# print the JSON string representation of the object
print(DrawingRevisionCustomFields.to_json())

# convert the object into a dict
drawing_revision_custom_fields_dict = drawing_revision_custom_fields_instance.to_dict()
# create an instance of DrawingRevisionCustomFields from a dict
drawing_revision_custom_fields_from_dict = DrawingRevisionCustomFields.from_dict(drawing_revision_custom_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


