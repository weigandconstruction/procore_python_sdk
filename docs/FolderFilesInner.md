# FolderFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the file. | [optional] 
**name** | **str** | Name of the file. | [optional] 
**parent_id** | **int** | The unique identifier of the file parent. | [optional] 
**size** | **int** | File size in bytes. | [optional] 
**description** | **str** | A description of the file. | [optional] 
**updated_at** | **datetime** | File updated datetime in ISO8601 format. | [optional] 
**created_at** | **datetime** | File created datetime in ISO8601 format. | [optional] 
**checked_out_until** | **datetime** | File checked out until datetime in ISO8601 format. | [optional] 
**name_with_path** | **str** | Full file path with filename. | [optional] 
**private** | **bool** | File private status | [optional] 
**is_tracked** | **bool** | If true, file is being tracked. | [optional] 
**tracked_folder** | **object** | Folder watchers | [optional] 
**checked_out_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**file_type** | **str** | Type of the file. | [optional] 
**file_versions** | [**List[FolderFilesInnerFileVersionsInner]**](FolderFilesInnerFileVersionsInner.md) |  | [optional] 
**legacy_id** | **int** | The unique identifier of the legacy file. | [optional] 
**is_deleted** | **bool** | If true, file is in the recycle bin. | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.folder_files_inner import FolderFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FolderFilesInner from a JSON string
folder_files_inner_instance = FolderFilesInner.from_json(json)
# print the JSON string representation of the object
print(FolderFilesInner.to_json())

# convert the object into a dict
folder_files_inner_dict = folder_files_inner_instance.to_dict()
# create an instance of FolderFilesInner from a dict
folder_files_inner_from_dict = FolderFilesInner.from_dict(folder_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


