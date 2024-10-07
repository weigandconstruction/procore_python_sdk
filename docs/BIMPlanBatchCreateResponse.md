# BIMPlanBatchCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_plans** | [**List[RestV10BimPlansGet200ResponseInner]**](RestV10BimPlansGet200ResponseInner.md) |  | [optional] 
**errors** | [**List[BIMPlanBatchCreateResponseErrorsInner]**](BIMPlanBatchCreateResponseErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_plan_batch_create_response import BIMPlanBatchCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BIMPlanBatchCreateResponse from a JSON string
bim_plan_batch_create_response_instance = BIMPlanBatchCreateResponse.from_json(json)
# print the JSON string representation of the object
print(BIMPlanBatchCreateResponse.to_json())

# convert the object into a dict
bim_plan_batch_create_response_dict = bim_plan_batch_create_response_instance.to_dict()
# create an instance of BIMPlanBatchCreateResponse from a dict
bim_plan_batch_create_response_from_dict = BIMPlanBatchCreateResponse.from_dict(bim_plan_batch_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


