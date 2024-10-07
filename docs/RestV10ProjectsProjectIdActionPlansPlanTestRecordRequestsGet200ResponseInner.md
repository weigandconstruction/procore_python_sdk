# RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInner

Action Plan Test Record Request (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_item_id** | **int** | ID of the associated Action Plan Item | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**payload** | [**RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload**](RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload.md) |  | [optional] 
**plan_id** | **int** | Action Plan ID | [optional] 
**plan_test_records_count** | **int** | Count of Action Plan Test Records linked to this Action Plan Test Record Request | [optional] 
**type** | **str** | Action Plan Test Record Type | [optional] 
**type_id** | **int** | Action Plan Test Record Type ID | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_record_requests_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_test_record_requests_get200_response_inner_instance = RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_test_record_requests_get200_response_inner_dict = rest_v10_projects_project_id_action_plans_plan_test_record_requests_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInner from a dict
rest_v10_projects_project_id_action_plans_plan_test_record_requests_get200_response_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsGet200ResponseInner.from_dict(rest_v10_projects_project_id_action_plans_plan_test_record_requests_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


