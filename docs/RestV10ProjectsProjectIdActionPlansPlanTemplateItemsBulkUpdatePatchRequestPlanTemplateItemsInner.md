# RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequestPlanTemplateItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Action Plan Template Item | 
**description** | **str** | Description of the Action Plan Item | [optional] 
**due_at** | **datetime** | Timestamp of when the Project Action Plan Template Item should be completed by | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch_request_plan_template_items_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequestPlanTemplateItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequestPlanTemplateItemsInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch_request_plan_template_items_inner_instance = RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequestPlanTemplateItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequestPlanTemplateItemsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch_request_plan_template_items_inner_dict = rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch_request_plan_template_items_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequestPlanTemplateItemsInner from a dict
rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch_request_plan_template_items_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequestPlanTemplateItemsInner.from_dict(rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch_request_plan_template_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


