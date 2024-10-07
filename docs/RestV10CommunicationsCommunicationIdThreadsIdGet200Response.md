# RestV10CommunicationsCommunicationIdThreadsIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Body | [optional] 
**cc** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**bcc** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 
**from_external_email** | **bool** | Flag indicating whether the communication originated outside of Procore | [optional] 
**var_from** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**to** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**id** | **int** | ID | [optional] 
**subject** | **str** | Subject | [optional] 
**email_sent_at** | **datetime** | Date email sent | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_communications_communication_id_threads_id_get200_response import RestV10CommunicationsCommunicationIdThreadsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CommunicationsCommunicationIdThreadsIdGet200Response from a JSON string
rest_v10_communications_communication_id_threads_id_get200_response_instance = RestV10CommunicationsCommunicationIdThreadsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CommunicationsCommunicationIdThreadsIdGet200Response.to_json())

# convert the object into a dict
rest_v10_communications_communication_id_threads_id_get200_response_dict = rest_v10_communications_communication_id_threads_id_get200_response_instance.to_dict()
# create an instance of RestV10CommunicationsCommunicationIdThreadsIdGet200Response from a dict
rest_v10_communications_communication_id_threads_id_get200_response_from_dict = RestV10CommunicationsCommunicationIdThreadsIdGet200Response.from_dict(rest_v10_communications_communication_id_threads_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


