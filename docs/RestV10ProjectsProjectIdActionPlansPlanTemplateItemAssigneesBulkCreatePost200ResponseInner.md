# RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePost200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_template_item_id** | **int** | The ID of the Item | [optional] 
**is_holding** | **bool** | status of the update on that Item | [optional] 
**errors** | **object** |  | [optional] 
**role** | **str** | Role of the Project Action Plan Template Item Assignee to be set | [optional] 
**verification_method_id** | **int** | Verification Method ID of the Project Action Plan Template Item Assignee to be set | [optional] 
**party_id** | **int** | Party Person ID of the Action Plan Item Assignee to be set | [optional] 
**status** | **str** | status of the update on that Item | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePost200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePost200ResponseInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post200_response_inner_instance = RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePost200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePost200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post200_response_inner_dict = rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePost200ResponseInner from a dict
rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post200_response_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePost200ResponseInner.from_dict(rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


