# MaterialBulkDestroyBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_materials** | [**TimeAndMaterialMaterials**](TimeAndMaterialMaterials.md) |  | 

## Example

```python
from procore_sdk.models.material_bulk_destroy_body import MaterialBulkDestroyBody

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialBulkDestroyBody from a JSON string
material_bulk_destroy_body_instance = MaterialBulkDestroyBody.from_json(json)
# print the JSON string representation of the object
print(MaterialBulkDestroyBody.to_json())

# convert the object into a dict
material_bulk_destroy_body_dict = material_bulk_destroy_body_instance.to_dict()
# create an instance of MaterialBulkDestroyBody from a dict
material_bulk_destroy_body_from_dict = MaterialBulkDestroyBody.from_dict(material_bulk_destroy_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


