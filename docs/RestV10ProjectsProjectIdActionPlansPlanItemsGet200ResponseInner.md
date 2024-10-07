# RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner

Action Plan Item (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_item_assignees** | [**List[RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInner]**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInner.md) |  | [optional] 
**created_at** | **str** | Time the Action Plan Item was created | [optional] 
**description** | **str** | Description of the Action Plan Item | [optional] 
**due_at** | **datetime** | Due Date of the Action Plan Item | [optional] 
**holding_type** | **str** | Action Plan Item holding type specifies whether the current item holds all the succeeding items in the section or the plan | [optional] 
**is_blocked** | **bool** | Indicates whether current Action Plan Item is blocked by another Action Plan Item | [optional] 
**is_blocking** | **bool** | Indicates whether current Action Plan Item is blocking other Action Plan Items | [optional] 
**notes** | **str** | Notes for the Action Plan Item | [optional] 
**plan_id** | **int** | Plan ID the Action Plan Item belongs to | [optional] 
**position** | **int** | Position of the Action Plan Item | [optional] 
**plan_section_id** | **int** | Action Plan Section ID the Item belongs to | [optional] 
**title** | **str** | Title of the Action Plan Item | [optional] 
**status** | [**RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerStatus**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerStatus.md) |  | [optional] 
**updated_at** | **str** | Time the Action Plan Item was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_instance = RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_dict = rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner from a dict
rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner.from_dict(rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


