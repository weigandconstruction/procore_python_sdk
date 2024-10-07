# MaterialBulkUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_materials** | [**List[MaterialProperties]**](MaterialProperties.md) | Array of Material objects | 

## Example

```python
from procore_sdk.models.material_bulk_update_body import MaterialBulkUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialBulkUpdateBody from a JSON string
material_bulk_update_body_instance = MaterialBulkUpdateBody.from_json(json)
# print the JSON string representation of the object
print(MaterialBulkUpdateBody.to_json())

# convert the object into a dict
material_bulk_update_body_dict = material_bulk_update_body_instance.to_dict()
# create an instance of MaterialBulkUpdateBody from a dict
material_bulk_update_body_from_dict = MaterialBulkUpdateBody.from_dict(material_bulk_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


