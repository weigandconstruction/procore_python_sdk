# RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**var_global** | **bool** | Flag indicating if Action Plan Status applies to all Companies | [optional] 
**name** | **str** | Name | [optional] 
**status** | **str** | Status | [optional] 
**updated_at** | **datetime** | Timestamp of the last update | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_status import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanStatus from a JSON string
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_status_instance = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanStatus.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanStatus.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_status_dict = rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_status_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanStatus from a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_status_from_dict = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanStatus.from_dict(rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


