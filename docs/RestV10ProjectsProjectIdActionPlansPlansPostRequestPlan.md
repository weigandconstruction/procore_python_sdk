# RestV10ProjectsProjectIdActionPlansPlansPostRequestPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the Action Plan | 
**description** | **str** | Description of the Action Plan | [optional] 
**private** | **bool** | Privacy flag of the Action Plan | [optional] 
**location_id** | **int** | Location ID to be set on the Action Plan | [optional] 
**manager_id** | **int** | Party Person ID of the Action Plan Manager | [optional] 
**plan_type_id** | **int** | Plan Type ID to be set on the Action Plan | 
**plan_approvers_attributes** | [**List[RestV10ProjectsProjectIdActionPlansPlansPostRequestPlanPlanApproversAttributesInner]**](RestV10ProjectsProjectIdActionPlansPlansPostRequestPlanPlanApproversAttributesInner.md) |  | [optional] 
**plan_receivers_attributes** | [**List[RestV10ProjectsProjectIdActionPlansPlansPostRequestPlanPlanReceiversAttributesInner]**](RestV10ProjectsProjectIdActionPlansPlansPostRequestPlanPlanReceiversAttributesInner.md) |  | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_post_request_plan import RestV10ProjectsProjectIdActionPlansPlansPostRequestPlan

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlansPostRequestPlan from a JSON string
rest_v10_projects_project_id_action_plans_plans_post_request_plan_instance = RestV10ProjectsProjectIdActionPlansPlansPostRequestPlan.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlansPostRequestPlan.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plans_post_request_plan_dict = rest_v10_projects_project_id_action_plans_plans_post_request_plan_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlansPostRequestPlan from a dict
rest_v10_projects_project_id_action_plans_plans_post_request_plan_from_dict = RestV10ProjectsProjectIdActionPlansPlansPostRequestPlan.from_dict(rest_v10_projects_project_id_action_plans_plans_post_request_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


