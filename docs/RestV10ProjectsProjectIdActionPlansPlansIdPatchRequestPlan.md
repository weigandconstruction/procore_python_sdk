# RestV10ProjectsProjectIdActionPlansPlansIdPatchRequestPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the Action Plan | [optional] 
**description** | **str** | Description of the Action Plan | [optional] 
**private** | **bool** | Privacy flag of the Action Plan | [optional] 
**location_id** | **int** | Location ID to be set on the Action Plan | [optional] 
**manager_id** | **int** | Party Person ID of the Action Plan Manager | [optional] 
**plan_type_id** | **int** | Plan Type ID to be set on the Action Plan | [optional] 
**status_id** | **int** | Action Plan Status ID to be set on the Action Plan | [optional] 
**plan_approvers_attributes** | [**List[RestV10ProjectsProjectIdActionPlansPlansIdPatchRequestPlanPlanApproversAttributesInner]**](RestV10ProjectsProjectIdActionPlansPlansIdPatchRequestPlanPlanApproversAttributesInner.md) |  | [optional] 
**plan_receivers_attributes** | [**List[RestV10ProjectsProjectIdActionPlansPlansIdPatchRequestPlanPlanReceiversAttributesInner]**](RestV10ProjectsProjectIdActionPlansPlansIdPatchRequestPlanPlanReceiversAttributesInner.md) |  | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_id_patch_request_plan import RestV10ProjectsProjectIdActionPlansPlansIdPatchRequestPlan

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlansIdPatchRequestPlan from a JSON string
rest_v10_projects_project_id_action_plans_plans_id_patch_request_plan_instance = RestV10ProjectsProjectIdActionPlansPlansIdPatchRequestPlan.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlansIdPatchRequestPlan.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plans_id_patch_request_plan_dict = rest_v10_projects_project_id_action_plans_plans_id_patch_request_plan_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlansIdPatchRequestPlan from a dict
rest_v10_projects_project_id_action_plans_plans_id_patch_request_plan_from_dict = RestV10ProjectsProjectIdActionPlansPlansIdPatchRequestPlan.from_dict(rest_v10_projects_project_id_action_plans_plans_id_patch_request_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


