# Body130BimModelRevisionOneOf

BIM Model Revision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_file_id** | **int** | ID of the published model file | 
**bim_model_id** | **int** | ID of the published model | 
**home_viewpoint_id** | **int** | ID of the BimViewpoint resource to be set as home viewpoint | [optional] 
**suitability** | **str** | Suitability of published model | 
**publisher_name** | **str** | Name of application publishing the model revision | [optional] 
**publisher_version** | **str** | Version of application publishing the model revision | [optional] 
**min_boundary** | [**RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary**](RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary.md) |  | 
**max_boundary** | [**RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary**](RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary.md) |  | 
**rotation** | [**RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary**](RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary.md) |  | [optional] 
**geometry_file_bundle_id** | **int** | ID of the associated geometry file bundle | [optional] 

## Example

```python
from procore_sdk.models.body130_bim_model_revision_one_of import Body130BimModelRevisionOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of Body130BimModelRevisionOneOf from a JSON string
body130_bim_model_revision_one_of_instance = Body130BimModelRevisionOneOf.from_json(json)
# print the JSON string representation of the object
print(Body130BimModelRevisionOneOf.to_json())

# convert the object into a dict
body130_bim_model_revision_one_of_dict = body130_bim_model_revision_one_of_instance.to_dict()
# create an instance of Body130BimModelRevisionOneOf from a dict
body130_bim_model_revision_one_of_from_dict = Body130BimModelRevisionOneOf.from_dict(body130_bim_model_revision_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


