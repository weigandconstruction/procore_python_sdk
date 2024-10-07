# IncidentNormalAllOfWitnessStatementsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Witness Statement ID | [optional] 
**incident_id** | **int** | Incident ID | [optional] 
**attachments** | [**List[IncidentAttachment]**](IncidentAttachment.md) |  | [optional] 
**statement** | **str** | The account of the event by the witness in rich text form. | [optional] 
**statement_plain_text** | **str** | The account of the event by the witness in plain text form. | [optional] 
**date_received** | **date** | Date that the Witness Statement was received. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**deleted_at** | **datetime** | Timestamp of deletion | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**witness** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness.md) |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.incident_normal_all_of_witness_statements_inner import IncidentNormalAllOfWitnessStatementsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentNormalAllOfWitnessStatementsInner from a JSON string
incident_normal_all_of_witness_statements_inner_instance = IncidentNormalAllOfWitnessStatementsInner.from_json(json)
# print the JSON string representation of the object
print(IncidentNormalAllOfWitnessStatementsInner.to_json())

# convert the object into a dict
incident_normal_all_of_witness_statements_inner_dict = incident_normal_all_of_witness_statements_inner_instance.to_dict()
# create an instance of IncidentNormalAllOfWitnessStatementsInner from a dict
incident_normal_all_of_witness_statements_inner_from_dict = IncidentNormalAllOfWitnessStatementsInner.from_dict(incident_normal_all_of_witness_statements_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


