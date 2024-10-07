# RestV10BimModelRevisionPlansGet200ResponseInnerOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bim_model_revision_id** | **int** | ID of associated published BIM Model Revision | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**bim_plan_id** | **int** | ID of the BIM Plan | [optional] 
**bim_level_id** | **int** | ID of the Bim Level linked to the plan | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_model_revision_plans_get200_response_inner_one_of import RestV10BimModelRevisionPlansGet200ResponseInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimModelRevisionPlansGet200ResponseInnerOneOf from a JSON string
rest_v10_bim_model_revision_plans_get200_response_inner_one_of_instance = RestV10BimModelRevisionPlansGet200ResponseInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(RestV10BimModelRevisionPlansGet200ResponseInnerOneOf.to_json())

# convert the object into a dict
rest_v10_bim_model_revision_plans_get200_response_inner_one_of_dict = rest_v10_bim_model_revision_plans_get200_response_inner_one_of_instance.to_dict()
# create an instance of RestV10BimModelRevisionPlansGet200ResponseInnerOneOf from a dict
rest_v10_bim_model_revision_plans_get200_response_inner_one_of_from_dict = RestV10BimModelRevisionPlansGet200ResponseInnerOneOf.from_dict(rest_v10_bim_model_revision_plans_get200_response_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


