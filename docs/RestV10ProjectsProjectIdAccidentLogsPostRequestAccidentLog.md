# RestV10ProjectsProjectIdAccidentLogsPostRequestAccidentLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Additional comments about the accident | [optional] 
**var_date** | **date** | Date that the accident occured. Format: YYYY-MM-DD | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**involved_company** | **str** | Name of the Company involved in the accident | [optional] 
**involved_name** | **str** | Name of the person involved in the accident | [optional] 
**time_hour** | **int** | Time of accident - hour | 
**time_minute** | **int** | Time of accident - minute | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_accident_logs_post_request_accident_log import RestV10ProjectsProjectIdAccidentLogsPostRequestAccidentLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdAccidentLogsPostRequestAccidentLog from a JSON string
rest_v10_projects_project_id_accident_logs_post_request_accident_log_instance = RestV10ProjectsProjectIdAccidentLogsPostRequestAccidentLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdAccidentLogsPostRequestAccidentLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_accident_logs_post_request_accident_log_dict = rest_v10_projects_project_id_accident_logs_post_request_accident_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdAccidentLogsPostRequestAccidentLog from a dict
rest_v10_projects_project_id_accident_logs_post_request_accident_log_from_dict = RestV10ProjectsProjectIdAccidentLogsPostRequestAccidentLog.from_dict(rest_v10_projects_project_id_accident_logs_post_request_accident_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


