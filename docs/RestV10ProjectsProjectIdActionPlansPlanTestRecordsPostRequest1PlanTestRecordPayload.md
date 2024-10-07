# RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest1PlanTestRecordPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | **bytearray** | Test Record Attachment. To upload an attachment you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type with the &#x60;attachment&#x60; file. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_records_post_request1_plan_test_record_payload import RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest1PlanTestRecordPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest1PlanTestRecordPayload from a JSON string
rest_v10_projects_project_id_action_plans_plan_test_records_post_request1_plan_test_record_payload_instance = RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest1PlanTestRecordPayload.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest1PlanTestRecordPayload.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_test_records_post_request1_plan_test_record_payload_dict = rest_v10_projects_project_id_action_plans_plan_test_records_post_request1_plan_test_record_payload_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest1PlanTestRecordPayload from a dict
rest_v10_projects_project_id_action_plans_plan_test_records_post_request1_plan_test_record_payload_from_dict = RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest1PlanTestRecordPayload.from_dict(rest_v10_projects_project_id_action_plans_plan_test_records_post_request1_plan_test_record_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


