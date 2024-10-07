# RestV10ProjectProjectIdEmailCommunicationsIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Communication ID | [optional] 
**private** | **bool** | Private Indicator | [optional] 
**subject** | **str** | Subject of the email communication | [optional] 
**emails** | [**List[RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInner]**](RestV10ProjectProjectIdEmailCommunicationsIdGet200ResponseEmailsInner.md) | Emails | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_project_project_id_email_communications_id_get200_response import RestV10ProjectProjectIdEmailCommunicationsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectProjectIdEmailCommunicationsIdGet200Response from a JSON string
rest_v10_project_project_id_email_communications_id_get200_response_instance = RestV10ProjectProjectIdEmailCommunicationsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectProjectIdEmailCommunicationsIdGet200Response.to_json())

# convert the object into a dict
rest_v10_project_project_id_email_communications_id_get200_response_dict = rest_v10_project_project_id_email_communications_id_get200_response_instance.to_dict()
# create an instance of RestV10ProjectProjectIdEmailCommunicationsIdGet200Response from a dict
rest_v10_project_project_id_email_communications_id_get200_response_from_dict = RestV10ProjectProjectIdEmailCommunicationsIdGet200Response.from_dict(rest_v10_project_project_id_email_communications_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


