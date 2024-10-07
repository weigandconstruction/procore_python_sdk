# RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom Field Lov Entry ID | [optional] 
**label** | **str** | Label | [optional] 
**position** | **float** | Position is sorted descending, highest position is visually the top of the list. | [optional] 
**active** | **bool** | Whether or not the Custom Field Lov Entry is active | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get200_response import RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesGet200Response from a JSON string
rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get200_response_instance = RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesGet200Response.to_json())

# convert the object into a dict
rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get200_response_dict = rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get200_response_instance.to_dict()
# create an instance of RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesGet200Response from a dict
rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get200_response_from_dict = RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesGet200Response.from_dict(rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


