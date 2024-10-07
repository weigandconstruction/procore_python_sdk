# RestV10ProjectsProjectIdIncidentsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incident** | [**RestV10ProjectsProjectIdIncidentsPostRequestIncident**](RestV10ProjectsProjectIdIncidentsPostRequestIncident.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_incidents_post_request import RestV10ProjectsProjectIdIncidentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdIncidentsPostRequest from a JSON string
rest_v10_projects_project_id_incidents_post_request_instance = RestV10ProjectsProjectIdIncidentsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdIncidentsPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_incidents_post_request_dict = rest_v10_projects_project_id_incidents_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdIncidentsPostRequest from a dict
rest_v10_projects_project_id_incidents_post_request_from_dict = RestV10ProjectsProjectIdIncidentsPostRequest.from_dict(rest_v10_projects_project_id_incidents_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


