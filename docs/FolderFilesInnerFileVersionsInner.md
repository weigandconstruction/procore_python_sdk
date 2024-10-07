# FolderFilesInnerFileVersionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the file version. | [optional] 
**notes** | **str** | File version notes | [optional] 
**url** | **str** | The URL where the file can be downloaded. | [optional] 
**size** | **int** | File version size in bytes. | [optional] 
**created_at** | **datetime** | File version created datetime in ISO8601 format. | [optional] 
**number** | **int** | File version number. | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**prostore_file** | [**RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 
**file_id** | **int** | The unique identifier of the parent files. | [optional] 

## Example

```python
from procore_sdk.models.folder_files_inner_file_versions_inner import FolderFilesInnerFileVersionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FolderFilesInnerFileVersionsInner from a JSON string
folder_files_inner_file_versions_inner_instance = FolderFilesInnerFileVersionsInner.from_json(json)
# print the JSON string representation of the object
print(FolderFilesInnerFileVersionsInner.to_json())

# convert the object into a dict
folder_files_inner_file_versions_inner_dict = folder_files_inner_file_versions_inner_instance.to_dict()
# create an instance of FolderFilesInnerFileVersionsInner from a dict
folder_files_inner_file_versions_inner_from_dict = FolderFilesInnerFileVersionsInner.from_dict(folder_files_inner_file_versions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


