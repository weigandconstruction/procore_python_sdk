# BIMViewpointBatchCreateResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_file_id** | **int** | ID of a BIM File to be associated to the viewpoint | 
**name** | **str** | Viewpoint name | [optional] 
**view_folder_id** | **int** | ID of the BIM View Folder the viewpoint belongs to | [optional] 
**upload_uuid** | **str** | UUID of uploaded snapshot | 
**camera_data** | **str** | Camera data for the building model associated with the issue | 
**redlines_data** | **str** | Lines data for the building model associated with the issue | [optional] 
**sections_data** | **str** | Clipping plane data for the building model associated with the issue | [optional] 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_viewpoint_batch_create_response_errors_inner import BIMViewpointBatchCreateResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BIMViewpointBatchCreateResponseErrorsInner from a JSON string
bim_viewpoint_batch_create_response_errors_inner_instance = BIMViewpointBatchCreateResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(BIMViewpointBatchCreateResponseErrorsInner.to_json())

# convert the object into a dict
bim_viewpoint_batch_create_response_errors_inner_dict = bim_viewpoint_batch_create_response_errors_inner_instance.to_dict()
# create an instance of BIMViewpointBatchCreateResponseErrorsInner from a dict
bim_viewpoint_batch_create_response_errors_inner_from_dict = BIMViewpointBatchCreateResponseErrorsInner.from_dict(bim_viewpoint_batch_create_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


