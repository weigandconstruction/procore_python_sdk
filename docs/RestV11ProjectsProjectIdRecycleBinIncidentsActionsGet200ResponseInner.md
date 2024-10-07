# RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner


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
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner from a JSON string
rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner_instance = RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner_dict = rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner from a dict
rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner_from_dict = RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner.from_dict(rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


