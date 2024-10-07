# RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_items** | [**List[RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequestPlanItemsInner]**](RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequestPlanItemsInner.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request import RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest from a JSON string
rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request_instance = RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request_dict = rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest from a dict
rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request_from_dict = RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest.from_dict(rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


