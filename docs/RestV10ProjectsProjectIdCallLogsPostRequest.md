# RestV10ProjectsProjectIdCallLogsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_log** | [**RestV10ProjectsProjectIdCallLogsPostRequestCallLog**](RestV10ProjectsProjectIdCallLogsPostRequestCallLog.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_call_logs_post_request import RestV10ProjectsProjectIdCallLogsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdCallLogsPostRequest from a JSON string
rest_v10_projects_project_id_call_logs_post_request_instance = RestV10ProjectsProjectIdCallLogsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdCallLogsPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_call_logs_post_request_dict = rest_v10_projects_project_id_call_logs_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdCallLogsPostRequest from a dict
rest_v10_projects_project_id_call_logs_post_request_from_dict = RestV10ProjectsProjectIdCallLogsPostRequest.from_dict(rest_v10_projects_project_id_call_logs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


