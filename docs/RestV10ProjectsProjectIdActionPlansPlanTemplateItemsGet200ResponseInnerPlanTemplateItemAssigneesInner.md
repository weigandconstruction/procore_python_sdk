# RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInnerPlanTemplateItemAssigneesInner

Project Action Plan Template Item Assignee (Compact)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Time the Project Action Plan Template Item Assignee was created | [optional] 
**is_holding** | **bool** | Boolean flag indicating whether the assignee is necessary to sign for a hold point | [optional] 
**party** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 
**role** | **str** | Role of the Project Action Plan Template Item Assignee | [optional] 
**updated_at** | **datetime** | Time the Project Action Plan Template Item Assignee was updated | [optional] 
**verification_method** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInnerPlanTemplateItemAssigneesInnerVerificationMethod**](RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInnerPlanTemplateItemAssigneesInnerVerificationMethod.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_items_get200_response_inner_plan_template_item_assignees_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInnerPlanTemplateItemAssigneesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInnerPlanTemplateItemAssigneesInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_template_items_get200_response_inner_plan_template_item_assignees_inner_instance = RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInnerPlanTemplateItemAssigneesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInnerPlanTemplateItemAssigneesInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_template_items_get200_response_inner_plan_template_item_assignees_inner_dict = rest_v10_projects_project_id_action_plans_plan_template_items_get200_response_inner_plan_template_item_assignees_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInnerPlanTemplateItemAssigneesInner from a dict
rest_v10_projects_project_id_action_plans_plan_template_items_get200_response_inner_plan_template_item_assignees_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInnerPlanTemplateItemAssigneesInner.from_dict(rest_v10_projects_project_id_action_plans_plan_template_items_get200_response_inner_plan_template_item_assignees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


