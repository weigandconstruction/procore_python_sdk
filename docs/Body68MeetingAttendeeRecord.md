# Body68MeetingAttendeeRecord

Meeting Attendee record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Attendance status | [optional] 
**login_information_id** | **int** | The ID of the User to associate with the Meeting | [optional] 

## Example

```python
from procore_sdk.models.body68_meeting_attendee_record import Body68MeetingAttendeeRecord

# TODO update the JSON string below
json = "{}"
# create an instance of Body68MeetingAttendeeRecord from a JSON string
body68_meeting_attendee_record_instance = Body68MeetingAttendeeRecord.from_json(json)
# print the JSON string representation of the object
print(Body68MeetingAttendeeRecord.to_json())

# convert the object into a dict
body68_meeting_attendee_record_dict = body68_meeting_attendee_record_instance.to_dict()
# create an instance of Body68MeetingAttendeeRecord from a dict
body68_meeting_attendee_record_from_dict = Body68MeetingAttendeeRecord.from_dict(body68_meeting_attendee_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


