# RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInner

Action Plan Item Assignee (Compact)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Time the Plan Item Assignee was created | [optional] 
**is_holding** | **bool** | Boolean flag indicating whether the assignee is necessary to sign for a hold point | [optional] 
**is_locked** | **bool** | Boolean flag indicating whether the assignee was added prior to an Action Plan&#39;s approval | [optional] 
**party** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 
**role** | **str** | Role of the Plan Item Assignee | [optional] 
**role_id** | **int** | Role ID | [optional] 
**signature** | [**RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignature**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignature.md) |  | [optional] 
**updated_at** | **datetime** | Time the Plan Item Assignee was updated | [optional] 
**verification_method** | [**RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerVerificationMethod**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerVerificationMethod.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_plan_item_assignees_inner import RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_plan_item_assignees_inner_instance = RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_plan_item_assignees_inner_dict = rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_plan_item_assignees_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInner from a dict
rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_plan_item_assignees_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInner.from_dict(rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_plan_item_assignees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


