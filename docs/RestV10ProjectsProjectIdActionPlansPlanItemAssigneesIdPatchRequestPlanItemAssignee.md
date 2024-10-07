# RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_holding** | **bool** | Indicates whether or not the Action Plan Item Assignee&#39;s signature is holding | [optional] 
**party_id** | **int** | Party Person ID of the Action Plan Item Assignee to be set | [optional] 
**verification_method_id** | **int** | Verification Method ID of the Action Plan Item Assignee to be set | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request_plan_item_assignee import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee from a JSON string
rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request_plan_item_assignee_instance = RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request_plan_item_assignee_dict = rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request_plan_item_assignee_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee from a dict
rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request_plan_item_assignee_from_dict = RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee.from_dict(rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request_plan_item_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


