# RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequestPlanItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Action Plan Item | 
**title** | **str** | Title of the Action Plan Item | [optional] 
**description** | **str** | Description of the Action Plan Item | [optional] 
**notes** | **str** | Notes for the Action Plan Item | [optional] 
**due_at** | **datetime** | Due Date of the Action Plan Item | [optional] 
**status_id** | **int** | Status ID of the Action Plan Item (1 - open, 2 - in_progress, 3 - delayed, 4 - closed) | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request_plan_items_inner import RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequestPlanItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequestPlanItemsInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request_plan_items_inner_instance = RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequestPlanItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequestPlanItemsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request_plan_items_inner_dict = rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request_plan_items_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequestPlanItemsInner from a dict
rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request_plan_items_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequestPlanItemsInner.from_dict(rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request_plan_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


