# IncidentNormal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**deleted_at** | **datetime** | Timestamp of deletion | [optional] 
**description** | **str** | Description of the Incident | [optional] 
**event_date** | **datetime** | Date of Incident occurrence | [optional] 
**number** | **int** | Number | [optional] 
**private** | **bool** | Indicates whether an Incident is private | [optional] 
**recordable** | **bool** | Indicates whether an Incident is recordable | [optional] 
**records_count** | **int** | Number of Records associated to the Incident | [optional] 
**open_observations_count** | **int** | Number of Open Observations associated to the Incident | [optional] 
**closed_observations_count** | **int** | Number of Closed Observations associated to the Incident | [optional] 
**actions_count** | **int** | Number of Actions associated to the Incident | [optional] 
**witness_statements_count** | **int** | Number of Witness Statements associated to the Incident | [optional] 
**status** | **str** | Status | [optional] 
**time_unknown** | **bool** | Indicates that the time of the Incident occurrence is unknown | [optional] 
**title** | **str** | Incident Title | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**created_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**contributing_behavior** | [**ContributingBehavior1**](ContributingBehavior1.md) |  | [optional] 
**contributing_condition** | [**ContributingCondition1**](ContributingCondition1.md) |  | [optional] 
**hazard** | [**Hazard1**](Hazard1.md) |  | [optional] 
**location** | [**Location6**](Location6.md) |  | [optional] 
**attachments_count** | **int** | Number of Attachments attached to the Incident | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**attachments** | [**List[IncidentAttachment]**](IncidentAttachment.md) | Attachments | [optional] 
**distribution_members** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**environmentals** | [**List[IncidentNormalAllOfEnvironmentalsInner]**](IncidentNormalAllOfEnvironmentalsInner.md) | Environmentals | [optional] 
**injuries** | [**List[IncidentNormalAllOfInjuriesInner]**](IncidentNormalAllOfInjuriesInner.md) | Injuries | [optional] 
**near_misses** | [**List[IncidentNormalAllOfNearMissesInner]**](IncidentNormalAllOfNearMissesInner.md) | NearMisses | [optional] 
**property_damages** | [**List[IncidentNormalAllOfPropertyDamagesInner]**](IncidentNormalAllOfPropertyDamagesInner.md) | PropertyDamages | [optional] 
**witness_statements** | [**List[IncidentNormalAllOfWitnessStatementsInner]**](IncidentNormalAllOfWitnessStatementsInner.md) | WitnessStatements | [optional] 
**actions** | [**List[IncidentNormalAllOfActionsInner]**](IncidentNormalAllOfActionsInner.md) | Actions | [optional] 

## Example

```python
from procore_sdk.models.incident_normal import IncidentNormal

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentNormal from a JSON string
incident_normal_instance = IncidentNormal.from_json(json)
# print the JSON string representation of the object
print(IncidentNormal.to_json())

# convert the object into a dict
incident_normal_dict = incident_normal_instance.to_dict()
# create an instance of IncidentNormal from a dict
incident_normal_from_dict = IncidentNormal.from_dict(incident_normal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


