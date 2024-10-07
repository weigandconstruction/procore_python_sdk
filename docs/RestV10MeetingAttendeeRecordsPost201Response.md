# RestV10MeetingAttendeeRecordsPost201Response

Meeting Attendee record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Meeting Attendee record ID | [optional] 
**meeting_id** | **int** | ID of the corresponding Meeting | [optional] 
**status** | **str** | Attendance status | [optional] 
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_meeting_attendee_records_post201_response import RestV10MeetingAttendeeRecordsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10MeetingAttendeeRecordsPost201Response from a JSON string
rest_v10_meeting_attendee_records_post201_response_instance = RestV10MeetingAttendeeRecordsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10MeetingAttendeeRecordsPost201Response.to_json())

# convert the object into a dict
rest_v10_meeting_attendee_records_post201_response_dict = rest_v10_meeting_attendee_records_post201_response_instance.to_dict()
# create an instance of RestV10MeetingAttendeeRecordsPost201Response from a dict
rest_v10_meeting_attendee_records_post201_response_from_dict = RestV10MeetingAttendeeRecordsPost201Response.from_dict(rest_v10_meeting_attendee_records_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


