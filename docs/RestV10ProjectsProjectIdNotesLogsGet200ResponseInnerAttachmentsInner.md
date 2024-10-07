# RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**name** | **str** | Use :name, :filename to be deprecated | [optional] 
**url** | **str** |  | [optional] 
**filename** | **str** | :filename to be deprecated, use :name | [optional] 
**share_url** | **str** |  | [optional] 
**viewable_type** | **str** |  | [optional] 
**viewable_url** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_notes_logs_get200_response_inner_attachments_inner import RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner from a JSON string
rest_v10_projects_project_id_notes_logs_get200_response_inner_attachments_inner_instance = RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_notes_logs_get200_response_inner_attachments_inner_dict = rest_v10_projects_project_id_notes_logs_get200_response_inner_attachments_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner from a dict
rest_v10_projects_project_id_notes_logs_get200_response_inner_attachments_inner_from_dict = RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner.from_dict(rest_v10_projects_project_id_notes_logs_get200_response_inner_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


