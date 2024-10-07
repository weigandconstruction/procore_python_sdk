# RestV10FilesIdPatchRequestFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int** | The ID of the parent folder to move the file to | [optional] 
**name** | **str** | The Name of the file | [optional] 
**checked_out_until** | **datetime** | Check out a file until the specified time. Admins may reset checkout by sending \&quot;null\&quot; | [optional] 
**is_tracked** | **bool** | Status if a file should be tracked (true/false) | [optional] [default to False]
**explicit_permissions** | **bool** | Set file to private (true/false) | [optional] 
**description** | **str** | A description of the file | [optional] 
**data** | **str** | File to use as file data. Note that it&#39;s only possible to post a file using a multipart/form-data body (see RFC 2388). Most HTTP libraries will do the right thing when you pass in an open file or IO stream. Alternatively you can use an upload_uuid (see Company Uploads or Project Uploads). You should not use both file and upload_uuid fields in the same request. | [optional] 
**upload_uuid** | **str** | UUID referencing a previously completed Upload. See Company Uploads or Project Uploads for instructions on how use uploads. You should not use both data and upload_uuid fields in the same request. | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_files_id_patch_request_file import RestV10FilesIdPatchRequestFile

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10FilesIdPatchRequestFile from a JSON string
rest_v10_files_id_patch_request_file_instance = RestV10FilesIdPatchRequestFile.from_json(json)
# print the JSON string representation of the object
print(RestV10FilesIdPatchRequestFile.to_json())

# convert the object into a dict
rest_v10_files_id_patch_request_file_dict = rest_v10_files_id_patch_request_file_instance.to_dict()
# create an instance of RestV10FilesIdPatchRequestFile from a dict
rest_v10_files_id_patch_request_file_from_dict = RestV10FilesIdPatchRequestFile.from_dict(rest_v10_files_id_patch_request_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


