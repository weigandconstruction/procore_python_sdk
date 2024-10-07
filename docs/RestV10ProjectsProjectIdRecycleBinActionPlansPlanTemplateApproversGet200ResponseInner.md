# RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner

Recycled Project Action Plan Template Approver (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**deleted_at** | **datetime** | Timestamp of deletion | [optional] 
**plan_template_id** | **int** | Project Action Plan Template ID | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**party** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner from a JSON string
rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get200_response_inner_instance = RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get200_response_inner_dict = rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner from a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get200_response_inner_from_dict = RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner.from_dict(rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


