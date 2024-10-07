# CustomFieldMetadatum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Custom Field Metadatum ID | [optional] 
**custom_field_definition_id** | **float** | Custom Field Definition ID | [optional] 
**position** | **float** | Position is sorted ascending, lowest position is visually the top left of the page on a grid basis (used in conjunction with column_width property to calculate row and column properties). | [optional] 
**required** | **bool** | Whether or not the Custom Field Metadatum is required | [optional] 
**visible** | **bool** | Whether or not the Custom Field Metadatum is visible | [optional] 
**company_id** | **float** | Company ID | [optional] 
**host_type** | **str** | Procore Entity | [optional] 
**source_type** | **str** | Configurable FieldSet Class | [optional] 
**source_id** | **str** | Configurable FieldSet ID | [optional] 
**label** | **str** | Custom Field Metadatum Label | [optional] 
**data_type** | **str** | Type of Custom field | [optional] 
**variant** | **str** | The variant type of the Custom Field | [optional] 
**default_value** | **str** | The default value of the Custom Field | [optional] 
**row** | **float** | Row the Field is position on the Form | [optional] 
**column** | **float** | Column the Field is position on the Form | [optional] 
**column_width** | **float** | How many columns the field spans on the Form | [optional] 
**custom_fields_section_id** | **float** | The display section of the Custom Field, if null it is the general section, visually in the top level section typically called \&quot;General Information\&quot;. | [optional] 
**lov_entries** | [**List[CustomFieldLovEntry]**](CustomFieldLovEntry.md) |  | [optional] 

## Example

```python
from procore_sdk.models.custom_field_metadatum import CustomFieldMetadatum

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldMetadatum from a JSON string
custom_field_metadatum_instance = CustomFieldMetadatum.from_json(json)
# print the JSON string representation of the object
print(CustomFieldMetadatum.to_json())

# convert the object into a dict
custom_field_metadatum_dict = custom_field_metadatum_instance.to_dict()
# create an instance of CustomFieldMetadatum from a dict
custom_field_metadatum_from_dict = CustomFieldMetadatum.from_dict(custom_field_metadatum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


