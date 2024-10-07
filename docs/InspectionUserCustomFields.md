# InspectionUserCustomFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_custom_field_decimal_definition_id** | **bool** | Represents whether or not the user has read access to the Custom Field | [optional] 

## Example

```python
from procore_sdk.models.inspection_user_custom_fields import InspectionUserCustomFields

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionUserCustomFields from a JSON string
inspection_user_custom_fields_instance = InspectionUserCustomFields.from_json(json)
# print the JSON string representation of the object
print(InspectionUserCustomFields.to_json())

# convert the object into a dict
inspection_user_custom_fields_dict = inspection_user_custom_fields_instance.to_dict()
# create an instance of InspectionUserCustomFields from a dict
inspection_user_custom_fields_from_dict = InspectionUserCustomFields.from_dict(inspection_user_custom_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


