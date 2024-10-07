# Body131BimModelRevisionOneOf

BIM Model Revision object

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

## Example

```python
from procore_sdk.models.body131_bim_model_revision_one_of import Body131BimModelRevisionOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of Body131BimModelRevisionOneOf from a JSON string
body131_bim_model_revision_one_of_instance = Body131BimModelRevisionOneOf.from_json(json)
# print the JSON string representation of the object
print(Body131BimModelRevisionOneOf.to_json())

# convert the object into a dict
body131_bim_model_revision_one_of_dict = body131_bim_model_revision_one_of_instance.to_dict()
# create an instance of Body131BimModelRevisionOneOf from a dict
body131_bim_model_revision_one_of_from_dict = Body131BimModelRevisionOneOf.from_dict(body131_bim_model_revision_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


