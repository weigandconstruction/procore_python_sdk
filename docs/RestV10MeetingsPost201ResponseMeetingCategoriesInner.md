# RestV10MeetingsPost201ResponseMeetingCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Meeting category id | [optional] 
**title** | **str** | Meeting category topic | [optional] 
**position** | **int** | Meeting category position | [optional] 
**meeting_topic** | [**List[RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner]**](RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner.md) | Meeting category meeting topics | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_meetings_post201_response_meeting_categories_inner import RestV10MeetingsPost201ResponseMeetingCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10MeetingsPost201ResponseMeetingCategoriesInner from a JSON string
rest_v10_meetings_post201_response_meeting_categories_inner_instance = RestV10MeetingsPost201ResponseMeetingCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10MeetingsPost201ResponseMeetingCategoriesInner.to_json())

# convert the object into a dict
rest_v10_meetings_post201_response_meeting_categories_inner_dict = rest_v10_meetings_post201_response_meeting_categories_inner_instance.to_dict()
# create an instance of RestV10MeetingsPost201ResponseMeetingCategoriesInner from a dict
rest_v10_meetings_post201_response_meeting_categories_inner_from_dict = RestV10MeetingsPost201ResponseMeetingCategoriesInner.from_dict(rest_v10_meetings_post201_response_meeting_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


