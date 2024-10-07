# RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner

Action Plan Item Assignee (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_item_id** | **int** | Plan Item ID of the Action Plan Item Assignee | [optional] 
**created_at** | **str** | Time the Action Plan Item Assignee was created | [optional] 
**is_holding** | **bool** | Boolean flag indicating whether the assignee is necessary to sign for a hold point | [optional] 
**is_locked** | **bool** | Boolean flag indicating whether the assignee was added prior to an Action Plan&#39;s approval | [optional] 
**party** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 
**plan_id** | **int** | Plan ID of the Action Plan Item Assignee | [optional] 
**role** | **str** | Role of the Action Plan Item Assignee | [optional] 
**role_id** | **int** | Role ID | [optional] 
**signature** | [**RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignature**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignature.md) |  | [optional] 
**updated_at** | **str** | Time the Action Plan Item Assignee was updated | [optional] 
**verification_method** | [**RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerVerificationMethod**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerVerificationMethod.md) |  | [optional] 
**plan_template_item_id** | **int** | Plan Template Item ID | [optional] 
**plan_template_id** | **int** | Plan Template ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_item_assignees_get200_response_inner_instance = RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_item_assignees_get200_response_inner_dict = rest_v10_projects_project_id_action_plans_plan_item_assignees_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner from a dict
rest_v10_projects_project_id_action_plans_plan_item_assignees_get200_response_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner.from_dict(rest_v10_projects_project_id_action_plans_plan_item_assignees_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


