# Body130BimModelRevisionOneOf2

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
**geometry_file_id** | **int** | ID of the Procore 3d model format file containing geometry information. | [optional] 
**property_file_id** | **int** | ID of the Procore 3d model format file containing property data information. | [optional] 

## Example

```python
from procore_sdk.models.body130_bim_model_revision_one_of2 import Body130BimModelRevisionOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of Body130BimModelRevisionOneOf2 from a JSON string
body130_bim_model_revision_one_of2_instance = Body130BimModelRevisionOneOf2.from_json(json)
# print the JSON string representation of the object
print(Body130BimModelRevisionOneOf2.to_json())

# convert the object into a dict
body130_bim_model_revision_one_of2_dict = body130_bim_model_revision_one_of2_instance.to_dict()
# create an instance of Body130BimModelRevisionOneOf2 from a dict
body130_bim_model_revision_one_of2_from_dict = Body130BimModelRevisionOneOf2.from_dict(body130_bim_model_revision_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


