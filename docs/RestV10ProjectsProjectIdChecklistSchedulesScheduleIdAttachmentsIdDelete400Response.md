# RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**fields** | **str** |  | [optional] 
**reason** | **str** | A human-readable code providing additional detail on the cause of the error. | [optional] 
**error** | [**RestV10CompanyConfigurationGet400ResponseError**](RestV10CompanyConfigurationGet400ResponseError.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete400_response import RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response from a JSON string
rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete400_response_instance = RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete400_response_dict = rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete400_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response from a dict
rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete400_response_from_dict = RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response.from_dict(rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


