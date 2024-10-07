# procore_sdk.ProjectManagementRFIRepliesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_rfis_rfi_id_replies_get**](ProjectManagementRFIRepliesApi.md#rest_v10_projects_project_id_rfis_rfi_id_replies_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/{rfi_id}/replies | List RFI Replies
[**rest_v10_projects_project_id_rfis_rfi_id_replies_id_delete**](ProjectManagementRFIRepliesApi.md#rest_v10_projects_project_id_rfis_rfi_id_replies_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/rfis/{rfi_id}/replies/{id} | Delete an RFI Response
[**rest_v10_projects_project_id_rfis_rfi_id_replies_id_get**](ProjectManagementRFIRepliesApi.md#rest_v10_projects_project_id_rfis_rfi_id_replies_id_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/{rfi_id}/replies/{id} | Show RFI Reply
[**rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch**](ProjectManagementRFIRepliesApi.md#rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/rfis/{rfi_id}/replies/{id} | Update RFI Reply
[**rest_v10_projects_project_id_rfis_rfi_id_replies_post**](ProjectManagementRFIRepliesApi.md#rest_v10_projects_project_id_rfis_rfi_id_replies_post) | **POST** /rest/v1.0/projects/{project_id}/rfis/{rfi_id}/replies | Create RFI Reply


# **rest_v10_projects_project_id_rfis_rfi_id_replies_get**
> List[RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner] rest_v10_projects_project_id_rfis_rfi_id_replies_get(procore_company_id, project_id, rfi_id, page=page, per_page=per_page)

List RFI Replies

Returns a list of replies for a specified RFI

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_answers_inner import RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner
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
    api_instance = procore_sdk.ProjectManagementRFIRepliesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rfi_id = 56 # int | RFI ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List RFI Replies
        api_response = api_instance.rest_v10_projects_project_id_rfis_rfi_id_replies_get(procore_company_id, project_id, rfi_id, page=page, per_page=per_page)
        print("The response of ProjectManagementRFIRepliesApi->rest_v10_projects_project_id_rfis_rfi_id_replies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRepliesApi->rest_v10_projects_project_id_rfis_rfi_id_replies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rfi_id** | **int**| RFI ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner]**](RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_rfis_rfi_id_replies_id_delete**
> rest_v10_projects_project_id_rfis_rfi_id_replies_id_delete(procore_company_id, project_id, rfi_id, id)

Delete an RFI Response

Deletes a specified response associated with a specified RFI and specified Project

### Example


```python
import procore_sdk
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
    api_instance = procore_sdk.ProjectManagementRFIRepliesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rfi_id = 56 # int | RFI ID
    id = 56 # int | Reply ID

    try:
        # Delete an RFI Response
        api_instance.rest_v10_projects_project_id_rfis_rfi_id_replies_id_delete(procore_company_id, project_id, rfi_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRepliesApi->rest_v10_projects_project_id_rfis_rfi_id_replies_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rfi_id** | **int**| RFI ID | 
 **id** | **int**| Reply ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted responses |  -  |
**401** | Forbidden |  -  |
**403** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_rfis_rfi_id_replies_id_get**
> RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner rest_v10_projects_project_id_rfis_rfi_id_replies_id_get(procore_company_id, project_id, rfi_id, id)

Show RFI Reply

Returns detailed information on a specified RFI reply

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_answers_inner import RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner
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
    api_instance = procore_sdk.ProjectManagementRFIRepliesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rfi_id = 56 # int | RFI ID
    id = 56 # int | Reply ID

    try:
        # Show RFI Reply
        api_response = api_instance.rest_v10_projects_project_id_rfis_rfi_id_replies_id_get(procore_company_id, project_id, rfi_id, id)
        print("The response of ProjectManagementRFIRepliesApi->rest_v10_projects_project_id_rfis_rfi_id_replies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRepliesApi->rest_v10_projects_project_id_rfis_rfi_id_replies_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rfi_id** | **int**| RFI ID | 
 **id** | **int**| Reply ID | 

### Return type

[**RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner**](RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch**
> RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch(procore_company_id, project_id, rfi_id, id, rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch_request)

Update RFI Reply

Updates a specified RFI reply

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_answers_inner import RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner
from procore_sdk.models.rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch_request import RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementRFIRepliesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rfi_id = 56 # int | RFI ID
    id = 56 # int | Reply ID
    rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch_request = procore_sdk.RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequest() # RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequest | 

    try:
        # Update RFI Reply
        api_response = api_instance.rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch(procore_company_id, project_id, rfi_id, id, rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch_request)
        print("The response of ProjectManagementRFIRepliesApi->rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRepliesApi->rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rfi_id** | **int**| RFI ID | 
 **id** | **int**| Reply ID | 
 **rest_v10_projects_project_id_rfis_rfi_id_replies_id_patch_request** | [**RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequest**](RestV10ProjectsProjectIdRfisRfiIdRepliesIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner**](RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RFI Reply |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_rfis_rfi_id_replies_post**
> RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner rest_v10_projects_project_id_rfis_rfi_id_replies_post(procore_company_id, project_id, rfi_id, rest_v10_projects_project_id_rfis_rfi_id_replies_post_request)

Create RFI Reply

Creates a reply for a specified RFI

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response_all_of_questions_inner_answers_inner import RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner
from procore_sdk.models.rest_v10_projects_project_id_rfis_rfi_id_replies_post_request import RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest
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
    api_instance = procore_sdk.ProjectManagementRFIRepliesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rfi_id = 56 # int | RFI ID
    rest_v10_projects_project_id_rfis_rfi_id_replies_post_request = procore_sdk.RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest() # RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest | 

    try:
        # Create RFI Reply
        api_response = api_instance.rest_v10_projects_project_id_rfis_rfi_id_replies_post(procore_company_id, project_id, rfi_id, rest_v10_projects_project_id_rfis_rfi_id_replies_post_request)
        print("The response of ProjectManagementRFIRepliesApi->rest_v10_projects_project_id_rfis_rfi_id_replies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRepliesApi->rest_v10_projects_project_id_rfis_rfi_id_replies_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rfi_id** | **int**| RFI ID | 
 **rest_v10_projects_project_id_rfis_rfi_id_replies_post_request** | [**RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest**](RestV10ProjectsProjectIdRfisRfiIdRepliesPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner**](RestV10ProjectsProjectIdRfisPost201ResponseAllOfQuestionsInnerAnswersInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

