# RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Incident Record ID | [optional] 
**number** | **int** | The number of the Record | [optional] 
**full_number** | **str** | The Incident Number combined with the Record Number | [optional] 
**incident_id** | **int** | The id of the Incident to which the record belongs | [optional] 
**recordable** | **bool** | Indicates whether the Incident Record is recordable | [optional] 
**type** | **str** | The type of incident record (environmental, injury, near_miss, property_damage) | [optional] 
**date_returned_to_work** | **date** | Date returned to work | [optional] 
**affected_party** | [**Party**](Party.md) |  | [optional] 
**affected_person** | [**RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjuryAffectedPerson**](RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjuryAffectedPerson.md) |  | [optional] 
**harm_source** | [**HarmSource1**](HarmSource1.md) |  | [optional] 
**date_of_death** | **date** | Date of death | [optional] 
**filing_type** | **str** | Filing Type | [optional] 
**hospitalized_overnight** | **bool** | Represents whether the injured person was hospitalized overnight | [optional] 
**treated_in_er** | **bool** | Represents whether the injured person was treated in the ER | [optional] 
**treatment_facility_address** | **str** | The street address of the treatment facility | [optional] 
**treatment_facility** | **str** | The name of the treatment facility | [optional] 
**treatment_provider** | **str** | The name of the treatment provider | [optional] 
**work_days_absent** | **int** | The number of days absent from work | [optional] 
**work_days_restricted** | **int** | The number of days on restricted work | [optional] 
**work_days_transferred** | **int** | The number of days transferred | [optional] 
**body_diagram_type** | **str** | Body Type displayed in Body Diagram | [optional] 
**affliction_type** | [**AfflictionType1**](AfflictionType1.md) |  | [optional] 
**affected_body_part** | **str** | DEPRECATED. The body part affected by the affliction | [optional] 
**affected_body_parts** | **List[str]** | Array of body parts affected by the affliction | [optional] 
**afflictions** | [**List[IncidentAffliction1]**](IncidentAffliction1.md) | DEPRECATED. Array of afflictions affecting the injured person. Currently this is limited to one. | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**body_parts** | [**List[BodyPart1]**](BodyPart1.md) | Body parts affected by the injury | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_incidents_alerts_get200_response_inner_injury import RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury from a JSON string
rest_v10_projects_project_id_incidents_alerts_get200_response_inner_injury_instance = RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury.to_json())

# convert the object into a dict
rest_v10_projects_project_id_incidents_alerts_get200_response_inner_injury_dict = rest_v10_projects_project_id_incidents_alerts_get200_response_inner_injury_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury from a dict
rest_v10_projects_project_id_incidents_alerts_get200_response_inner_injury_from_dict = RestV10ProjectsProjectIdIncidentsAlertsGet200ResponseInnerInjury.from_dict(rest_v10_projects_project_id_incidents_alerts_get200_response_inner_injury_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


