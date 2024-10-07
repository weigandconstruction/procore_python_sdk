# RestV10ProjectProjectIdEmailCommunicationsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication** | [**RestV10ProjectProjectIdEmailCommunicationsPostRequestCommunication**](RestV10ProjectProjectIdEmailCommunicationsPostRequestCommunication.md) |  | 
**email** | [**RestV10ProjectProjectIdEmailCommunicationsPostRequestEmail**](RestV10ProjectProjectIdEmailCommunicationsPostRequestEmail.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_project_project_id_email_communications_post_request import RestV10ProjectProjectIdEmailCommunicationsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectProjectIdEmailCommunicationsPostRequest from a JSON string
rest_v10_project_project_id_email_communications_post_request_instance = RestV10ProjectProjectIdEmailCommunicationsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectProjectIdEmailCommunicationsPostRequest.to_json())

# convert the object into a dict
rest_v10_project_project_id_email_communications_post_request_dict = rest_v10_project_project_id_email_communications_post_request_instance.to_dict()
# create an instance of RestV10ProjectProjectIdEmailCommunicationsPostRequest from a dict
rest_v10_project_project_id_email_communications_post_request_from_dict = RestV10ProjectProjectIdEmailCommunicationsPostRequest.from_dict(rest_v10_project_project_id_email_communications_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


