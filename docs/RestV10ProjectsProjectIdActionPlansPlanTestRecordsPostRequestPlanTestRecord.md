# RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequestPlanTestRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_item_id** | **int** | ID of the associated Action Plan Control Activity | 
**plan_test_record_request_id** | **int** | ID of the associated Action Plan Test Record Request | 
**type** | **str** | Action Plan Test Record Type | 
**payload** | [**OneOf**](.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_records_post_request_plan_test_record import RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequestPlanTestRecord

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequestPlanTestRecord from a JSON string
rest_v10_projects_project_id_action_plans_plan_test_records_post_request_plan_test_record_instance = RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequestPlanTestRecord.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequestPlanTestRecord.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_test_records_post_request_plan_test_record_dict = rest_v10_projects_project_id_action_plans_plan_test_records_post_request_plan_test_record_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequestPlanTestRecord from a dict
rest_v10_projects_project_id_action_plans_plan_test_records_post_request_plan_test_record_from_dict = RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequestPlanTestRecord.from_dict(rest_v10_projects_project_id_action_plans_plan_test_records_post_request_plan_test_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


