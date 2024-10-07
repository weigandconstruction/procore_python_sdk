# MaterialBulkCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_materials** | [**List[MaterialProperties]**](MaterialProperties.md) | Array of Material objects | 

## Example

```python
from procore_sdk.models.material_bulk_create_body import MaterialBulkCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialBulkCreateBody from a JSON string
material_bulk_create_body_instance = MaterialBulkCreateBody.from_json(json)
# print the JSON string representation of the object
print(MaterialBulkCreateBody.to_json())

# convert the object into a dict
material_bulk_create_body_dict = material_bulk_create_body_instance.to_dict()
# create an instance of MaterialBulkCreateBody from a dict
material_bulk_create_body_from_dict = MaterialBulkCreateBody.from_dict(material_bulk_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


