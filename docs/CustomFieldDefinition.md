# CustomFieldDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom Field Definition ID | [optional] 
**label** | **str** | Custom Field Definition Label | [optional] 
**active** | **bool** | Whether or not the Custom Field Definition is active | [optional] 
**company_id** | **int** | Company ID | [optional] 
**data_type** | **str** | Type of Custom field | [optional] 
**variant** | **str** | The variant type of the Custom Field | [optional] 
**description** | **str** | Description | [optional] 
**default_value** | **str** | Text displayed on Read Only variant | [optional] 
**configurable_field_sets_count** | **int** | Number of Configurable Field Sets associated with the Custom Field | [optional] 

## Example

```python
from procore_sdk.models.custom_field_definition import CustomFieldDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldDefinition from a JSON string
custom_field_definition_instance = CustomFieldDefinition.from_json(json)
# print the JSON string representation of the object
print(CustomFieldDefinition.to_json())

# convert the object into a dict
custom_field_definition_dict = custom_field_definition_instance.to_dict()
# create an instance of CustomFieldDefinition from a dict
custom_field_definition_from_dict = CustomFieldDefinition.from_dict(custom_field_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


