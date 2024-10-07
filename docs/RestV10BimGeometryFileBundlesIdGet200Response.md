# RestV10BimGeometryFileBundlesIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**project_id** | **int** | Unique identifier for the project. | [optional] 
**created_by_id** | **int** | Creator ID | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**bim_model_revision_id** | **int** | ID of associated model revision | [optional] 
**cell_file_id** | **int** | ID of associated cell geometry file | [optional] 
**node_file_id** | **int** | ID of associated node geometry file | [optional] 
**mesh_node_file_id** | **int** | ID of associated mesh node geometry file | [optional] 
**mesh_file_id** | **int** | ID of associated mesh geometry file | [optional] 
**manifest_file_id** | **int** | ID of associated manifest file | [optional] 
**cell_file** | [**VendorCommentAttachmentsInner**](VendorCommentAttachmentsInner.md) |  | [optional] 
**node_file** | [**VendorCommentAttachmentsInner**](VendorCommentAttachmentsInner.md) |  | [optional] 
**mesh_node_file** | [**VendorCommentAttachmentsInner**](VendorCommentAttachmentsInner.md) |  | [optional] 
**mesh_file** | [**VendorCommentAttachmentsInner**](VendorCommentAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_geometry_file_bundles_id_get200_response import RestV10BimGeometryFileBundlesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimGeometryFileBundlesIdGet200Response from a JSON string
rest_v10_bim_geometry_file_bundles_id_get200_response_instance = RestV10BimGeometryFileBundlesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10BimGeometryFileBundlesIdGet200Response.to_json())

# convert the object into a dict
rest_v10_bim_geometry_file_bundles_id_get200_response_dict = rest_v10_bim_geometry_file_bundles_id_get200_response_instance.to_dict()
# create an instance of RestV10BimGeometryFileBundlesIdGet200Response from a dict
rest_v10_bim_geometry_file_bundles_id_get200_response_from_dict = RestV10BimGeometryFileBundlesIdGet200Response.from_dict(rest_v10_bim_geometry_file_bundles_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


