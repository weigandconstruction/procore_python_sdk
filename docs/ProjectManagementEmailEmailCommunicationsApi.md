# procore_sdk.ProjectManagementEmailEmailCommunicationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_project_project_id_email_communications_communication_id_emails_email_id_download_attachments_get**](ProjectManagementEmailEmailCommunicationsApi.md#rest_v10_project_project_id_email_communications_communication_id_emails_email_id_download_attachments_get) | **GET** /rest/v1.0/project/{project_id}/email_communications/{communication_id}/emails/{email_id}/download_attachments | Download all email attachments
[**rest_v10_project_project_id_email_communications_communication_id_emails_post**](ProjectManagementEmailEmailCommunicationsApi.md#rest_v10_project_project_id_email_communications_communication_id_emails_post) | **POST** /rest/v1.0/project/{project_id}/email_communications/{communication_id}/emails | Create Email
[**rest_v10_project_project_id_email_communications_communication_id_export_get**](ProjectManagementEmailEmailCommunicationsApi.md#rest_v10_project_project_id_email_communications_communication_id_export_get) | **GET** /rest/v1.0/project/{project_id}/email_communications/{communication_id}/export | Export Email Communication to PDF
[**rest_v10_project_project_id_email_communications_emails_get**](ProjectManagementEmailEmailCommunicationsApi.md#rest_v10_project_project_id_email_communications_emails_get) | **GET** /rest/v1.0/project/{project_id}/email_communications/emails | List of Emails
[**rest_v10_project_project_id_email_communications_id_get**](ProjectManagementEmailEmailCommunicationsApi.md#rest_v10_project_project_id_email_communications_id_get) | **GET** /rest/v1.0/project/{project_id}/email_communications/{id} | Show Email Communication
[**rest_v10_project_project_id_email_communications_id_patch**](ProjectManagementEmailEmailCommunicationsApi.md#rest_v10_project_project_id_email_communications_id_patch) | **PATCH** /rest/v1.0/project/{project_id}/email_communications/{id} | Update a private field in Email Communication
[**rest_v10_project_project_id_email_communications_post**](ProjectManagementEmailEmailCommunicationsApi.md#rest_v10_project_project_id_email_communications_post) | **POST** /rest/v1.0/project/{project_id}/email_communications | Create Email Communication


# **rest_v10_project_project_id_email_communications_communication_id_emails_email_id_download_attachments_get**
> RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsEmailIdDownloadAttachmentsGet200Response rest_v10_project_project_id_email_communications_communication_id_emails_email_id_download_attachments_get(procore_company_id, project_id, communication_id, email_id)

Download all email attachments

Return URL to download all email attachments in .zip format

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_project_project_id_email_communications_communication_id_emails_email_id_download_attachments_get200_response import RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsEmailIdDownloadAttachmentsGet200Response
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
    api_instance = procore_sdk.ProjectManagementEmailEmailCommunicationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    communication_id = 56 # int | Communication ID
    email_id = 56 # int | Email ID

    try:
        # Download all email attachments
        api_response = api_instance.rest_v10_project_project_id_email_communications_communication_id_emails_email_id_download_attachments_get(procore_company_id, project_id, communication_id, email_id)
        print("The response of ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_communication_id_emails_email_id_download_attachments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_communication_id_emails_email_id_download_attachments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **communication_id** | **int**| Communication ID | 
 **email_id** | **int**| Email ID | 

### Return type

[**RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsEmailIdDownloadAttachmentsGet200Response**](RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsEmailIdDownloadAttachmentsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_project_project_id_email_communications_communication_id_emails_post**
> RestV10ProjectProjectIdEmailCommunicationsIdGet200Response rest_v10_project_project_id_email_communications_communication_id_emails_post(procore_company_id, project_id, communication_id, topic_type, topic_id, rest_v10_project_project_id_email_communications_communication_id_emails_post_request)

Create Email

Creates a email on a given communication

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_project_project_id_email_communications_communication_id_emails_post_request import RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequest
from procore_sdk.models.rest_v10_project_project_id_email_communications_id_get200_response import RestV10ProjectProjectIdEmailCommunicationsIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementEmailEmailCommunicationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    communication_id = 56 # int | Communication ID
    topic_type = 'topic_type_example' # str | The type of the topic to be associated with the communication
    topic_id = 56 # int | Topic ID
    rest_v10_project_project_id_email_communications_communication_id_emails_post_request = procore_sdk.RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequest() # RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequest | 

    try:
        # Create Email
        api_response = api_instance.rest_v10_project_project_id_email_communications_communication_id_emails_post(procore_company_id, project_id, communication_id, topic_type, topic_id, rest_v10_project_project_id_email_communications_communication_id_emails_post_request)
        print("The response of ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_communication_id_emails_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_communication_id_emails_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **communication_id** | **int**| Communication ID | 
 **topic_type** | **str**| The type of the topic to be associated with the communication | 
 **topic_id** | **int**| Topic ID | 
 **rest_v10_project_project_id_email_communications_communication_id_emails_post_request** | [**RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequest**](RestV10ProjectProjectIdEmailCommunicationsCommunicationIdEmailsPostRequest.md)|  | 

### Return type

[**RestV10ProjectProjectIdEmailCommunicationsIdGet200Response**](RestV10ProjectProjectIdEmailCommunicationsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_project_project_id_email_communications_communication_id_export_get**
> RestV10ProjectProjectIdEmailCommunicationsCommunicationIdExportGet200Response rest_v10_project_project_id_email_communications_communication_id_export_get(procore_company_id, project_id, communication_id, topic_type)

Export Email Communication to PDF

Creates a email communication on a given project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_project_project_id_email_communications_communication_id_export_get200_response import RestV10ProjectProjectIdEmailCommunicationsCommunicationIdExportGet200Response
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
    api_instance = procore_sdk.ProjectManagementEmailEmailCommunicationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    communication_id = 56 # int | Communication ID
    topic_type = 'topic_type_example' # str | The type of the topic to be associated with the communication

    try:
        # Export Email Communication to PDF
        api_response = api_instance.rest_v10_project_project_id_email_communications_communication_id_export_get(procore_company_id, project_id, communication_id, topic_type)
        print("The response of ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_communication_id_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_communication_id_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **communication_id** | **int**| Communication ID | 
 **topic_type** | **str**| The type of the topic to be associated with the communication | 

### Return type

[**RestV10ProjectProjectIdEmailCommunicationsCommunicationIdExportGet200Response**](RestV10ProjectProjectIdEmailCommunicationsCommunicationIdExportGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_project_project_id_email_communications_emails_get**
> RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response rest_v10_project_project_id_email_communications_emails_get(procore_company_id, project_id, topic_type, topic_id, page=page, per_page=per_page)

List of Emails

Return a list of emails.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_project_project_id_email_communications_emails_get200_response import RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response
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
    api_instance = procore_sdk.ProjectManagementEmailEmailCommunicationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    topic_type = 'topic_type_example' # str | The type of the topic to be associated with the communication
    topic_id = 56 # int | Topic ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List of Emails
        api_response = api_instance.rest_v10_project_project_id_email_communications_emails_get(procore_company_id, project_id, topic_type, topic_id, page=page, per_page=per_page)
        print("The response of ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_emails_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_emails_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **topic_type** | **str**| The type of the topic to be associated with the communication | 
 **topic_id** | **int**| Topic ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response**](RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_project_project_id_email_communications_id_get**
> RestV10ProjectProjectIdEmailCommunicationsIdGet200Response rest_v10_project_project_id_email_communications_id_get(procore_company_id, project_id, id)

Show Email Communication

Shows detailed information around a single email communication

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_project_project_id_email_communications_id_get200_response import RestV10ProjectProjectIdEmailCommunicationsIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementEmailEmailCommunicationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Communication ID

    try:
        # Show Email Communication
        api_response = api_instance.rest_v10_project_project_id_email_communications_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Communication ID | 

### Return type

[**RestV10ProjectProjectIdEmailCommunicationsIdGet200Response**](RestV10ProjectProjectIdEmailCommunicationsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_project_project_id_email_communications_id_patch**
> RestV10ProjectProjectIdEmailCommunicationsIdGet200Response rest_v10_project_project_id_email_communications_id_patch(procore_company_id, project_id, id, rest_v10_project_project_id_email_communications_id_patch_request)

Update a private field in Email Communication

Update a private field in email communication on the specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_project_project_id_email_communications_id_get200_response import RestV10ProjectProjectIdEmailCommunicationsIdGet200Response
from procore_sdk.models.rest_v10_project_project_id_email_communications_id_patch_request import RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementEmailEmailCommunicationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Communication ID
    rest_v10_project_project_id_email_communications_id_patch_request = procore_sdk.RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest() # RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest | 

    try:
        # Update a private field in Email Communication
        api_response = api_instance.rest_v10_project_project_id_email_communications_id_patch(procore_company_id, project_id, id, rest_v10_project_project_id_email_communications_id_patch_request)
        print("The response of ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Communication ID | 
 **rest_v10_project_project_id_email_communications_id_patch_request** | [**RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest**](RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectProjectIdEmailCommunicationsIdGet200Response**](RestV10ProjectProjectIdEmailCommunicationsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_project_project_id_email_communications_post**
> RestV10ProjectProjectIdEmailCommunicationsIdGet200Response rest_v10_project_project_id_email_communications_post(procore_company_id, project_id, topic_type, topic_id, rest_v10_project_project_id_email_communications_post_request)

Create Email Communication

Creates a email communication on a given project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_project_project_id_email_communications_id_get200_response import RestV10ProjectProjectIdEmailCommunicationsIdGet200Response
from procore_sdk.models.rest_v10_project_project_id_email_communications_post_request import RestV10ProjectProjectIdEmailCommunicationsPostRequest
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
    api_instance = procore_sdk.ProjectManagementEmailEmailCommunicationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    topic_type = 'topic_type_example' # str | The type of the topic to be associated with the communication
    topic_id = 56 # int | Topic ID
    rest_v10_project_project_id_email_communications_post_request = procore_sdk.RestV10ProjectProjectIdEmailCommunicationsPostRequest() # RestV10ProjectProjectIdEmailCommunicationsPostRequest | 

    try:
        # Create Email Communication
        api_response = api_instance.rest_v10_project_project_id_email_communications_post(procore_company_id, project_id, topic_type, topic_id, rest_v10_project_project_id_email_communications_post_request)
        print("The response of ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailEmailCommunicationsApi->rest_v10_project_project_id_email_communications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **topic_type** | **str**| The type of the topic to be associated with the communication | 
 **topic_id** | **int**| Topic ID | 
 **rest_v10_project_project_id_email_communications_post_request** | [**RestV10ProjectProjectIdEmailCommunicationsPostRequest**](RestV10ProjectProjectIdEmailCommunicationsPostRequest.md)|  | 

### Return type

[**RestV10ProjectProjectIdEmailCommunicationsIdGet200Response**](RestV10ProjectProjectIdEmailCommunicationsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

