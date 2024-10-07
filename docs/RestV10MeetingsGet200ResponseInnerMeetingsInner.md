# RestV10MeetingsGet200ResponseInnerMeetingsInner

Meeting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Meeting id | [optional] 
**title** | **str** | Meeting title | [optional] 
**position** | **int** | Meeting position | [optional] 
**created_by_id** | **int** | Id of the user who created the meeting (returned only for meetings created after Dec 2023) | [optional] 
**description** | **str** | Meeting description | [optional] 
**mode** | **str** | Meeting mode | [optional] 
**meeting_date** | **date** | Meeting date | [optional] 
**parent_id** | **int** | Meeting parent id | [optional] 
**location** | **str** | Meeting location | [optional] 
**meeting_topics_count** | **int** | The number of agendas associated with this meeting | [optional] 
**occurred** | **bool** | Indicates whether this meeting has already taken place | [optional] 
**is_private** | **bool** | Indicates whether this meeting is only visible to scheduled attendees and users with &#39;Admin&#39; level permissions to the Meetings tool. | [optional] 
**created_at** | **datetime** | Meeting created at | [optional] 
**updated_at** | **datetime** | Meeting updated at | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_meetings_get200_response_inner_meetings_inner import RestV10MeetingsGet200ResponseInnerMeetingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10MeetingsGet200ResponseInnerMeetingsInner from a JSON string
rest_v10_meetings_get200_response_inner_meetings_inner_instance = RestV10MeetingsGet200ResponseInnerMeetingsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10MeetingsGet200ResponseInnerMeetingsInner.to_json())

# convert the object into a dict
rest_v10_meetings_get200_response_inner_meetings_inner_dict = rest_v10_meetings_get200_response_inner_meetings_inner_instance.to_dict()
# create an instance of RestV10MeetingsGet200ResponseInnerMeetingsInner from a dict
rest_v10_meetings_get200_response_inner_meetings_inner_from_dict = RestV10MeetingsGet200ResponseInnerMeetingsInner.from_dict(rest_v10_meetings_get200_response_inner_meetings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


