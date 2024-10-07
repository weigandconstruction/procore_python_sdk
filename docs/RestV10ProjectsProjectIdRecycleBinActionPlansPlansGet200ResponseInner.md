# RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner

Recycled Action Plan (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_approvers** | [**List[RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInner]**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInner.md) |  | [optional] 
**created_at** | **str** | Time the Action Plan was created | [optional] 
**deleted_at** | **str** | Time the Action Plan was deleted | [optional] 
**deleted_by** | [**RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInnerDeletedBy**](RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInnerDeletedBy.md) |  | [optional] 
**description** | **str** | Description of the Action Plan in rich text form | [optional] 
**description_plain_text** | **str** | Description of the Action Plan in plain text form | [optional] 
**location** | [**Location1**](Location1.md) |  | [optional] 
**manager** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 
**number** | **int** | Number of the Action Plan | [optional] 
**plan_receivers** | [**List[RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner]**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner.md) |  | [optional] 
**plan_type** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.md) |  | [optional] 
**plan_status** | [**RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanStatus**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanStatus.md) |  | [optional] 
**status** | **str** | Status of the Action Plan | [optional] 
**title** | **str** | Title of the Action Plan | [optional] 
**updated_at** | **datetime** | Timestamp of when the Action Plan was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plans_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner from a JSON string
rest_v10_projects_project_id_recycle_bin_action_plans_plans_get200_response_inner_instance = RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plans_get200_response_inner_dict = rest_v10_projects_project_id_recycle_bin_action_plans_plans_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner from a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plans_get200_response_inner_from_dict = RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner.from_dict(rest_v10_projects_project_id_recycle_bin_action_plans_plans_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


