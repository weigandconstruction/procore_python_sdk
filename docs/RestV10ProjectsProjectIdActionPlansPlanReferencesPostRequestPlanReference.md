# RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequestPlanReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_item_id** | **int** | Action Plan Item ID | 
**type** | **str** | Action Plan Reference Type | 
**payload** | [**RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequestPlanReferencePayload**](RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequestPlanReferencePayload.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_references_post_request_plan_reference import RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequestPlanReference

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequestPlanReference from a JSON string
rest_v10_projects_project_id_action_plans_plan_references_post_request_plan_reference_instance = RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequestPlanReference.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequestPlanReference.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_references_post_request_plan_reference_dict = rest_v10_projects_project_id_action_plans_plan_references_post_request_plan_reference_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequestPlanReference from a dict
rest_v10_projects_project_id_action_plans_plan_references_post_request_plan_reference_from_dict = RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequestPlanReference.from_dict(rest_v10_projects_project_id_action_plans_plan_references_post_request_plan_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


