# Observation1

Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee_id** | **int** | The ID of the User that will be assigned to the Observation Item | [optional] 
**contributing_behavior_id** | **int** | The ID of the Contributing Behavior associated to the Observation Item | [optional] 
**contributing_condition_id** | **int** | The ID of the Contributing Condition associated to the Observation Item | [optional] 
**checklist_item_id** | **int** | Sets the origin to the ID of a Checklist Item (Note: the Item&#39;s origin can either be a coordination_issue_id, checklist_list_id or incident_action_id) | [optional] 
**coordination_issue_id** | **int** | Sets the origin to the ID of a Coordination Issue (Note: the Item&#39;s origin can either be a coordination_issue_id, checklist_list_id or incident_action_id) | [optional] 
**created_by_id** | **int** | The ID of the User creating the Observation Item. Only Observations Admin Users can set the creator | [optional] 
**description** | **str** | The Description of the Observation Item | [optional] 
**due_date** | **date** | The Due Date of the Observation Item | [optional] 
**hazard_id** | **int** | The ID of the Hazard associated to the Observation Item | [optional] 
**incident_action_id** | **int** | Sets the origin to the ID of an Incident Action (Note: the Item&#39;s origin can either be a coordination_issue_id, checklist_list_id or incident_action_id) | [optional] 
**name** | **str** | The Name of the Observation Item | 
**number** | **str** | The Number of the Observation Item | [optional] 
**personal** | **bool** | The Privacy status of the Observation Item | [optional] 
**priority** | **str** | The Priority of the Observation Item | [optional] 
**status** | **str** | The Status of the Observation Item | [optional] 
**trade_id** | **int** | The ID of the Trade of the Observation Item | [optional] 
**type_id** | **int** | The ID of the Type of the Observation Item | 
**distribution_member_ids** | **List[int]** | An array of the User IDs of the Observation Item distribution members | [optional] 
**location_id** | **int** | The ID of the Location of the Observation Item. &#x60;location_id&#x60; takes precedence over &#x60;mt_location&#x60;. | [optional] 
**mt_location** | **List[str]** | Use this for creating a new multi-tier or single-tier Location. This will be ignored if &#x60;location_id&#x60; is provided. | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.observation1 import Observation1

# TODO update the JSON string below
json = "{}"
# create an instance of Observation1 from a JSON string
observation1_instance = Observation1.from_json(json)
# print the JSON string representation of the object
print(Observation1.to_json())

# convert the object into a dict
observation1_dict = observation1_instance.to_dict()
# create an instance of Observation1 from a dict
observation1_from_dict = Observation1.from_dict(observation1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


