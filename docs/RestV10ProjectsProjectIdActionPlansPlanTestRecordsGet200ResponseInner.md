# RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner

Action Plan Test Record (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_item_id** | **int** | ID of the associated Action Plan Item | [optional] 
**created_at** | **str** | Timestamp of creation | [optional] 
**payload** | [**RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInnerPayload**](RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInnerPayload.md) |  | [optional] 
**plan_id** | **int** | Action Plan ID | [optional] 
**plan_test_record_request_id** | **int** | Action Plan Test Record Request ID | [optional] 
**type** | **str** | Action Plan Test Record Type | [optional] 
**updated_at** | **str** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_records_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_test_records_get200_response_inner_instance = RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_test_records_get200_response_inner_dict = rest_v10_projects_project_id_action_plans_plan_test_records_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner from a dict
rest_v10_projects_project_id_action_plans_plan_test_records_get200_response_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner.from_dict(rest_v10_projects_project_id_action_plans_plan_test_records_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


