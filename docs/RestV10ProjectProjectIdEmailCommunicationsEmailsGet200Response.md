# RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | [**List[RestV10ProjectProjectIdEmailCommunicationsEmailsGet200ResponseEmailsInner]**](RestV10ProjectProjectIdEmailCommunicationsEmailsGet200ResponseEmailsInner.md) | An array of IDs of the Distributions of the topic | [optional] 
**total** | **int** | Total count of emails | [optional] 
**new_communication_email** | **str** | Email for creating a new communication thread associated with this topic | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_project_project_id_email_communications_emails_get200_response import RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response from a JSON string
rest_v10_project_project_id_email_communications_emails_get200_response_instance = RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response.to_json())

# convert the object into a dict
rest_v10_project_project_id_email_communications_emails_get200_response_dict = rest_v10_project_project_id_email_communications_emails_get200_response_instance.to_dict()
# create an instance of RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response from a dict
rest_v10_project_project_id_email_communications_emails_get200_response_from_dict = RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response.from_dict(rest_v10_project_project_id_email_communications_emails_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


