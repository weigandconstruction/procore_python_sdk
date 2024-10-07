# RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInner

Group of meetings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_title** | **str** | Meeting group title | [optional] 
**meetings** | [**List[RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner]**](RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner.md) | Meetings | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_meetings_get200_response_one_of_inner import RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInner from a JSON string
rest_v11_projects_project_id_meetings_get200_response_one_of_inner_instance = RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_meetings_get200_response_one_of_inner_dict = rest_v11_projects_project_id_meetings_get200_response_one_of_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInner from a dict
rest_v11_projects_project_id_meetings_get200_response_one_of_inner_from_dict = RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInner.from_dict(rest_v11_projects_project_id_meetings_get200_response_one_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


