# RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInner

Recycled Action Plan Test Record Request (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_item_id** | **int** | ID of the associated Action Plan Item ID | [optional] 
**created_at** | **datetime** | Time the Action Plan Test Record Request was created | [optional] 
**deleted_at** | **datetime** | Time the Recycled Action Plan Test Record Request was deleted | [optional] 
**payload** | [**RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload.md) |  | [optional] 
**plan_id** | **int** | Action Plan ID | [optional] 
**plan_test_records_count** | **int** | Count of Action Plan Test Records linked to this Action Plan Test Record Request | [optional] 
**type** | **str** | Action Plan Test Record Request Type | [optional] 
**updated_at** | **datetime** | Time the Action Plan Test Record Request was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_record_requests_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_record_requests_get200_response_inner_instance = RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_record_requests_get200_response_inner_dict = rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_record_requests_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInner from a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_record_requests_get200_response_inner_from_dict = RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInner.from_dict(rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_record_requests_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


