# procore_sdk.QualitySafetyIncidentsWitnessStatementAttachmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_witness_statements_witness_statement_id_attachments_post**](QualitySafetyIncidentsWitnessStatementAttachmentsApi.md#rest_v10_projects_project_id_incidents_witness_statements_witness_statement_id_attachments_post) | **POST** /rest/v1.0/projects/{project_id}/incidents/witness_statements/{witness_statement_id}/attachments | Create Attachment


# **rest_v10_projects_project_id_incidents_witness_statements_witness_statement_id_attachments_post**
> IncidentAttachment1 rest_v10_projects_project_id_incidents_witness_statements_witness_statement_id_attachments_post(procore_company_id, project_id, witness_statement_id, attachment)

Create Attachment

Creates an attachment for the specified Witness Statement.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_attachment1 import IncidentAttachment1
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    witness_statement_id = 56 # int | Witness Statement ID
    attachment = None # bytearray | Witness Statement Attachment. To upload an attachment you must upload the entire payload as `multipart/form-data` content-type with the `attachment` file.

    try:
        # Create Attachment
        api_response = api_instance.rest_v10_projects_project_id_incidents_witness_statements_witness_statement_id_attachments_post(procore_company_id, project_id, witness_statement_id, attachment)
        print("The response of QualitySafetyIncidentsWitnessStatementAttachmentsApi->rest_v10_projects_project_id_incidents_witness_statements_witness_statement_id_attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementAttachmentsApi->rest_v10_projects_project_id_incidents_witness_statements_witness_statement_id_attachments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **witness_statement_id** | **int**| Witness Statement ID | 
 **attachment** | **bytearray**| Witness Statement Attachment. To upload an attachment you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type with the &#x60;attachment&#x60; file. | 

### Return type

[**IncidentAttachment1**](IncidentAttachment1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

