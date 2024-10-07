# IncidentInjuryUpdateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_of_death** | **datetime** | Date of death | [optional] 
**description** | **str** | Description of event in Rich Text format | [optional] 
**filing_type** | **str** | Filing Type - The &#39;recordable&#39; filing_type value is deprecated. When a filing type of &#39;recordable&#39; is provided, the &#x60;recordable&#x60; attribute of the Injury will instead be set to &#39;true&#39;. | [optional] 
**hospitalized_overnight** | **bool** | Represents whether the injured person was hospitalized overnight | [optional] 
**recordable** | **bool** | Represents whether the Injury record is recordable | [optional] 
**treated_in_er** | **bool** | Represents whether the injured person was treated in the ER | [optional] 
**treatment_facility_address** | **str** | The street address of the treatment facility | [optional] 
**treatment_facility** | **str** | The name of the treatment facility | [optional] 
**treatment_provider** | **str** | The name of the treatment provider | [optional] 
**work_days_absent** | **int** | The number of days absent from work | [optional] 
**work_days_restricted** | **int** | The number of days on restricted work | [optional] 
**work_days_transferred** | **int** | The number of days transferred | [optional] 
**affliction_type_id** | **int** | The ID of the Affliction Type. This cannot be cleared if there is an affected_body_part. | [optional] 
**body_diagram_type** | **str** |  | [optional] 
**affected_body_parts** | **List[str]** | DEPRECATED - Use body_part_ids instead. The body parts affected by the affliction. This requires an affliction_type to be set. | [optional] 
**affected_person_id** | **int** | The ID of the Affected Person. This only supports full Users from the Users endpoints. | [optional] 
**affected_party_id** | **int** | The ID of the Affected Person. This supports full and reference Users from the People endpoints. | [optional] 
**body_part_ids** | **List[int]** | The IDs of body parts affected by the affliction. This requires an affliction_type to be set. | [optional] 
**harm_source_id** | **int** | The ID of the Harm Source | [optional] 
**affected_company_id** | **int** | The ID of the Affected Company | [optional] 
**managed_equipment_id** | **int** | The ID of the Managed Equipment | [optional] 
**work_activity_id** | **int** | The ID of the Work Activity | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.incident_injury_update_parameters import IncidentInjuryUpdateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentInjuryUpdateParameters from a JSON string
incident_injury_update_parameters_instance = IncidentInjuryUpdateParameters.from_json(json)
# print the JSON string representation of the object
print(IncidentInjuryUpdateParameters.to_json())

# convert the object into a dict
incident_injury_update_parameters_dict = incident_injury_update_parameters_instance.to_dict()
# create an instance of IncidentInjuryUpdateParameters from a dict
incident_injury_update_parameters_from_dict = IncidentInjuryUpdateParameters.from_dict(incident_injury_update_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


