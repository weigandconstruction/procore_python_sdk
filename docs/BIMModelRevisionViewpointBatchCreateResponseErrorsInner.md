# BIMModelRevisionViewpointBatchCreateResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_model_revision_id** | **int** | BIM Model Revision ID | 
**bim_viewpoint_id** | **int** | BIM Viewpoint ID. The BIM Viewpoint should be associated to the same BIM File as the BIM Model Revision | 
**primary** | **bool** | Flag to indicate whether this is primary viewpoint for the model revision. There can only be one primary viewpoint per model revision | [optional] 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_model_revision_viewpoint_batch_create_response_errors_inner import BIMModelRevisionViewpointBatchCreateResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BIMModelRevisionViewpointBatchCreateResponseErrorsInner from a JSON string
bim_model_revision_viewpoint_batch_create_response_errors_inner_instance = BIMModelRevisionViewpointBatchCreateResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(BIMModelRevisionViewpointBatchCreateResponseErrorsInner.to_json())

# convert the object into a dict
bim_model_revision_viewpoint_batch_create_response_errors_inner_dict = bim_model_revision_viewpoint_batch_create_response_errors_inner_instance.to_dict()
# create an instance of BIMModelRevisionViewpointBatchCreateResponseErrorsInner from a dict
bim_model_revision_viewpoint_batch_create_response_errors_inner_from_dict = BIMModelRevisionViewpointBatchCreateResponseErrorsInner.from_dict(bim_model_revision_viewpoint_batch_create_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


