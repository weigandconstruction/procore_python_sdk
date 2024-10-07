# MaterialProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_entry_id** | **int** | Time &amp; Material Entry Id the material is associated with | [optional] 
**name** | **str** | Name of the material | [optional] 
**description** | **str** | Description of the material | [optional] 
**uom** | **str** | Unit of measure for the material | [optional] 
**quantity** | **float** | Quantity of the material | [optional] 

## Example

```python
from procore_sdk.models.material_properties import MaterialProperties

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialProperties from a JSON string
material_properties_instance = MaterialProperties.from_json(json)
# print the JSON string representation of the object
print(MaterialProperties.to_json())

# convert the object into a dict
material_properties_dict = material_properties_instance.to_dict()
# create an instance of MaterialProperties from a dict
material_properties_from_dict = MaterialProperties.from_dict(material_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


