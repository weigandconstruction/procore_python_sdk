# IncidentNormalAllOfActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Action ID | [optional] 
**incident_id** | **int** | Incident ID | [optional] 
**action_type** | [**ActionType**](ActionType.md) |  | [optional] 
**attachments** | [**List[IncidentAttachment]**](IncidentAttachment.md) |  | [optional] 
**description** | **str** | The account of the action in rich text form. | [optional] 
**description_plain_text** | **str** | The account of the action plain text form. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**deleted_at** | **datetime** | Timestamp of deletion | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**observation_id** | **int** | Observation ID | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.incident_normal_all_of_actions_inner import IncidentNormalAllOfActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentNormalAllOfActionsInner from a JSON string
incident_normal_all_of_actions_inner_instance = IncidentNormalAllOfActionsInner.from_json(json)
# print the JSON string representation of the object
print(IncidentNormalAllOfActionsInner.to_json())

# convert the object into a dict
incident_normal_all_of_actions_inner_dict = incident_normal_all_of_actions_inner_instance.to_dict()
# create an instance of IncidentNormalAllOfActionsInner from a dict
incident_normal_all_of_actions_inner_from_dict = IncidentNormalAllOfActionsInner.from_dict(incident_normal_all_of_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


