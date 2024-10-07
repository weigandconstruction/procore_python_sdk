# RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Status ID for the Action Plan Item (1 - open, 2 - in_progress, 3 - delayed, 4 - closed) | [optional] 
**name** | **str** | Status name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_status import RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerStatus from a JSON string
rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_status_instance = RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerStatus.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerStatus.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_status_dict = rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_status_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerStatus from a dict
rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_status_from_dict = RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerStatus.from_dict(rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


