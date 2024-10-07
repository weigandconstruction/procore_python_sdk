# CustomFieldLovEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom Field Lov Entry ID | [optional] 
**label** | **str** | Label | [optional] 
**position** | **float** | Position is sorted descending, highest position is visually the top of the list. | [optional] 
**active** | **bool** | Whether or not the Custom Field Lov Entry is active | [optional] 

## Example

```python
from procore_sdk.models.custom_field_lov_entry import CustomFieldLovEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldLovEntry from a JSON string
custom_field_lov_entry_instance = CustomFieldLovEntry.from_json(json)
# print the JSON string representation of the object
print(CustomFieldLovEntry.to_json())

# convert the object into a dict
custom_field_lov_entry_dict = custom_field_lov_entry_instance.to_dict()
# create an instance of CustomFieldLovEntry from a dict
custom_field_lov_entry_from_dict = CustomFieldLovEntry.from_dict(custom_field_lov_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


