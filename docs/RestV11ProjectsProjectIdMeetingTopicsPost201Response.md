# RestV11ProjectsProjectIdMeetingTopicsPost201Response

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
from procore_sdk.models.rest_v11_projects_project_id_meeting_topics_post201_response import RestV11ProjectsProjectIdMeetingTopicsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdMeetingTopicsPost201Response from a JSON string
rest_v11_projects_project_id_meeting_topics_post201_response_instance = RestV11ProjectsProjectIdMeetingTopicsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdMeetingTopicsPost201Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_meeting_topics_post201_response_dict = rest_v11_projects_project_id_meeting_topics_post201_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdMeetingTopicsPost201Response from a dict
rest_v11_projects_project_id_meeting_topics_post201_response_from_dict = RestV11ProjectsProjectIdMeetingTopicsPost201Response.from_dict(rest_v11_projects_project_id_meeting_topics_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


