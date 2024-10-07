# RestV10ProjectsProjectIdScheduleGet200ResponseType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Schedule type key | [optional] 
**p6_id** | **str** | Schedule type Primavera P6 Identifier | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_schedule_get200_response_type import RestV10ProjectsProjectIdScheduleGet200ResponseType

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdScheduleGet200ResponseType from a JSON string
rest_v10_projects_project_id_schedule_get200_response_type_instance = RestV10ProjectsProjectIdScheduleGet200ResponseType.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdScheduleGet200ResponseType.to_json())

# convert the object into a dict
rest_v10_projects_project_id_schedule_get200_response_type_dict = rest_v10_projects_project_id_schedule_get200_response_type_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdScheduleGet200ResponseType from a dict
rest_v10_projects_project_id_schedule_get200_response_type_from_dict = RestV10ProjectsProjectIdScheduleGet200ResponseType.from_dict(rest_v10_projects_project_id_schedule_get200_response_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


