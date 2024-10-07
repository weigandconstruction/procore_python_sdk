# RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attendee id | [optional] 
**status** | **str** | Attendee status | [optional] 
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_meetings_post201_response_attendees_inner import RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner from a JSON string
rest_v11_projects_project_id_meetings_post201_response_attendees_inner_instance = RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_meetings_post201_response_attendees_inner_dict = rest_v11_projects_project_id_meetings_post201_response_attendees_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner from a dict
rest_v11_projects_project_id_meetings_post201_response_attendees_inner_from_dict = RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner.from_dict(rest_v11_projects_project_id_meetings_post201_response_attendees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


