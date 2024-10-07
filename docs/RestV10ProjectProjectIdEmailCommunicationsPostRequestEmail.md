# RestV10ProjectProjectIdEmailCommunicationsPostRequestEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Body of the email | [optional] 
**prostore_file_ids** | **List[int]** | Prostore file IDs | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing revision IDs | [optional] 
**file_version_ids** | **List[int]** | File version IDs | [optional] 
**form_ids** | **List[int]** | Form IDs | [optional] 
**image_ids** | **List[int]** | Image IDs | [optional] 
**upload_ids** | **List[str]** | Upload UUIDs | [optional] 
**distribution_ids** | **List[int]** | An array of IDs of the Distributions of the topic | [optional] 
**cc_distribution_ids** | **List[int]** | User IDs on the email CC distribution | [optional] 
**bcc_distribution_ids** | **List[int]** | User IDs on the email BCC distribution | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_project_project_id_email_communications_post_request_email import RestV10ProjectProjectIdEmailCommunicationsPostRequestEmail

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectProjectIdEmailCommunicationsPostRequestEmail from a JSON string
rest_v10_project_project_id_email_communications_post_request_email_instance = RestV10ProjectProjectIdEmailCommunicationsPostRequestEmail.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectProjectIdEmailCommunicationsPostRequestEmail.to_json())

# convert the object into a dict
rest_v10_project_project_id_email_communications_post_request_email_dict = rest_v10_project_project_id_email_communications_post_request_email_instance.to_dict()
# create an instance of RestV10ProjectProjectIdEmailCommunicationsPostRequestEmail from a dict
rest_v10_project_project_id_email_communications_post_request_email_from_dict = RestV10ProjectProjectIdEmailCommunicationsPostRequestEmail.from_dict(rest_v10_project_project_id_email_communications_post_request_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


