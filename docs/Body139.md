# Body139


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**view** | **str** | Specify response schema view | [optional] 
**bim_geometry_file_bundle** | [**Body139BimGeometryFileBundle**](Body139BimGeometryFileBundle.md) |  | 

## Example

```python
from procore_sdk.models.body139 import Body139

# TODO update the JSON string below
json = "{}"
# create an instance of Body139 from a JSON string
body139_instance = Body139.from_json(json)
# print the JSON string representation of the object
print(Body139.to_json())

# convert the object into a dict
body139_dict = body139_instance.to_dict()
# create an instance of Body139 from a dict
body139_from_dict = Body139.from_dict(body139_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


