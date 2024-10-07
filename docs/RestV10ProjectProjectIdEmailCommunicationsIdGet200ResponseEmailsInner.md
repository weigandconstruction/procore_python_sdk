# RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Email ID | [optional] 
**communication_id** | **int** | Communication ID | [optional] 
**private** | **bool** | Private Indicator | [optional] 
**attachments** | [**List[RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerAttachmentsInner]**](RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerAttachmentsInner.md) | Email attachnents | [optional] 
**bcc_distribution** | [**List[RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerBccDistributionInner]**](RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerBccDistributionInner.md) | Users on the email BCC distribution | [optional] 
**body** | **str** | Company name | [optional] 
**sanitized_body_html** | **str** | Body of the email in HTML format | [optional] 
**cc_distribution** | [**List[RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerBccDistributionInner]**](RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerBccDistributionInner.md) | Users on the email CC distribution | [optional] 
**distribution** | [**List[RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerBccDistributionInner]**](RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerBccDistributionInner.md) | An array of users of the Distributions of the topic | [optional] 
**email_sent_at** | **datetime** | Date email sent | [optional] 
**login_information** | [**RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerLoginInformation**](RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerLoginInformation.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_project_project_id_email_communications_id_get200_response_emails_inner import RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInner from a JSON string
rest_v10_project_project_id_email_communications_id_get200_response_emails_inner_instance = RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInner.to_json())

# convert the object into a dict
rest_v10_project_project_id_email_communications_id_get200_response_emails_inner_dict = rest_v10_project_project_id_email_communications_id_get200_response_emails_inner_instance.to_dict()
# create an instance of RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInner from a dict
rest_v10_project_project_id_email_communications_id_get200_response_emails_inner_from_dict = RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInner.from_dict(rest_v10_project_project_id_email_communications_id_get200_response_emails_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


