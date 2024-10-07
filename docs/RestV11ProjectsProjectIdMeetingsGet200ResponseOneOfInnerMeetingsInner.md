# RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner

Meeting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Meeting id | [optional] 
**meeting_template_id** | **int** | Meeting Template id | [optional] 
**title** | **str** | Meeting title | [optional] 
**position** | **int** | Meeting position | [optional] 
**created_by_id** | **int** | Id of the user who created the meeting (returned only for meetings created after Dec 2023) | [optional] 
**description** | **str** | Meeting description | [optional] 
**mode** | **str** | Meeting mode | [optional] 
**starts_at** | **datetime** | Meeting start time | [optional] 
**ends_at** | **datetime** | Meeting finish time | [optional] 
**parent_id** | **int** | Meeting parent id | [optional] 
**location** | **str** | Meeting location | [optional] 
**meeting_topics_count** | **int** | The number of agendas associated with this meeting | [optional] 
**occurred** | **bool** | Indicates whether this meeting has already taken place | [optional] 
**is_private** | **bool** | Indicates whether this meeting is only visible to scheduled attendees and users with &#39;Admin&#39; level permissions to the Meetings tool. | [optional] 
**created_at** | **datetime** | Meeting created at | [optional] 
**updated_at** | **datetime** | Meeting updated at | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_meetings_get200_response_one_of_inner_meetings_inner import RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner from a JSON string
rest_v11_projects_project_id_meetings_get200_response_one_of_inner_meetings_inner_instance = RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_meetings_get200_response_one_of_inner_meetings_inner_dict = rest_v11_projects_project_id_meetings_get200_response_one_of_inner_meetings_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner from a dict
rest_v11_projects_project_id_meetings_get200_response_one_of_inner_meetings_inner_from_dict = RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner.from_dict(rest_v11_projects_project_id_meetings_get200_response_one_of_inner_meetings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


