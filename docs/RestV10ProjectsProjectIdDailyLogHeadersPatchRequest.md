# RestV10ProjectsProjectIdDailyLogHeadersPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily_log_header** | [**RestV10ProjectsProjectIdDailyLogHeadersPatchRequestDailyLogHeader**](RestV10ProjectsProjectIdDailyLogHeadersPatchRequestDailyLogHeader.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_log_headers_patch_request import RestV10ProjectsProjectIdDailyLogHeadersPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyLogHeadersPatchRequest from a JSON string
rest_v10_projects_project_id_daily_log_headers_patch_request_instance = RestV10ProjectsProjectIdDailyLogHeadersPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyLogHeadersPatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_log_headers_patch_request_dict = rest_v10_projects_project_id_daily_log_headers_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyLogHeadersPatchRequest from a dict
rest_v10_projects_project_id_daily_log_headers_patch_request_from_dict = RestV10ProjectsProjectIdDailyLogHeadersPatchRequest.from_dict(rest_v10_projects_project_id_daily_log_headers_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


