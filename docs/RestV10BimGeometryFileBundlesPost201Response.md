# RestV10BimGeometryFileBundlesPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bim_model_revision_id** | **int** | ID of associated model revision | [optional] 
**project_id** | **int** | Unique identifier for the project. | [optional] 
**created_by_id** | **int** | Creator ID | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**cell_file** | [**VendorCommentAttachmentsInner**](VendorCommentAttachmentsInner.md) |  | [optional] 
**node_file** | [**VendorCommentAttachmentsInner**](VendorCommentAttachmentsInner.md) |  | [optional] 
**mesh_node_file** | [**VendorCommentAttachmentsInner**](VendorCommentAttachmentsInner.md) |  | [optional] 
**mesh_file** | [**VendorCommentAttachmentsInner**](VendorCommentAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_geometry_file_bundles_post201_response import RestV10BimGeometryFileBundlesPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimGeometryFileBundlesPost201Response from a JSON string
rest_v10_bim_geometry_file_bundles_post201_response_instance = RestV10BimGeometryFileBundlesPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10BimGeometryFileBundlesPost201Response.to_json())

# convert the object into a dict
rest_v10_bim_geometry_file_bundles_post201_response_dict = rest_v10_bim_geometry_file_bundles_post201_response_instance.to_dict()
# create an instance of RestV10BimGeometryFileBundlesPost201Response from a dict
rest_v10_bim_geometry_file_bundles_post201_response_from_dict = RestV10BimGeometryFileBundlesPost201Response.from_dict(rest_v10_bim_geometry_file_bundles_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


