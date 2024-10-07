# IncidentNearMissCreateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incident_id** | **int** | The ID of the Incident | 
**description** | **str** | Description of event in Rich Text format | [optional] 
**affected_person_id** | **int** | The ID of the Affected Person. This only supports full Users from the Users endpoints. | [optional] 
**affected_party_id** | **int** | The ID of the Affected Person. This supports full and reference Users from the People endpoints. | [optional] 
**harm_source_id** | **int** | The ID of the Harm Source | [optional] 
**affected_company_id** | **int** | The ID of the Affected Company | [optional] 
**managed_equipment_id** | **int** | The ID of the Managed Equipment | [optional] 
**work_activity_id** | **int** | The ID of the Work Activity | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.incident_near_miss_create_parameters import IncidentNearMissCreateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentNearMissCreateParameters from a JSON string
incident_near_miss_create_parameters_instance = IncidentNearMissCreateParameters.from_json(json)
# print the JSON string representation of the object
print(IncidentNearMissCreateParameters.to_json())

# convert the object into a dict
incident_near_miss_create_parameters_dict = incident_near_miss_create_parameters_instance.to_dict()
# create an instance of IncidentNearMissCreateParameters from a dict
incident_near_miss_create_parameters_from_dict = IncidentNearMissCreateParameters.from_dict(incident_near_miss_create_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


