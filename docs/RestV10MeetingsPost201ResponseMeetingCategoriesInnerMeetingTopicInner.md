# RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner

Meeting topic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Meeting topic id | [optional] 
**number** | **str** | Meeting topic number | [optional] 
**created_on** | **date** | Meeting topic created on | [optional] 
**position** | **int** | Meeting topic position | [optional] 
**due_date** | **date** | Meeting topic due date | [optional] 
**priority** | **str** | Meeting topic priority | [optional] 
**status** | **str** | Meeting topic status | [optional] 
**title** | **str** | Meeting topic title | [optional] 
**minutes** | **str** | Meeting topic minutes | [optional] 
**description** | **str** | Meeting topic description | [optional] 
**meeting_category** | [**RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInnerMeetingCategory**](RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInnerMeetingCategory.md) |  | [optional] 
**assignments** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) | Meeting topic assignments | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Meeting topic attachments | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_meetings_post201_response_meeting_categories_inner_meeting_topic_inner import RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner from a JSON string
rest_v10_meetings_post201_response_meeting_categories_inner_meeting_topic_inner_instance = RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner.from_json(json)
# print the JSON string representation of the object
print(RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner.to_json())

# convert the object into a dict
rest_v10_meetings_post201_response_meeting_categories_inner_meeting_topic_inner_dict = rest_v10_meetings_post201_response_meeting_categories_inner_meeting_topic_inner_instance.to_dict()
# create an instance of RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner from a dict
rest_v10_meetings_post201_response_meeting_categories_inner_meeting_topic_inner_from_dict = RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner.from_dict(rest_v10_meetings_post201_response_meeting_categories_inner_meeting_topic_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


