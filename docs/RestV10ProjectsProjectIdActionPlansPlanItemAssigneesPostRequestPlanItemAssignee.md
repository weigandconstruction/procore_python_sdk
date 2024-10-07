# RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequestPlanItemAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_item_id** | **int** | Action Plan Item ID of the Action Plan Item Assignee to be set | 
**is_holding** | **bool** | Indicates whether or not the Action  Item Assignee&#39;s signature is holding | [optional] 
**party_id** | **int** | Party Person ID of the Action Plan Item Assignee to be set | [optional] 
**role** | **str** | Role of the Action Plan Item Assignee to be set | [optional] 
**verification_method_id** | **int** | Verification Method ID of the Action Plan Item Assignee to be set | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request_plan_item_assignee import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequestPlanItemAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequestPlanItemAssignee from a JSON string
rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request_plan_item_assignee_instance = RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequestPlanItemAssignee.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequestPlanItemAssignee.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request_plan_item_assignee_dict = rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request_plan_item_assignee_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequestPlanItemAssignee from a dict
rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request_plan_item_assignee_from_dict = RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequestPlanItemAssignee.from_dict(rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request_plan_item_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


