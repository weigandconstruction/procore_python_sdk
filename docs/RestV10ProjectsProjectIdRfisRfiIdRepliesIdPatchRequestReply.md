# RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequestReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**official** | **bool** | Official Status | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch_request_reply import RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequestReply

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequestReply from a JSON string
rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch_request_reply_instance = RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequestReply.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequestReply.to_json())

# convert the object into a dict
rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch_request_reply_dict = rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch_request_reply_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequestReply from a dict
rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch_request_reply_from_dict = RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequestReply.from_dict(rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch_request_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


