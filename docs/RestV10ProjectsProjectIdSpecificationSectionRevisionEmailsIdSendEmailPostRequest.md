# RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Subject of Email | [optional] 
**body** | **str** | Body of email | [optional] 
**distribution_ids** | **List[int]** |  | 
**cc_distribution_ids** | **List[int]** |  | [optional] 
**bcc_distribution_ids** | **List[int]** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_specification_section_revision_emails_id_send_email_post_request import RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest from a JSON string
rest_v10_projects_project_id_specification_section_revision_emails_id_send_email_post_request_instance = RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_specification_section_revision_emails_id_send_email_post_request_dict = rest_v10_projects_project_id_specification_section_revision_emails_id_send_email_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest from a dict
rest_v10_projects_project_id_specification_section_revision_emails_id_send_email_post_request_from_dict = RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest.from_dict(rest_v10_projects_project_id_specification_section_revision_emails_id_send_email_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


