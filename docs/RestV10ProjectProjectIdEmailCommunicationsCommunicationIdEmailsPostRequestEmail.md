# RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequestEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Body of the email | [optional] 
**prostore_file_ids** | **List[int]** | Prostore file IDs | [optional] 
**distribution_ids** | **List[int]** | An array of IDs of the Distributions of the topic | [optional] 
**cc_distribution_ids** | **List[int]** | User IDs on the email CC distribution | [optional] 
**bcc_distribution_ids** | **List[int]** | User IDs on the email BCC distribution | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_project_project_id_email_communications_communication_id_emails_post_request_email import RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequestEmail

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequestEmail from a JSON string
rest_v10_project_project_id_email_communications_communication_id_emails_post_request_email_instance = RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequestEmail.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequestEmail.to_json())

# convert the object into a dict
rest_v10_project_project_id_email_communications_communication_id_emails_post_request_email_dict = rest_v10_project_project_id_email_communications_communication_id_emails_post_request_email_instance.to_dict()
# create an instance of RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequestEmail from a dict
rest_v10_project_project_id_email_communications_communication_id_emails_post_request_email_from_dict = RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequestEmail.from_dict(rest_v10_project_project_id_email_communications_communication_id_emails_post_request_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


