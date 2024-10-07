# RestV10FilesIdPatch409ResponseFileFileVersionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File version id | [optional] 
**notes** | **str** | File version notes | [optional] 
**url** | **str** | File version url | [optional] 
**size** | **int** | File version size in bytes | [optional] 
**created_at** | **datetime** | File version created at | [optional] 
**number** | **int** | File version number | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**prostore_file** | [**RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 
**file_id** | **int** | Parent Files id | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_files_id_patch409_response_file_file_versions_inner import RestV10FilesIdPatch409ResponseFileFileVersionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10FilesIdPatch409ResponseFileFileVersionsInner from a JSON string
rest_v10_files_id_patch409_response_file_file_versions_inner_instance = RestV10FilesIdPatch409ResponseFileFileVersionsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10FilesIdPatch409ResponseFileFileVersionsInner.to_json())

# convert the object into a dict
rest_v10_files_id_patch409_response_file_file_versions_inner_dict = rest_v10_files_id_patch409_response_file_file_versions_inner_instance.to_dict()
# create an instance of RestV10FilesIdPatch409ResponseFileFileVersionsInner from a dict
rest_v10_files_id_patch409_response_file_file_versions_inner_from_dict = RestV10FilesIdPatch409ResponseFileFileVersionsInner.from_dict(rest_v10_files_id_patch409_response_file_file_versions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


