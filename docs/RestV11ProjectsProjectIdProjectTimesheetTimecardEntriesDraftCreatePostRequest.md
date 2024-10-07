# RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesDraftCreatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The Date of the Timesheet | [optional] 
**timecard_entries** | [**List[TimecardEntry]**](TimecardEntry.md) | Timecard Entries to Create | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_project_timesheet_timecard_entries_draft_create_post_request import RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesDraftCreatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesDraftCreatePostRequest from a JSON string
rest_v11_projects_project_id_project_timesheet_timecard_entries_draft_create_post_request_instance = RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesDraftCreatePostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesDraftCreatePostRequest.to_json())

# convert the object into a dict
rest_v11_projects_project_id_project_timesheet_timecard_entries_draft_create_post_request_dict = rest_v11_projects_project_id_project_timesheet_timecard_entries_draft_create_post_request_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesDraftCreatePostRequest from a dict
rest_v11_projects_project_id_project_timesheet_timecard_entries_draft_create_post_request_from_dict = RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesDraftCreatePostRequest.from_dict(rest_v11_projects_project_id_project_timesheet_timecard_entries_draft_create_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


