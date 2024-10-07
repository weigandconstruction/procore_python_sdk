# IncidentWitnessStatementUpdateParameters1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement** | **str** | The account of the event by the witness in rich text form. | [optional] 
**date_received** | **date** | Date that the Witness Statement was received. This assumes the dates provided are in the project timezone. | [optional] 
**witness_id** | **int** | Witness ID | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.incident_witness_statement_update_parameters1 import IncidentWitnessStatementUpdateParameters1

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentWitnessStatementUpdateParameters1 from a JSON string
incident_witness_statement_update_parameters1_instance = IncidentWitnessStatementUpdateParameters1.from_json(json)
# print the JSON string representation of the object
print(IncidentWitnessStatementUpdateParameters1.to_json())

# convert the object into a dict
incident_witness_statement_update_parameters1_dict = incident_witness_statement_update_parameters1_instance.to_dict()
# create an instance of IncidentWitnessStatementUpdateParameters1 from a dict
incident_witness_statement_update_parameters1_from_dict = IncidentWitnessStatementUpdateParameters1.from_dict(incident_witness_statement_update_parameters1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


