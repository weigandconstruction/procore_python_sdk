# RestV10ProjectsProjectIdDailyLogsClonesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **date** | Date to copy logs from in YYYY-MM-DD format | 
**to_date** | **date** | Date to copy logs to in YYYY-MM-DD format | 
**log_types** | **List[str]** | Log types to copy. More than one log type can be provided.  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_clones_post_request import RestV10ProjectsProjectIdDailyLogsClonesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyLogsClonesPostRequest from a JSON string
rest_v10_projects_project_id_daily_logs_clones_post_request_instance = RestV10ProjectsProjectIdDailyLogsClonesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyLogsClonesPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_logs_clones_post_request_dict = rest_v10_projects_project_id_daily_logs_clones_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyLogsClonesPostRequest from a dict
rest_v10_projects_project_id_daily_logs_clones_post_request_from_dict = RestV10ProjectsProjectIdDailyLogsClonesPostRequest.from_dict(rest_v10_projects_project_id_daily_logs_clones_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


