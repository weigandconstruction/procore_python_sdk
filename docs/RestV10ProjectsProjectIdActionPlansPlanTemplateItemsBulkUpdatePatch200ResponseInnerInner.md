# RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Item | [optional] 
**description** | **str** | Description of the Action Plan Template Item | [optional] 
**due_at** | **datetime** | Timestamp of when the Project Action Plan Template Item should be completed by | [optional] 
**status** | **str** | status of the update on that Item | [optional] 
**errors** | **object** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch200_response_inner_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch200_response_inner_inner_instance = RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch200_response_inner_inner_dict = rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch200_response_inner_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner from a dict
rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch200_response_inner_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner.from_dict(rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch200_response_inner_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


