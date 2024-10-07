# RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner

Project Action Plan Template Item Assignee (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_template_item_id** | **int** | Project Action Plan Template Item ID the Project Action Plan Template Item Assignee belongs to | [optional] 
**created_at** | **datetime** | Time the Project Action Plan Template Item Assignee was created | [optional] 
**is_holding** | **bool** | Boolean flag indicating whether the assignee is necessary to sign for a hold point | [optional] 
**party** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 
**plan_template_id** | **int** | Plan Template ID the Project Action Plan Template Item Assignee belongs to | [optional] 
**role** | **str** | Role of the Project Action Plan Template Item Assignee | [optional] 
**updated_at** | **datetime** | Time the Project Action Plan Template Item Assignee was updated | [optional] 
**verification_method** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInnerVerificationMethod**](RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInnerVerificationMethod.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get200_response_inner_instance = RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get200_response_inner_dict = rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner from a dict
rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get200_response_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner.from_dict(rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


