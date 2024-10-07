# RestV10MeetingsPost201Response

Meeting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Meeting id | [optional] 
**position** | **int** | Meeting position | [optional] 
**created_by_id** | **int** | Id of the user who created the meeting (returned only for meetings created after Dec 2023) | [optional] 
**title** | **str** | Meeting title | [optional] 
**location** | **str** | Meeting location | [optional] 
**meeting_date** | **date** | Meeting date | [optional] 
**occurred** | **bool** | Meeting occurred status | [optional] 
**start_time** | **str** | Meeting start time | [optional] 
**finish_time** | **str** | Meeting finish time | [optional] 
**time_zone** | **str** | Meeting Timezone | [optional] 
**is_private** | **bool** | Meeting private status | [optional] 
**is_draft** | **bool** | Meeting draft status | [optional] 
**mode** | **str** | Meeting mode | [optional] 
**description** | **str** | Meeting description | [optional] 
**conclusion** | **str** | Meeting conclusion | [optional] 
**created_at** | **datetime** | Meeting created at | [optional] 
**updated_at** | **datetime** | Meeting updated at | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Meeting attachments | [optional] 
**attendees** | [**List[RestV10MeetingsPost201ResponseAttendeesInner]**](RestV10MeetingsPost201ResponseAttendeesInner.md) | Meeting attendees | [optional] 
**meeting_categories** | [**List[RestV10MeetingsPost201ResponseMeetingCategoriesInner]**](RestV10MeetingsPost201ResponseMeetingCategoriesInner.md) | Meeting categories | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_meetings_post201_response import RestV10MeetingsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10MeetingsPost201Response from a JSON string
rest_v10_meetings_post201_response_instance = RestV10MeetingsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10MeetingsPost201Response.to_json())

# convert the object into a dict
rest_v10_meetings_post201_response_dict = rest_v10_meetings_post201_response_instance.to_dict()
# create an instance of RestV10MeetingsPost201Response from a dict
rest_v10_meetings_post201_response_from_dict = RestV10MeetingsPost201Response.from_dict(rest_v10_meetings_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


