# RestV10ProjectsProjectIdScheduleGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_features** | [**RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures**](RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures.md) |  | [optional] 
**last_calendar_view** | **str** |  | [optional] 
**schedule_present** | **bool** |  | [optional] 
**schedule_processing** | **bool** |  | [optional] 
**schedule_crud_beta_agreement** | [**RestV10ProjectsProjectIdScheduleGet200ResponseScheduleCrudBetaAgreement**](RestV10ProjectsProjectIdScheduleGet200ResponseScheduleCrudBetaAgreement.md) |  | [optional] 
**schedule_tasks_last_updated_at** | **datetime** | Timestamp of the most recent change to any task in the Schedule. | [optional] 
**schedule_tasks_edited_manually** | **bool** |  | [optional] 
**type** | [**RestV10ProjectsProjectIdScheduleGet200ResponseType**](RestV10ProjectsProjectIdScheduleGet200ResponseType.md) |  | [optional] 
**data_date** | **datetime** | The data datetime of the last imported schedule. | [optional] 
**lookahead_data_date** | **datetime** | The Lookahead&#39;s data datetime. | [optional] 
**number_of_pending_requested_changes** | **float** | The number of pending Requested Changes for the given user. | [optional] 
**uploaded_at** | **datetime** | The upload datetime of the last imported schedule. | [optional] 
**office** | [**Office**](Office.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_schedule_get200_response import RestV10ProjectsProjectIdScheduleGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdScheduleGet200Response from a JSON string
rest_v10_projects_project_id_schedule_get200_response_instance = RestV10ProjectsProjectIdScheduleGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdScheduleGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_schedule_get200_response_dict = rest_v10_projects_project_id_schedule_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdScheduleGet200Response from a dict
rest_v10_projects_project_id_schedule_get200_response_from_dict = RestV10ProjectsProjectIdScheduleGet200Response.from_dict(rest_v10_projects_project_id_schedule_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


