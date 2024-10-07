# RestV11ProjectsProjectIdMeetingsGet200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meetings** | [**List[RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner]**](RestV11ProjectsProjectIdMeetingsGet200ResponseOneOfInnerMeetingsInner.md) | Meetings | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_meetings_get200_response_one_of import RestV11ProjectsProjectIdMeetingsGet200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdMeetingsGet200ResponseOneOf from a JSON string
rest_v11_projects_project_id_meetings_get200_response_one_of_instance = RestV11ProjectsProjectIdMeetingsGet200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdMeetingsGet200ResponseOneOf.to_json())

# convert the object into a dict
rest_v11_projects_project_id_meetings_get200_response_one_of_dict = rest_v11_projects_project_id_meetings_get200_response_one_of_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdMeetingsGet200ResponseOneOf from a dict
rest_v11_projects_project_id_meetings_get200_response_one_of_from_dict = RestV11ProjectsProjectIdMeetingsGet200ResponseOneOf.from_dict(rest_v11_projects_project_id_meetings_get200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


