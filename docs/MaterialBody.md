# MaterialBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**material** | [**MaterialProperties**](MaterialProperties.md) |  | 

## Example

```python
from procore_sdk.models.material_body import MaterialBody

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialBody from a JSON string
material_body_instance = MaterialBody.from_json(json)
# print the JSON string representation of the object
print(MaterialBody.to_json())

# convert the object into a dict
material_body_dict = material_body_instance.to_dict()
# create an instance of MaterialBody from a dict
material_body_from_dict = MaterialBody.from_dict(material_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


