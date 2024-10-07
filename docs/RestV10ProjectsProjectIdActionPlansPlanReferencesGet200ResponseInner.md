# RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner

Action Plan Reference (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_item_id** | **int** | Action Plan Item ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**payload** | [**RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInnerPayload**](RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInnerPayload.md) |  | [optional] 
**plan_id** | **int** | Action Plan ID | [optional] 
**type** | **str** | Action Plan Reference Type | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**deleted_at** | **datetime** | Timestamp of deletion | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_references_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_references_get200_response_inner_instance = RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_references_get200_response_inner_dict = rest_v10_projects_project_id_action_plans_plan_references_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner from a dict
rest_v10_projects_project_id_action_plans_plan_references_get200_response_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner.from_dict(rest_v10_projects_project_id_action_plans_plan_references_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


