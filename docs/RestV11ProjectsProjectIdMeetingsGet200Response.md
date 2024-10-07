# RestV11ProjectsProjectIdMeetingsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meetings** | [**List[RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner]**](RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner.md) | Meetings | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_meetings_get200_response import RestV11ProjectsProjectIdMeetingsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdMeetingsGet200Response from a JSON string
rest_v11_projects_project_id_meetings_get200_response_instance = RestV11ProjectsProjectIdMeetingsGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdMeetingsGet200Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_meetings_get200_response_dict = rest_v11_projects_project_id_meetings_get200_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdMeetingsGet200Response from a dict
rest_v11_projects_project_id_meetings_get200_response_from_dict = RestV11ProjectsProjectIdMeetingsGet200Response.from_dict(rest_v11_projects_project_id_meetings_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


