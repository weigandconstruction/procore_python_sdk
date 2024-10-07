# RestV10ProjectsProjectIdTimesheetsDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | IDs of Timesheets to be deleted | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_timesheets_delete_request import RestV10ProjectsProjectIdTimesheetsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimesheetsDeleteRequest from a JSON string
rest_v10_projects_project_id_timesheets_delete_request_instance = RestV10ProjectsProjectIdTimesheetsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimesheetsDeleteRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_timesheets_delete_request_dict = rest_v10_projects_project_id_timesheets_delete_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimesheetsDeleteRequest from a dict
rest_v10_projects_project_id_timesheets_delete_request_from_dict = RestV10ProjectsProjectIdTimesheetsDeleteRequest.from_dict(rest_v10_projects_project_id_timesheets_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


