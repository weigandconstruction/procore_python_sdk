# CustomFieldsSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom Fields Section ID | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**position** | **int** | Position is sorted ascending, lowest position is visually the top of the page. | [optional] 
**from_v1_custom_fields** | **bool** | If section was migrated from v1 Custom Fields | [optional] 

## Example

```python
from procore_sdk.models.custom_fields_section import CustomFieldsSection

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldsSection from a JSON string
custom_fields_section_instance = CustomFieldsSection.from_json(json)
# print the JSON string representation of the object
print(CustomFieldsSection.to_json())

# convert the object into a dict
custom_fields_section_dict = custom_fields_section_instance.to_dict()
# create an instance of CustomFieldsSection from a dict
custom_fields_section_from_dict = CustomFieldsSection.from_dict(custom_fields_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


