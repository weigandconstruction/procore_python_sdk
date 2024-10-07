# Body139BimGeometryFileBundle

BIM Geometry File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_model_revision_id** | **int** | ID of the model revision to be associated | 
**cell_upload_uuid** | **str** | UUID of uploaded cell geometry file | 
**node_upload_uuid** | **str** | UUID of uploaded node geometry file | 
**mesh_node_upload_uuid** | **str** | UUID of uploaded mesh node geometry file | 
**mesh_upload_uuid** | **str** | UUID of uploaded mesh geometry file | 

## Example

```python
from procore_sdk.models.body139_bim_geometry_file_bundle import Body139BimGeometryFileBundle

# TODO update the JSON string below
json = "{}"
# create an instance of Body139BimGeometryFileBundle from a JSON string
body139_bim_geometry_file_bundle_instance = Body139BimGeometryFileBundle.from_json(json)
# print the JSON string representation of the object
print(Body139BimGeometryFileBundle.to_json())

# convert the object into a dict
body139_bim_geometry_file_bundle_dict = body139_bim_geometry_file_bundle_instance.to_dict()
# create an instance of Body139BimGeometryFileBundle from a dict
body139_bim_geometry_file_bundle_from_dict = Body139BimGeometryFileBundle.from_dict(body139_bim_geometry_file_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


