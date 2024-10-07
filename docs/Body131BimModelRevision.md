# Body131BimModelRevision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_viewpoint_id** | **int** | ID of the BimViewpoint resource to be set as home viewpoint | [optional] 
**suitability** | **str** | Suitability of published model | [optional] 
**publish_status** | **str** | Model publish status | [optional] 
**min_boundary** | [**Body125BimPlanOneOfModelMapStart**](Body125BimPlanOneOfModelMapStart.md) |  | [optional] 
**max_boundary** | [**Body125BimPlanOneOfModelMapStart**](Body125BimPlanOneOfModelMapStart.md) |  | [optional] 
**rotation** | [**Body131BimModelRevisionOneOfRotation**](Body131BimModelRevisionOneOfRotation.md) |  | [optional] 
**published_model_upload_uuid** | **str** | UUID of the uploaded model | [optional] 
**object_definition_upload_uuid** | **str** | UUID of the uploaded model object definition file | [optional] 
**geometry_file_id** | **int** | ID of the Procore 3d model format file containing geometry information. | [optional] 
**geometry_file_bundle_id** | **int** | ID of the Procore BIM Geometry File Bundle. | [optional] 
**property_file_id** | **int** | ID of the Procore 3d model format file containing property data information. | [optional] 

## Example

```python
from procore_sdk.models.body131_bim_model_revision import Body131BimModelRevision

# TODO update the JSON string below
json = "{}"
# create an instance of Body131BimModelRevision from a JSON string
body131_bim_model_revision_instance = Body131BimModelRevision.from_json(json)
# print the JSON string representation of the object
print(Body131BimModelRevision.to_json())

# convert the object into a dict
body131_bim_model_revision_dict = body131_bim_model_revision_instance.to_dict()
# create an instance of Body131BimModelRevision from a dict
body131_bim_model_revision_from_dict = Body131BimModelRevision.from_dict(body131_bim_model_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


