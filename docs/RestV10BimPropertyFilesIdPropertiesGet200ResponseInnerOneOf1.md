# RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf1

BIM Model Property

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int** | Object ID | [optional] 
**category** | **str** | Property Category | [optional] 
**name** | **str** | Property Name | [optional] 
**typed_value** | **float** | Property value in native type. Numeric value can contain numbers with very high decimal precision. The typed_value can be null for models published to Procore when native values were not captured in the publishing process. | [optional] 
**uom** | **str** | The unit of measure for the property value. The value is null when unit of measure does not exist for a property. | [optional] 
**value** | **str** | Property display value. For numeric values with uom, the typed_value is concatenated with uom. Decimal values are truncated to four decimal places. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_property_files_id_properties_get200_response_inner_one_of1 import RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf1 from a JSON string
rest_v10_bim_property_files_id_properties_get200_response_inner_one_of1_instance = RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf1.from_json(json)
# print the JSON string representation of the object
print(RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf1.to_json())

# convert the object into a dict
rest_v10_bim_property_files_id_properties_get200_response_inner_one_of1_dict = rest_v10_bim_property_files_id_properties_get200_response_inner_one_of1_instance.to_dict()
# create an instance of RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf1 from a dict
rest_v10_bim_property_files_id_properties_get200_response_inner_one_of1_from_dict = RestV10BimPropertyFilesIdPropertiesGet200ResponseInnerOneOf1.from_dict(rest_v10_bim_property_files_id_properties_get200_response_inner_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


