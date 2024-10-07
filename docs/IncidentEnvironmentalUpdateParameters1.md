# IncidentEnvironmentalUpdateParameters1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environmental_type_id** | **int** | The ID of the Environmental Type | [optional] 
**description** | **str** | Description of event in Rich Text format | [optional] 
**estimated_cost_impact** | **float** | Estimated cost impact of the record | [optional] 
**quantity_value** | **float** | Numeric portion of the \&quot;quantity\&quot; field | [optional] 
**quantity_unit_of_measure** | **str** | Unit of measure for the \&quot;quantity\&quot; field | [optional] 
**affected_company_id** | **int** | The ID of the Affected Company | [optional] 
**managed_equipment_id** | **int** | The ID of the Managed Equipment | [optional] 
**work_activity_id** | **int** | The ID of the Work Activity | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.incident_environmental_update_parameters1 import IncidentEnvironmentalUpdateParameters1

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentEnvironmentalUpdateParameters1 from a JSON string
incident_environmental_update_parameters1_instance = IncidentEnvironmentalUpdateParameters1.from_json(json)
# print the JSON string representation of the object
print(IncidentEnvironmentalUpdateParameters1.to_json())

# convert the object into a dict
incident_environmental_update_parameters1_dict = incident_environmental_update_parameters1_instance.to_dict()
# create an instance of IncidentEnvironmentalUpdateParameters1 from a dict
incident_environmental_update_parameters1_from_dict = IncidentEnvironmentalUpdateParameters1.from_dict(incident_environmental_update_parameters1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


