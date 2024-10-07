# RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerLoginInformation

User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**company_name** | **str** | Company Name | [optional] 
**locale** | **str** | User dictionary | [optional] 
**login** | **str** | Login of user | [optional] 
**name** | **str** | User name | [optional] 
**avatar** | **str** | User avatar url | [optional] 
**initials** | **str** | User initials | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_project_project_id_email_communications_id_get200_response_emails_inner_login_information import RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerLoginInformation

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerLoginInformation from a JSON string
rest_v10_project_project_id_email_communications_id_get200_response_emails_inner_login_information_instance = RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerLoginInformation.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerLoginInformation.to_json())

# convert the object into a dict
rest_v10_project_project_id_email_communications_id_get200_response_emails_inner_login_information_dict = rest_v10_project_project_id_email_communications_id_get200_response_emails_inner_login_information_instance.to_dict()
# create an instance of RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerLoginInformation from a dict
rest_v10_project_project_id_email_communications_id_get200_response_emails_inner_login_information_from_dict = RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInnerLoginInformation.from_dict(rest_v10_project_project_id_email_communications_id_get200_response_emails_inner_login_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


