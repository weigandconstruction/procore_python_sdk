# RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner

Recycled Action Plan Item Assignee (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_item_id** | **int** | Plan Item ID of the Recycled Action Plan Item Assignee | [optional] 
**created_at** | **str** | Time the Recycled Action Plan Item Assignee was created | [optional] 
**deleted_at** | **str** | Time the Recycled Action Plan Item Assignee was deleted | [optional] 
**is_holding** | **bool** | Boolean flag indicating whether the assignee is necessary to sign for a hold point | [optional] 
**is_locked** | **bool** | Boolean flag indicating whether the assignee was added prior to an Action Plan&#39;s approval | [optional] 
**party** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 
**plan_id** | **int** | Plan ID of the Action Plan Item Assignee | [optional] 
**role** | **str** | Role of the Recycled Action Plan Item Assignee | [optional] 
**signature** | [**RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignature**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignature.md) |  | [optional] 
**updated_at** | **str** | Time the Recycled Action Plan Item Assignee was updated | [optional] 
**verification_method** | [**RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerVerificationMethod**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerVerificationMethod.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get200_response_inner_instance = RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get200_response_inner_dict = rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner from a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get200_response_inner_from_dict = RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner.from_dict(rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


