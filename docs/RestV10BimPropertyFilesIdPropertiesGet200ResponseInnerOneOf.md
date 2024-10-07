# RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf

BIM Model Property

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int** | Object ID | [optional] 
**category** | **str** | Category | [optional] 
**name** | **str** | Name | [optional] 
**typed_value** | **str** | Property value in native type. The typed_value can be null for models published to Procore when native values were not captured in the publishing process. | [optional] 
**uom** | **str** | The unit of measure for the property value. The value is null when unit of measure does not exist for a property. | [optional] 
**value** | **str** | Property display value same as typed_value. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_property_files_id_properties_get200_response_inner_one_of import RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf from a JSON string
rest_v10_bim_property_files_id_properties_get200_response_inner_one_of_instance = RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf.to_json())

# convert the object into a dict
rest_v10_bim_property_files_id_properties_get200_response_inner_one_of_dict = rest_v10_bim_property_files_id_properties_get200_response_inner_one_of_instance.to_dict()
# create an instance of RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf from a dict
rest_v10_bim_property_files_id_properties_get200_response_inner_one_of_from_dict = RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf.from_dict(rest_v10_bim_property_files_id_properties_get200_response_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


