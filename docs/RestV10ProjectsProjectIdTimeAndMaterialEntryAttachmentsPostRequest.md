# RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_entry_id** | **int** | Time &amp; Material Id the attachment is associated with | 
**time_and_material_entry_attachment** | [**RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequestTimeAndMaterialEntryAttachment**](RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequestTimeAndMaterialEntryAttachment.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entry_attachments_post_request import RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest from a JSON string
rest_v10_projects_project_id_time_and_material_entry_attachments_post_request_instance = RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_time_and_material_entry_attachments_post_request_dict = rest_v10_projects_project_id_time_and_material_entry_attachments_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest from a dict
rest_v10_projects_project_id_time_and_material_entry_attachments_post_request_from_dict = RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest.from_dict(rest_v10_projects_project_id_time_and_material_entry_attachments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


