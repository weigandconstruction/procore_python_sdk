# RestV10MeetingsPost201ResponseAttendeesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attendee id | [optional] 
**status** | **str** | Attendee status | [optional] 
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_meetings_post201_response_attendees_inner import RestV10MeetingsPost201ResponseAttendeesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10MeetingsPost201ResponseAttendeesInner from a JSON string
rest_v10_meetings_post201_response_attendees_inner_instance = RestV10MeetingsPost201ResponseAttendeesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10MeetingsPost201ResponseAttendeesInner.to_json())

# convert the object into a dict
rest_v10_meetings_post201_response_attendees_inner_dict = rest_v10_meetings_post201_response_attendees_inner_instance.to_dict()
# create an instance of RestV10MeetingsPost201ResponseAttendeesInner from a dict
rest_v10_meetings_post201_response_attendees_inner_from_dict = RestV10MeetingsPost201ResponseAttendeesInner.from_dict(rest_v10_meetings_post201_response_attendees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


