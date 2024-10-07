# RestV10ProjectsProjectIdDailyLogsClonesPost201Response

An object where keys represent the copied log types, and their values are arrays of the newly-copied logs. The object will be empty if no logs are copied, such as when the to_date is already completed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes_log** | [**RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLog**](RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLog.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_clones_post201_response import RestV10ProjectsProjectIdDailyLogsClonesPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyLogsClonesPost201Response from a JSON string
rest_v10_projects_project_id_daily_logs_clones_post201_response_instance = RestV10ProjectsProjectIdDailyLogsClonesPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyLogsClonesPost201Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_logs_clones_post201_response_dict = rest_v10_projects_project_id_daily_logs_clones_post201_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyLogsClonesPost201Response from a dict
rest_v10_projects_project_id_daily_logs_clones_post201_response_from_dict = RestV10ProjectsProjectIdDailyLogsClonesPost201Response.from_dict(rest_v10_projects_project_id_daily_logs_clones_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


