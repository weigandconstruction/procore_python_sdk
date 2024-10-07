# RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInner

Action Plan Approver (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_id** | **int** | Action Plan ID | [optional] 
**updated_at** | **str** | Time the Action Plan Approver was updated | [optional] 
**party** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 
**signature** | [**RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignature**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignature.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInner from a JSON string
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_instance = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_dict = rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInner from a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInner.from_dict(rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


