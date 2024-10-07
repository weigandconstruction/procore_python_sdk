# BIMViewpointBatchCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_viewpoints** | [**List[RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner]**](RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner.md) |  | [optional] 
**errors** | [**List[BIMViewpointBatchCreateResponseErrorsInner]**](BIMViewpointBatchCreateResponseErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_viewpoint_batch_create_response import BIMViewpointBatchCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BIMViewpointBatchCreateResponse from a JSON string
bim_viewpoint_batch_create_response_instance = BIMViewpointBatchCreateResponse.from_json(json)
# print the JSON string representation of the object
print(BIMViewpointBatchCreateResponse.to_json())

# convert the object into a dict
bim_viewpoint_batch_create_response_dict = bim_viewpoint_batch_create_response_instance.to_dict()
# create an instance of BIMViewpointBatchCreateResponse from a dict
bim_viewpoint_batch_create_response_from_dict = BIMViewpointBatchCreateResponse.from_dict(bim_viewpoint_batch_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


