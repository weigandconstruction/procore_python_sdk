# RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incident_action** | [**RestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction**](RestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_incidents_actions_id_patch_request import RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest from a JSON string
rest_v10_projects_project_id_incidents_actions_id_patch_request_instance = RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_incidents_actions_id_patch_request_dict = rest_v10_projects_project_id_incidents_actions_id_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest from a dict
rest_v10_projects_project_id_incidents_actions_id_patch_request_from_dict = RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest.from_dict(rest_v10_projects_project_id_incidents_actions_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


