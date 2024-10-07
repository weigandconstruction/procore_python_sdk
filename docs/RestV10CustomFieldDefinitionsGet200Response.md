# RestV10CustomFieldDefinitionsGet200Response


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
**custom_field_lov_entries** | [**List[CustomFieldLovEntry]**](CustomFieldLovEntry.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_custom_field_definitions_get200_response import RestV10CustomFieldDefinitionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CustomFieldDefinitionsGet200Response from a JSON string
rest_v10_custom_field_definitions_get200_response_instance = RestV10CustomFieldDefinitionsGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CustomFieldDefinitionsGet200Response.to_json())

# convert the object into a dict
rest_v10_custom_field_definitions_get200_response_dict = rest_v10_custom_field_definitions_get200_response_instance.to_dict()
# create an instance of RestV10CustomFieldDefinitionsGet200Response from a dict
rest_v10_custom_field_definitions_get200_response_from_dict = RestV10CustomFieldDefinitionsGet200Response.from_dict(rest_v10_custom_field_definitions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


