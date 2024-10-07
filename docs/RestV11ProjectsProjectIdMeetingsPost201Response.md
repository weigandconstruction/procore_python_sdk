# RestV11ProjectsProjectIdMeetingsPost201Response

Meeting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Meeting id | [optional] 
**meeting_template_id** | **int** | Meeting Template id | [optional] 
**position** | **int** | Meeting position | [optional] 
**created_by_id** | **int** | Id of the user who created the meeting (returned only for meetings created after Dec 2023) | [optional] 
**title** | **str** | Meeting title | [optional] 
**location** | **str** | Meeting location | [optional] 
**occurred** | **bool** | Meeting occurred status | [optional] 
**starts_at** | **datetime** | Meeting start time | [optional] 
**ends_at** | **datetime** | Meeting finish time | [optional] 
**time_zone** | **str** | Meeting Timezone | [optional] 
**is_private** | **bool** | Meeting private status | [optional] 
**is_draft** | **bool** | Meeting draft status | [optional] 
**mode** | **str** | Meeting mode | [optional] 
**created_at** | **datetime** | Meeting created at | [optional] 
**updated_at** | **datetime** | Meeting updated at | [optional] 
**description** | **str** | Meeting description | [optional] 
**conclusion** | **str** | Meeting conclusion | [optional] 
**remote_meeting_url** | **str** | Url to join remote meeting | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Meeting attachments | [optional] 
**attendees** | [**List[RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner]**](RestV11ProjectsProjectIdMeetingsPost201ResponseAttendeesInner.md) | Meeting attendees | [optional] 
**meeting_categories** | [**List[RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner]**](RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner.md) | Meeting categories | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_meetings_post201_response import RestV11ProjectsProjectIdMeetingsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdMeetingsPost201Response from a JSON string
rest_v11_projects_project_id_meetings_post201_response_instance = RestV11ProjectsProjectIdMeetingsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdMeetingsPost201Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_meetings_post201_response_dict = rest_v11_projects_project_id_meetings_post201_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdMeetingsPost201Response from a dict
rest_v11_projects_project_id_meetings_post201_response_from_dict = RestV11ProjectsProjectIdMeetingsPost201Response.from_dict(rest_v11_projects_project_id_meetings_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


