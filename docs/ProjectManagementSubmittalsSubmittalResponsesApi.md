# procore_sdk.ProjectManagementSubmittalsSubmittalResponsesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_submittal_responses_get**](ProjectManagementSubmittalsSubmittalResponsesApi.md#rest_v10_projects_project_id_submittal_responses_get) | **GET** /rest/v1.0/projects/{project_id}/submittal_responses | List Submittal Responses
[**rest_v10_projects_project_id_submittal_responses_post**](ProjectManagementSubmittalsSubmittalResponsesApi.md#rest_v10_projects_project_id_submittal_responses_post) | **POST** /rest/v1.0/projects/{project_id}/submittal_responses | Create Submittal Response
[**rest_v10_submittal_responses_get**](ProjectManagementSubmittalsSubmittalResponsesApi.md#rest_v10_submittal_responses_get) | **GET** /rest/v1.0/submittal_responses | List Submittal Responses


# **rest_v10_projects_project_id_submittal_responses_get**
> List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse] rest_v10_projects_project_id_submittal_responses_get(procore_company_id, project_id, page=page, per_page=per_page)

List Submittal Responses

List Submittal Responses for the specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_submittals_get200_response_inner_approvers_inner_response import RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse
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
    api_instance = procore_sdk.ProjectManagementSubmittalsSubmittalResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Submittal Responses
        api_response = api_instance.rest_v10_projects_project_id_submittal_responses_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementSubmittalsSubmittalResponsesApi->rest_v10_projects_project_id_submittal_responses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSubmittalsSubmittalResponsesApi->rest_v10_projects_project_id_submittal_responses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse]**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Submittal Responses listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to view Submittal Responses |  -  |
**404** | Project not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_submittal_responses_post**
> RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse rest_v10_projects_project_id_submittal_responses_post(procore_company_id, project_id, rest_v10_projects_project_id_submittal_responses_post_request=rest_v10_projects_project_id_submittal_responses_post_request)

Create Submittal Response

Create a Submittal Response for the specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_submittal_responses_post_request import RestV10ProjectsProjectIdSubmittalResponsesPostRequest
from procore_sdk.models.rest_v11_projects_project_id_submittals_get200_response_inner_approvers_inner_response import RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse
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
    api_instance = procore_sdk.ProjectManagementSubmittalsSubmittalResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_submittal_responses_post_request = procore_sdk.RestV10ProjectsProjectIdSubmittalResponsesPostRequest() # RestV10ProjectsProjectIdSubmittalResponsesPostRequest |  (optional)

    try:
        # Create Submittal Response
        api_response = api_instance.rest_v10_projects_project_id_submittal_responses_post(procore_company_id, project_id, rest_v10_projects_project_id_submittal_responses_post_request=rest_v10_projects_project_id_submittal_responses_post_request)
        print("The response of ProjectManagementSubmittalsSubmittalResponsesApi->rest_v10_projects_project_id_submittal_responses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSubmittalsSubmittalResponsesApi->rest_v10_projects_project_id_submittal_responses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_submittal_responses_post_request** | [**RestV10ProjectsProjectIdSubmittalResponsesPostRequest**](RestV10ProjectsProjectIdSubmittalResponsesPostRequest.md)|  | [optional] 

### Return type

[**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Submittal Response created successfully |  -  |
**403** | User does not have permission to create Submittal Responses |  -  |
**404** | Project not found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_submittal_responses_get**
> List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse] rest_v10_submittal_responses_get(procore_company_id, project_id, page=page, per_page=per_page)

List Submittal Responses

List Submittal Responses for the specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_submittals_get200_response_inner_approvers_inner_response import RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse
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
    api_instance = procore_sdk.ProjectManagementSubmittalsSubmittalResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Submittal Responses
        api_response = api_instance.rest_v10_submittal_responses_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementSubmittalsSubmittalResponsesApi->rest_v10_submittal_responses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSubmittalsSubmittalResponsesApi->rest_v10_submittal_responses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse]**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Submittal Responses listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to view Submittal Responses |  -  |
**404** | Project not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

