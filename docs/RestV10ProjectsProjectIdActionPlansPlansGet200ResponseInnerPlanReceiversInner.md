# RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner

Action Plan Receiver (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_id** | **int** | Action Plan ID | [optional] 
**updated_at** | **datetime** | Time the Action Plan Receiver was updated | [optional] 
**party** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 
**signature** | [**RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_receivers_inner import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner from a JSON string
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_receivers_inner_instance = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_receivers_inner_dict = rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_receivers_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner from a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_receivers_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner.from_dict(rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_receivers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


