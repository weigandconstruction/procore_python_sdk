# BIMModelRevisionPlanBatchCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_model_revision_plans** | [**List[RestV10BimModelRevisionPlansGet200ResponseInner]**](RestV10BimModelRevisionPlansGet200ResponseInner.md) |  | [optional] 
**errors** | [**List[BIMModelRevisionPlanBatchCreateResponseErrorsInner]**](BIMModelRevisionPlanBatchCreateResponseErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_model_revision_plan_batch_create_response import BIMModelRevisionPlanBatchCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BIMModelRevisionPlanBatchCreateResponse from a JSON string
bim_model_revision_plan_batch_create_response_instance = BIMModelRevisionPlanBatchCreateResponse.from_json(json)
# print the JSON string representation of the object
print(BIMModelRevisionPlanBatchCreateResponse.to_json())

# convert the object into a dict
bim_model_revision_plan_batch_create_response_dict = bim_model_revision_plan_batch_create_response_instance.to_dict()
# create an instance of BIMModelRevisionPlanBatchCreateResponse from a dict
bim_model_revision_plan_batch_create_response_from_dict = BIMModelRevisionPlanBatchCreateResponse.from_dict(bim_model_revision_plan_batch_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


