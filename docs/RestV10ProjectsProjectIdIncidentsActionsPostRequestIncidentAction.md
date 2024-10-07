# RestV10ProjectsProjectIdIncidentsActionsPostRequestIncidentAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incident_id** | **int** | The ID of the Incident | 
**action_type_id** | **int** | The ID of the Action Type | 
**description** | **str** | Description of action taken in rich text form. | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_incidents_actions_post_request_incident_action import RestV10ProjectsProjectIdIncidentsActionsPostRequestIncidentAction

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdIncidentsActionsPostRequestIncidentAction from a JSON string
rest_v10_projects_project_id_incidents_actions_post_request_incident_action_instance = RestV10ProjectsProjectIdIncidentsActionsPostRequestIncidentAction.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdIncidentsActionsPostRequestIncidentAction.to_json())

# convert the object into a dict
rest_v10_projects_project_id_incidents_actions_post_request_incident_action_dict = rest_v10_projects_project_id_incidents_actions_post_request_incident_action_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdIncidentsActionsPostRequestIncidentAction from a dict
rest_v10_projects_project_id_incidents_actions_post_request_incident_action_from_dict = RestV10ProjectsProjectIdIncidentsActionsPostRequestIncidentAction.from_dict(rest_v10_projects_project_id_incidents_actions_post_request_incident_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


