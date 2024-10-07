# RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_template_item_id** | **int** | Project Action Plan Template Item ID | 
**type** | **str** | Action Plan Reference Type | 
**payload** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload**](RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_references_post_request1_plan_template_reference import RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReference from a JSON string
rest_v10_projects_project_id_action_plans_plan_template_references_post_request1_plan_template_reference_instance = RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReference.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReference.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_template_references_post_request1_plan_template_reference_dict = rest_v10_projects_project_id_action_plans_plan_template_references_post_request1_plan_template_reference_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReference from a dict
rest_v10_projects_project_id_action_plans_plan_template_references_post_request1_plan_template_reference_from_dict = RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReference.from_dict(rest_v10_projects_project_id_action_plans_plan_template_references_post_request1_plan_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


