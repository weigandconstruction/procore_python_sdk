# BIMModelRevisionPlanBatchCreateResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_model_revision_id** | **int** | ID of BIM Model Revision | 
**bim_plan_id** | **int** | ID of BIM Plan. The BIM Plan should be associated to the same BIM File as the BIM Model Revision | 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_model_revision_plan_batch_create_response_errors_inner import BIMModelRevisionPlanBatchCreateResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BIMModelRevisionPlanBatchCreateResponseErrorsInner from a JSON string
bim_model_revision_plan_batch_create_response_errors_inner_instance = BIMModelRevisionPlanBatchCreateResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(BIMModelRevisionPlanBatchCreateResponseErrorsInner.to_json())

# convert the object into a dict
bim_model_revision_plan_batch_create_response_errors_inner_dict = bim_model_revision_plan_batch_create_response_errors_inner_instance.to_dict()
# create an instance of BIMModelRevisionPlanBatchCreateResponseErrorsInner from a dict
bim_model_revision_plan_batch_create_response_errors_inner_from_dict = BIMModelRevisionPlanBatchCreateResponseErrorsInner.from_dict(bim_model_revision_plan_batch_create_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


