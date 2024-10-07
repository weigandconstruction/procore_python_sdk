# RestV10ProjectsProjectIdTimesheetsPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timesheet_id** | **int** | ID of Timesheet | [optional] 
**timecard_entries** | [**List[RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchRequestTimesheet]**](RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatchRequestTimesheet.md) | Timesheet object | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_timesheets_patch_request import RestV10ProjectsProjectIdTimesheetsPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimesheetsPatchRequest from a JSON string
rest_v10_projects_project_id_timesheets_patch_request_instance = RestV10ProjectsProjectIdTimesheetsPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimesheetsPatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_timesheets_patch_request_dict = rest_v10_projects_project_id_timesheets_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimesheetsPatchRequest from a dict
rest_v10_projects_project_id_timesheets_patch_request_from_dict = RestV10ProjectsProjectIdTimesheetsPatchRequest.from_dict(rest_v10_projects_project_id_timesheets_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


