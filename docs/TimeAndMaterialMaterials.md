# TimeAndMaterialMaterials

Material Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_materials_ids** | **List[int]** | Array of material IDs specified for delete | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_materials import TimeAndMaterialMaterials

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialMaterials from a JSON string
time_and_material_materials_instance = TimeAndMaterialMaterials.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialMaterials.to_json())

# convert the object into a dict
time_and_material_materials_dict = time_and_material_materials_instance.to_dict()
# create an instance of TimeAndMaterialMaterials from a dict
time_and_material_materials_from_dict = TimeAndMaterialMaterials.from_dict(time_and_material_materials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


