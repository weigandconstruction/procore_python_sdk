# RestV10ProjectsProjectIdProjectDatesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_dates** | [**ScheduleDates**](ScheduleDates.md) |  | [optional] 
**project_dates** | [**List[RestV10ProjectsProjectIdProjectDatesGet200ResponseProjectDatesInner]**](RestV10ProjectsProjectIdProjectDatesGet200ResponseProjectDatesInner.md) | Array of Project Dates | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_project_dates_get200_response import RestV10ProjectsProjectIdProjectDatesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdProjectDatesGet200Response from a JSON string
rest_v10_projects_project_id_project_dates_get200_response_instance = RestV10ProjectsProjectIdProjectDatesGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdProjectDatesGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_project_dates_get200_response_dict = rest_v10_projects_project_id_project_dates_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdProjectDatesGet200Response from a dict
rest_v10_projects_project_id_project_dates_get200_response_from_dict = RestV10ProjectsProjectIdProjectDatesGet200Response.from_dict(rest_v10_projects_project_id_project_dates_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


