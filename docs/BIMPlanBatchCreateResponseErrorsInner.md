# BIMPlanBatchCreateResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_level_id** | **int** | ID of the BIM Level to be associated to the plan | 
**drawing_id** | **int** | ID of the Drawing to be associated to the plan | [optional] 
**upload_uuid** | **str** | UUID of uploaded 2D sheet image. One of drawing_id or upload_uid is required | [optional] 
**sheet_map_start** | [**Body125BimPlanOneOfSheetMapStart**](Body125BimPlanOneOfSheetMapStart.md) |  | [optional] 
**sheet_map_end** | [**Body125BimPlanOneOfSheetMapStart**](Body125BimPlanOneOfSheetMapStart.md) |  | [optional] 
**model_map_start** | [**Body125BimPlanOneOfModelMapStart**](Body125BimPlanOneOfModelMapStart.md) |  | [optional] 
**model_map_end** | [**Body125BimPlanOneOfModelMapStart**](Body125BimPlanOneOfModelMapStart.md) |  | [optional] 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_plan_batch_create_response_errors_inner import BIMPlanBatchCreateResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BIMPlanBatchCreateResponseErrorsInner from a JSON string
bim_plan_batch_create_response_errors_inner_instance = BIMPlanBatchCreateResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(BIMPlanBatchCreateResponseErrorsInner.to_json())

# convert the object into a dict
bim_plan_batch_create_response_errors_inner_dict = bim_plan_batch_create_response_errors_inner_instance.to_dict()
# create an instance of BIMPlanBatchCreateResponseErrorsInner from a dict
bim_plan_batch_create_response_errors_inner_from_dict = BIMPlanBatchCreateResponseErrorsInner.from_dict(bim_plan_batch_create_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


