# BIMModelRevisionViewpointBatchCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_model_revision_viewpoints** | [**List[RestV10BimModelRevisionViewpointsGet200ResponseInnerOneOf]**](RestV10BimModelRevisionViewpointsGet200ResponseInnerOneOf.md) |  | [optional] 
**errors** | [**List[BIMModelRevisionViewpointBatchCreateResponseErrorsInner]**](BIMModelRevisionViewpointBatchCreateResponseErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_model_revision_viewpoint_batch_create_response import BIMModelRevisionViewpointBatchCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BIMModelRevisionViewpointBatchCreateResponse from a JSON string
bim_model_revision_viewpoint_batch_create_response_instance = BIMModelRevisionViewpointBatchCreateResponse.from_json(json)
# print the JSON string representation of the object
print(BIMModelRevisionViewpointBatchCreateResponse.to_json())

# convert the object into a dict
bim_model_revision_viewpoint_batch_create_response_dict = bim_model_revision_viewpoint_batch_create_response_instance.to_dict()
# create an instance of BIMModelRevisionViewpointBatchCreateResponse from a dict
bim_model_revision_viewpoint_batch_create_response_from_dict = BIMModelRevisionViewpointBatchCreateResponse.from_dict(bim_model_revision_viewpoint_batch_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


