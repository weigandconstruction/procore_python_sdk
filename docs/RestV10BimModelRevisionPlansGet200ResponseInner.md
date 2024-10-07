# RestV10BimModelRevisionPlansGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bim_model_revision_id** | **int** | ID of associated published BIM Model Revision | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**bim_plan_id** | **int** | ID of the BIM Plan | [optional] 
**bim_level_id** | **int** | ID of the Bim Level linked to the plan | [optional] 
**bim_plan** | [**RestV10BimPlansGet200ResponseInner**](RestV10BimPlansGet200ResponseInner.md) |  | [optional] 
**bim_level** | [**RestV10BimModelRevisionPlansGet200ResponseInnerOneOf1BimLevel**](RestV10BimModelRevisionPlansGet200ResponseInnerOneOf1BimLevel.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_model_revision_plans_get200_response_inner import RestV10BimModelRevisionPlansGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimModelRevisionPlansGet200ResponseInner from a JSON string
rest_v10_bim_model_revision_plans_get200_response_inner_instance = RestV10BimModelRevisionPlansGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BimModelRevisionPlansGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_bim_model_revision_plans_get200_response_inner_dict = rest_v10_bim_model_revision_plans_get200_response_inner_instance.to_dict()
# create an instance of RestV10BimModelRevisionPlansGet200ResponseInner from a dict
rest_v10_bim_model_revision_plans_get200_response_inner_from_dict = RestV10BimModelRevisionPlansGet200ResponseInner.from_dict(rest_v10_bim_model_revision_plans_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


