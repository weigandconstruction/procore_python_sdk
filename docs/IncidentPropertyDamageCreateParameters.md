# IncidentPropertyDamageCreateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incident_id** | **int** | The ID of the Incident | 
**description** | **str** | Description of event in Rich Text format | [optional] 
**estimated_cost_impact** | **float** | Estimated cost impact of the record | [optional] 
**affected_company_id** | **int** | The ID of the Affected Company | [optional] 
**responsible_company_id** | **int** | The ID of the Responsible Company | [optional] 
**managed_equipment_id** | **int** | The ID of the Managed Equipment | [optional] 
**work_activity_id** | **int** | The ID of the Work Activity | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.incident_property_damage_create_parameters import IncidentPropertyDamageCreateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentPropertyDamageCreateParameters from a JSON string
incident_property_damage_create_parameters_instance = IncidentPropertyDamageCreateParameters.from_json(json)
# print the JSON string representation of the object
print(IncidentPropertyDamageCreateParameters.to_json())

# convert the object into a dict
incident_property_damage_create_parameters_dict = incident_property_damage_create_parameters_instance.to_dict()
# create an instance of IncidentPropertyDamageCreateParameters from a dict
incident_property_damage_create_parameters_from_dict = IncidentPropertyDamageCreateParameters.from_dict(incident_property_damage_create_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


