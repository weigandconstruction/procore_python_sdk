# procore_sdk.ProjectManagementDrawingsDrawingRevisionEmailsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_drawing_revision_emails_id_send_email_post**](ProjectManagementDrawingsDrawingRevisionEmailsApi.md#rest_v10_projects_project_id_drawing_revision_emails_id_send_email_post) | **POST** /rest/v1.0/projects/{project_id}/drawing_revision_emails/{id}/send_email | Send email


# **rest_v10_projects_project_id_drawing_revision_emails_id_send_email_post**
> rest_v10_projects_project_id_drawing_revision_emails_id_send_email_post(procore_company_id, project_id, id, rest_v10_projects_project_id_specification_section_revision_emails_id_send_email_post_request)

Send email

Sends an email with an associated Drawing Revision. The text of the email and recipients are specified in the request body.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_specification_section_revision_emails_id_send_email_post_request import RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingRevisionEmailsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the Drawing Revision to email
    rest_v10_projects_project_id_specification_section_revision_emails_id_send_email_post_request = procore_sdk.RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest() # RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest | 

    try:
        # Send email
        api_instance.rest_v10_projects_project_id_drawing_revision_emails_id_send_email_post(procore_company_id, project_id, id, rest_v10_projects_project_id_specification_section_revision_emails_id_send_email_post_request)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingRevisionEmailsApi->rest_v10_projects_project_id_drawing_revision_emails_id_send_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the Drawing Revision to email | 
 **rest_v10_projects_project_id_specification_section_revision_emails_id_send_email_post_request** | [**RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest**](RestV10ProjectsProjectIdSpecificationSectionRevisionEmailsIdSendEmailPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

