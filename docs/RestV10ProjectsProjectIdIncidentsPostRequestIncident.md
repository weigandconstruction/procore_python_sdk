# RestV10ProjectsProjectIdIncidentsPostRequestIncident


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the Incident | [optional] 
**event_date** | **datetime** | Iso8601 datetime of Incident occurrence. If time is unknown, send in the date at 0:00 project time converted to UTC. | [optional] 
**distribution_member_ids** | **List[int]** | An Array of the IDs of the Distribution Members | [optional] 
**private** | **bool** | Indicates whether an Incident is private | [optional] 
**recordable** | **bool** | Indicates whether an Incident is recordable | [optional] 
**status** | **str** | Status | [optional] 
**time_unknown** | **bool** | Indicates that the time of the Incident occurrence is unknown | [optional] 
**title** | **str** | Incident Title | [optional] 
**contributing_behavior_id** | **int** | The ID of a Contributing Behavior | [optional] 
**contributing_condition_id** | **int** | The ID of a Contributing Condition | [optional] 
**hazard_id** | **int** | The ID of a Hazard | [optional] 
**location_id** | **int** | The ID of a Location | [optional] 
**environmentals** | [**List[IncidentEnvironmentalUpdateParameters]**](IncidentEnvironmentalUpdateParameters.md) | Associated Environmentals to create | [optional] 
**injuries** | [**List[IncidentInjuryUpdateParameters]**](IncidentInjuryUpdateParameters.md) | Associated Injuries to create | [optional] 
**near_misses** | [**List[IncidentNearMissUpdateParameters]**](IncidentNearMissUpdateParameters.md) | Associated Near Misses to create | [optional] 
**property_damages** | [**List[IncidentPropertyDamageUpdateParameters]**](IncidentPropertyDamageUpdateParameters.md) | Associated Property Damages to create | [optional] 
**witness_statements_attributes** | [**List[IncidentWitnessStatementUpdateParameters1]**](IncidentWitnessStatementUpdateParameters1.md) | Associated Witness Statement to create | [optional] 
**upload_uuids** | **List[str]** | Array of uploaded file UUIDs. | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_incidents_post_request_incident import RestV10ProjectsProjectIdIncidentsPostRequestIncident

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdIncidentsPostRequestIncident from a JSON string
rest_v10_projects_project_id_incidents_post_request_incident_instance = RestV10ProjectsProjectIdIncidentsPostRequestIncident.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdIncidentsPostRequestIncident.to_json())

# convert the object into a dict
rest_v10_projects_project_id_incidents_post_request_incident_dict = rest_v10_projects_project_id_incidents_post_request_incident_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdIncidentsPostRequestIncident from a dict
rest_v10_projects_project_id_incidents_post_request_incident_from_dict = RestV10ProjectsProjectIdIncidentsPostRequestIncident.from_dict(rest_v10_projects_project_id_incidents_post_request_incident_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


