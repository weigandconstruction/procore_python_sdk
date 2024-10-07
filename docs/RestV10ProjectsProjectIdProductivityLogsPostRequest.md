# RestV10ProjectsProjectIdProductivityLogsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**productivity_log** | [**RestV10ProjectsProjectIdProductivityLogsPostRequestProductivityLog**](RestV10ProjectsProjectIdProductivityLogsPostRequestProductivityLog.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_productivity_logs_post_request import RestV10ProjectsProjectIdProductivityLogsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdProductivityLogsPostRequest from a JSON string
rest_v10_projects_project_id_productivity_logs_post_request_instance = RestV10ProjectsProjectIdProductivityLogsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdProductivityLogsPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_productivity_logs_post_request_dict = rest_v10_projects_project_id_productivity_logs_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdProductivityLogsPostRequest from a dict
rest_v10_projects_project_id_productivity_logs_post_request_from_dict = RestV10ProjectsProjectIdProductivityLogsPostRequest.from_dict(rest_v10_projects_project_id_productivity_logs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


