# IncidentCompact


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
**contributing_behavior** | [**ContributingBehavior**](ContributingBehavior.md) |  | [optional] 
**contributing_condition** | [**ContributingCondition**](ContributingCondition.md) |  | [optional] 
**hazard** | [**Hazard**](Hazard.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**attachments_count** | **int** | Number of Attachments attached to the Incident | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.incident_compact import IncidentCompact

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentCompact from a JSON string
incident_compact_instance = IncidentCompact.from_json(json)
# print the JSON string representation of the object
print(IncidentCompact.to_json())

# convert the object into a dict
incident_compact_dict = incident_compact_instance.to_dict()
# create an instance of IncidentCompact from a dict
incident_compact_from_dict = IncidentCompact.from_dict(incident_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


