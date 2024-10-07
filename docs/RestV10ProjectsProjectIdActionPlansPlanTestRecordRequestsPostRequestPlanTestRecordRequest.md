# RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsPostRequestPlanTestRecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_item_id** | **int** | Action Plan Item ID | 
**type** | **str** | Action Plan Test Record Type | 
**payload** | [**ActionPlanTemplateReferencesInnerPayload**](ActionPlanTemplateReferencesInnerPayload.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_record_requests_post_request_plan_test_record_request import RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsPostRequestPlanTestRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsPostRequestPlanTestRecordRequest from a JSON string
rest_v10_projects_project_id_action_plans_plan_test_record_requests_post_request_plan_test_record_request_instance = RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsPostRequestPlanTestRecordRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsPostRequestPlanTestRecordRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_test_record_requests_post_request_plan_test_record_request_dict = rest_v10_projects_project_id_action_plans_plan_test_record_requests_post_request_plan_test_record_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsPostRequestPlanTestRecordRequest from a dict
rest_v10_projects_project_id_action_plans_plan_test_record_requests_post_request_plan_test_record_request_from_dict = RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsPostRequestPlanTestRecordRequest.from_dict(rest_v10_projects_project_id_action_plans_plan_test_record_requests_post_request_plan_test_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


