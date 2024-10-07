# RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner

Time and Material Entry Attachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**attachment_id** | **int** | ID of the associated prostore file | [optional] 
**content_type** | **str** | Content type | [optional] 
**presentation_url** | **str** | URL | [optional] 
**url** | **str** | URL | [optional] 
**thumbnail_url** | **str** | URL | [optional] 
**filename** | **str** | Filename of Time and Material Entry Attachment | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_time_and_material_entry_attachments_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner from a JSON string
rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_time_and_material_entry_attachments_inner_instance = RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_time_and_material_entry_attachments_inner_dict = rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_time_and_material_entry_attachments_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner from a dict
rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_time_and_material_entry_attachments_inner_from_dict = RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner.from_dict(rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_time_and_material_entry_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


