# Observation3

Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee_id** | **int** | The ID of the Assignee of the Observation Item | [optional] 
**checklist_item_id** | **int** | Sets the origin to the ID of a Checklist Item (Note: the Item&#39;s origin can either be a coordination_issue_id, checklist_list_id or incident_action_id) | [optional] 
**contributing_behavior_id** | **int** | The ID of the Contributing Behavior associated to the Observation Item | [optional] 
**contributing_condition_id** | **int** | The ID of the Contributing Condition associated to the Observation Item | [optional] 
**coordination_issue_id** | **int** | Sets the origin to the ID of a Coordination Issue (Note: the Item&#39;s origin can either be a coordination_issue_id, checklist_list_id or incident_action_id) | [optional] 
**description** | **str** | The Description of the Observation Item | [optional] 
**due_date** | **date** | The Due Date of the Observation Item | [optional] 
**hazard_id** | **int** | The ID of the Hazard associated to the Observation Item | [optional] 
**name** | **str** | The Name of the Observation Item | 
**number** | **str** | The Number of the Observation Item | [optional] 
**incident_action_id** | **int** | Sets the origin to the ID of an Incident Action (Note: the Item&#39;s origin can either be a coordination_issue_id, checklist_list_id or incident_action_id) | [optional] 
**personal** | **bool** | The Personal status of the Observation Item | [optional] [default to True]
**priority** | **str** | The Priority of the Observation Item | [optional] 
**status** | **str** | The Status of the Observation Item. Enum: 0: Initiated, 1: Ready for Review, 2: Not Accepted, 3: Closed | [optional] 
**trade_id** | **int** | The ID of the Trade of the Observation Item | [optional] 
**type_id** | **int** | The ID of the Type of the Observation Item | 
**distribution_member_ids** | **List[int]** | An array of the IDs of the Distribution Member of the Observation Item | [optional] 
**location_id** | **int** | The ID of the Location of the Observation Item. Use either &#x60;location_id&#x60; or &#x60;mt_location&#x60; but not both. | [optional] 
**mt_location** | **List[str]** | Use this for creating a new multi-tier or single-tier Location. This will be ignored if &#x60;location_id&#x60; is provided. | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.observation3 import Observation3

# TODO update the JSON string below
json = "{}"
# create an instance of Observation3 from a JSON string
observation3_instance = Observation3.from_json(json)
# print the JSON string representation of the object
print(Observation3.to_json())

# convert the object into a dict
observation3_dict = observation3_instance.to_dict()
# create an instance of Observation3 from a dict
observation3_from_dict = Observation3.from_dict(observation3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


