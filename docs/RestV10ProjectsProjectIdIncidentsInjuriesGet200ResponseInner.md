# RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The record type, i.e. &#39;injury&#39;, &#39;near_miss&#39;, &#39;environmental&#39;, or &#39;property_damage&#39; | [optional] 
**date_returned_to_work** | **date** | Date returned to work | [optional] 
**affected_party** | [**Party1**](Party1.md) |  | [optional] 
**affected_person** | [**RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInnerAllOfAffectedPerson**](RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInnerAllOfAffectedPerson.md) |  | [optional] 
**harm_source** | [**HarmSource**](HarmSource.md) |  | [optional] 
**date_of_death** | **date** | Date of death | [optional] 
**filing_type** | **str** | Filing Type | [optional] 
**hospitalized_overnight** | **bool** | Represents whether the injured person was hospitalized overnight | [optional] 
**recordable** | **bool** | Represents whether the Injury record is recordable | [optional] 
**treated_in_er** | **bool** | Represents whether the injured person was treated in the ER | [optional] 
**treatment_facility_address** | **str** | The street address of the treatment facility | [optional] 
**treatment_facility** | **str** | The name of the treatment facility | [optional] 
**treatment_provider** | **str** | The name of the treatment provider | [optional] 
**work_days_absent** | **int** | The number of days absent from work | [optional] 
**work_days_restricted** | **int** | The number of days on restricted work | [optional] 
**work_days_transferred** | **int** | The number of days transferred | [optional] 
**body_diagram_type** | **str** | Body Type displayed in Body Diagram | [optional] 
**affliction_type** | [**AfflictionType**](AfflictionType.md) |  | [optional] 
**affected_body_part** | **str** | DEPRECATED. The body part affected by the affliction | [optional] 
**affected_body_parts** | **List[str]** | Array of body parts affected by the affliction | [optional] 
**afflictions** | [**List[IncidentAffliction]**](IncidentAffliction.md) | DEPRECATED. Array of afflictions affecting the injured person. Currently this is limited to one. | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**body_parts** | [**List[BodyPart]**](BodyPart.md) | Body parts affected by the injury | [optional] 
**id** | **int** | Incident Record ID | [optional] 
**number** | **int** | The number of the Record | [optional] 
**full_number** | **str** | The Incident Number combined with the Record Number | [optional] 
**incident_id** | **int** | The id of the Incident to which the record belongs | [optional] 
**incident_title** | **str** | The title of the Incident to which the record belongs | [optional] 
**incident_private** | **bool** | Indicates whether the Incident to which the record belongs is private | [optional] 
**summary** | **str** | Summary combining the affliction type, body part affected, and source of harm. | [optional] 
**description_plain_text** | **str** | Description of event | [optional] 
**description** | **str** | Description of event in Rich Text format | [optional] 
**affected_company** | [**RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor**](RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**deleted_at** | **datetime** | Timestamp of deletion | [optional] 
**managed_equipment** | [**RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInnerAllOfManagedEquipment**](RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInnerAllOfManagedEquipment.md) |  | [optional] 
**incident_created_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**work_activity** | [**WorkActivity1**](WorkActivity1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_incidents_injuries_get200_response_inner import RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_incidents_injuries_get200_response_inner_instance = RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_incidents_injuries_get200_response_inner_dict = rest_v10_projects_project_id_incidents_injuries_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner from a dict
rest_v10_projects_project_id_incidents_injuries_get200_response_inner_from_dict = RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner.from_dict(rest_v10_projects_project_id_incidents_injuries_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


