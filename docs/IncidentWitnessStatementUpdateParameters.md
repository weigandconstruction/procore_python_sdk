# IncidentWitnessStatementUpdateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement** | **str** | The account of the event by the witness in rich text form. | [optional] 
**date_received** | **date** | Date that the Witness Statement was received. This assumes the dates provided are in the project timezone. | [optional] 
**witness_id** | **int** | Witness ID | [optional] 
**upload_uuids** | **List[str]** | Array of uploaded file UUIDs. | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.incident_witness_statement_update_parameters import IncidentWitnessStatementUpdateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentWitnessStatementUpdateParameters from a JSON string
incident_witness_statement_update_parameters_instance = IncidentWitnessStatementUpdateParameters.from_json(json)
# print the JSON string representation of the object
print(IncidentWitnessStatementUpdateParameters.to_json())

# convert the object into a dict
incident_witness_statement_update_parameters_dict = incident_witness_statement_update_parameters_instance.to_dict()
# create an instance of IncidentWitnessStatementUpdateParameters from a dict
incident_witness_statement_update_parameters_from_dict = IncidentWitnessStatementUpdateParameters.from_dict(incident_witness_statement_update_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


