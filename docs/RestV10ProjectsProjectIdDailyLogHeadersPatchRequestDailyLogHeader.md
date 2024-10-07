# RestV10ProjectsProjectIdDailyLogHeadersPatchRequestDailyLogHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** | Set the completion status for the day | 
**distributed** | **bool** | Distribute the Daily Log for the day | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_log_headers_patch_request_daily_log_header import RestV10ProjectsProjectIdDailyLogHeadersPatchRequestDailyLogHeader

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyLogHeadersPatchRequestDailyLogHeader from a JSON string
rest_v10_projects_project_id_daily_log_headers_patch_request_daily_log_header_instance = RestV10ProjectsProjectIdDailyLogHeadersPatchRequestDailyLogHeader.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyLogHeadersPatchRequestDailyLogHeader.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_log_headers_patch_request_daily_log_header_dict = rest_v10_projects_project_id_daily_log_headers_patch_request_daily_log_header_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyLogHeadersPatchRequestDailyLogHeader from a dict
rest_v10_projects_project_id_daily_log_headers_patch_request_daily_log_header_from_dict = RestV10ProjectsProjectIdDailyLogHeadersPatchRequestDailyLogHeader.from_dict(rest_v10_projects_project_id_daily_log_headers_patch_request_daily_log_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


