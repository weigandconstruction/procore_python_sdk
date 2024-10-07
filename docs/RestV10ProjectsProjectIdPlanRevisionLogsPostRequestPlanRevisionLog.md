# RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category of discipline that appears on the revision | [optional] 
**comments** | **str** | Additional comments | [optional] 
**var_date** | **date** | Date of record. Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**plan_number** | **str** | Number that appears on the plan submitted | [optional] 
**revision** | **str** | Revision number | [optional] 
**title** | **str** | Title of the plans | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_plan_revision_logs_post_request_plan_revision_log import RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog from a JSON string
rest_v10_projects_project_id_plan_revision_logs_post_request_plan_revision_log_instance = RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_plan_revision_logs_post_request_plan_revision_log_dict = rest_v10_projects_project_id_plan_revision_logs_post_request_plan_revision_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog from a dict
rest_v10_projects_project_id_plan_revision_logs_post_request_plan_revision_log_from_dict = RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog.from_dict(rest_v10_projects_project_id_plan_revision_logs_post_request_plan_revision_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


