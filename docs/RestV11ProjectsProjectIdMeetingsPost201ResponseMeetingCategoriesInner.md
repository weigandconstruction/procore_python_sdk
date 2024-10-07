# RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Meeting category id | [optional] 
**title** | **str** | Meeting category topic | [optional] 
**position** | **int** | Meeting category position | [optional] 
**meeting_topic** | [**List[RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner]**](RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner.md) | Meeting category meeting topics | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_meetings_post201_response_meeting_categories_inner import RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner from a JSON string
rest_v11_projects_project_id_meetings_post201_response_meeting_categories_inner_instance = RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_meetings_post201_response_meeting_categories_inner_dict = rest_v11_projects_project_id_meetings_post201_response_meeting_categories_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner from a dict
rest_v11_projects_project_id_meetings_post201_response_meeting_categories_inner_from_dict = RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner.from_dict(rest_v11_projects_project_id_meetings_post201_response_meeting_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


