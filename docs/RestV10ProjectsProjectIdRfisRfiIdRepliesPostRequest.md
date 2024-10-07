# RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply** | [**RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequestReply**](RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequestReply.md) |  | 
**attachments** | **List[str]** | RFI Response Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_rfis_rfi_id_replies_post_request import RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest from a JSON string
rest_v10_projects_project_id_rfis_rfi_id_replies_post_request_instance = RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_rfis_rfi_id_replies_post_request_dict = rest_v10_projects_project_id_rfis_rfi_id_replies_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest from a dict
rest_v10_projects_project_id_rfis_rfi_id_replies_post_request_from_dict = RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest.from_dict(rest_v10_projects_project_id_rfis_rfi_id_replies_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


